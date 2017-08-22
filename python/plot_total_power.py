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
    fs = glob.glob(fstring)

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
        deltat = times[1:] - times[:-1]
        nstep = int(30/np.median(deltat))
        ntotal = times.shape[0]
        print(nstep)
        print(ntotal)
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
            #### mask out airspy tone always there ####
            rfimask = ( freq > 1419.980e6) & (freq < 1420.1e6)
            s[rfimask] = 0
            #### Integrate Spectrum ####
            intH1 = s.sum()/flength
            print("integrated power",intH1)
            print("time", t)
            ptime.append(t)
            total_power.append(intH1)


            # except:
            #     print("exception!")
            #     pass

    np.savetxt(("total_power.csv"), total_power, delimiter="," )
    np.savetxt(("times.csv"), ptime, delimiter="," )
    pylab.plot(ptime,total_power)
    pylab.show()