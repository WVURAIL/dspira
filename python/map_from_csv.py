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

    if len(fs_hit) != len(fs_h1):
        print("ack!  didn't find same number of maps and hitmaps!")
        exit()

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
    
    pylab.imshow((h1/hit)[:,::-1].transpose(),extent=[0,360,-90,90], interpolation='gaussian', cmap='plasma')
    pylab.xlabel("galactic longitude")
    pylab.ylabel('galactic latitude')
    pylab.title('HI map')
    pylab.savefig('gal_map.pdf')
    pylab.show()
    