import numpy as np
import glob
import argparse
import pylab

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create map from csv files in a directory") # description is the first line of the docstring
    parser.add_argument('-d', '--directory', action='store', type=str, default=".", help="directory where hdf5 data files are stored")
    args = parser.parse_args()

    fstring_hit = args.directory + "/hit*.csv"
    fs_hit = glob.glob(fstring_hit)

    fstring_h1 = args.directory + "/h1*.csv"
    fs_h1 = glob.glob(fstring_h1)

    if len(fs_h1) == 0:
        print("No h1*.csv files in %s - nothing to plot." % args.directory)
        print("Copy h1map_drift.csv and hitmap_drift.csv here first.")
        exit(1)

    if len(fs_hit) != len(fs_h1):
        print("ack!  didn't find same number of maps and hitmaps!")
        exit(1)

    first = True

    for i,f in enumerate(fs_h1):
        print(f)
        print(fs_hit[i])
        if first:
            h1 = np.loadtxt(f,delimiter=',')
            hit = np.loadtxt(fs_hit[i],delimiter=',')
            first = False
        else:
            h_dat = np.loadtxt(f,delimiter=',')
            h1 += h_dat
            hit_dat = np.loadtxt(fs_hit[i], delimiter=',')
            hit += hit_dat
    
    # Divide signal by hits; pixels never observed become masked, not NaN.
    # A masked array plus interpolation='nearest' keeps every observed pixel
    # visible - 'gaussian' interpolation smeared NaN into the neighbouring
    # pixels and erased most of a sparse map.
    with np.errstate(invalid='ignore', divide='ignore'):
        sky = np.ma.masked_invalid(h1/hit)

    # Pixel EDGES, not centres: pixel i is centred at i*dl, so the image
    # runs from -dl/2. Without this every feature sat half a pixel (1.4
    # degrees) away from its true coordinates.
    nl, nb = sky.shape
    dl, db = 360.0/nl, 180.0/nb
    pylab.imshow(sky[:,::-1].transpose(),
                 extent=[-dl/2.0, 360.0-dl/2.0, -90.0-db/2.0, 90.0-db/2.0],
                 interpolation='nearest', cmap='plasma')
    # Astronomical maps draw galactic longitude increasing to the LEFT.
    pylab.gca().invert_xaxis()
    pylab.xlabel("galactic longitude")
    pylab.ylabel('galactic latitude')
    pylab.title('HI map')
    pylab.savefig('gal_map.pdf')
    pylab.show()
    