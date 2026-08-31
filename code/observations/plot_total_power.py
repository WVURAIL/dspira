import numpy as np
import time
import argparse
import glob
import h5py
import pylab


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Create map from h5 files in a directory") # description is the first line of the docstring
    parser.add_argument('-d', '--directory', action='store', type=str, default=".", help="directory where hdf5 data files are stored")
    parser.add_argument('-g', '--gain', action='store', type=str, default=None, help="csv File with gain solution")
    parser.add_argument('-t', '--tsys', action='store', type=str, default=None, help="csv file with temperature solution")
    args = parser.parse_args() 

    fstring = args.directory + "/*.h5"
    # sorted() matters: glob returns files in arbitrary filesystem order, and
    # an unsorted list here plotted the time series scrambled.
    fs = sorted(glob.glob(fstring))

    if args.gain:
        gain = np.loadtxt(args.gain, delimiter=',')
    else:
        gain = 1.0
    
    if args.tsys:
        tsys = np.loadtxt(args.tsys, delimiter=',')
    else:
        tsys = 0.0

    total_power = []
    ptime = []

    for f in fs:
        print(f)
        hf = h5py.File(f, 'r')
        spec = hf['spectrum']
        times = hf['timestamp']
        pointing = str(hf.attrs['pointing'])
        print(pointing)

        ## choose 30s integrations
        # The sink writes one timestamp per work() call, repeated for every
        # vector in it, so first differences are often zero - infer the
        # cadence from the whole span instead.
        times = np.asarray(times).reshape(-1)
        ntotal = times.shape[0]
        if ntotal < 2 or times[-1] <= times[0]:
            print("  only one distinct timestamp - skipping this file")
            continue
        deltat = float(times[-1] - times[0]) / (ntotal - 1)
        nstep = max(1, int(round(30.0/deltat)))
        print("  %d samples, %g s apart on average, averaging %d per step" % (ntotal, deltat, nstep))
        for k in range(0,ntotal,nstep):
            print(k)
            t = times[k:k+nstep].mean()
            s = spec[k:k+nstep].mean(axis=0)
            fstart = hf.attrs['freq_start']
            fstep = hf.attrs['freq_step']
            flength = s.shape[0]
            freq = np.arange(flength)*fstep + fstart
            #### Apply cal here ####
            s = s/gain - tsys
            #### mask the SDR's DC spike (centre of the band, wherever tuned) ####
            dc_freq = fstart + (flength * fstep) / 2.0
            rfimask = ( freq > dc_freq - 6.0e4) & (freq < dc_freq + 6.0e4)
            s[rfimask] = 0
            #### Band-average power ####
            # This is the average over the WHOLE band, not the hydrogen line -
            # useful for watching the system, not for line work.
            band_power = s.sum()/flength
            print("band-average power", band_power)
            print("time", t)
            ptime.append(t)
            total_power.append(band_power)


            # except:
            #     print("exception!")
            #     pass

    if not ptime:
        print("no usable files - nothing to plot")
        raise SystemExit(1)
    # Plot in time order even if the files arrived out of order.
    order = np.argsort(ptime)
    ptime = np.asarray(ptime)[order]
    total_power = np.asarray(total_power)[order]
    np.savetxt(("total_power.csv"), total_power, delimiter="," )
    np.savetxt(("times.csv"), ptime, delimiter="," )
    pylab.plot(ptime,total_power)
    pylab.show()