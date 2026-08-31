import os
import h5py
import pylab
import argparse
import numpy as np

# Reference temperatures for the Y-factor calibration. The ground is assumed
# to be a 300 K blackbody, empty sky 10 K. Change BOTH here if you change
# either - they each appear in two formulas below via these names.
T_HOT = 300.0    # ground, kelvin
T_COLD = 10.0    # empty sky, kelvin


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Convert telescope data to temperature.") # description is the first line of the docstring
    parser.add_argument('-g', '--ground', action='store', type=str, default='gnd.h5', help="File with data while pointing to the ground")
    parser.add_argument('-s', '--sky', action='store', type=str, default='sky.h5', help="File with data while pointing to an empty sky.")
    parser.add_argument('-o', '--output_file', action='store', type=str, default='tsys.pdf', help="Name of output file.")
    args = parser.parse_args()

    out_base = os.path.splitext(args.output_file)[0]
    fgal = h5py.File(args.sky,'r')
    fgd = h5py.File(args.ground, 'r')
    #Should parse to see how much data in the files.  
    cold = np.mean(fgal['spectrum'][:,:],axis=0)
    hot = np.mean(fgd['spectrum'][:,:],axis=0)
    Y = hot/cold #in linear ratio.  otherwise:Y = 10**((hot-cold)/10.0)
    # Channels where hot and cold are nearly equal (dead channels, band
    # edges) make Y ~ 1 and the formula below blow up. Warn about them.
    flat = np.abs(Y - 1.0) < 1e-3
    if flat.any():
        print("WARNING: %d of %d channels have hot ~ cold (dead channel or"
              % (int(flat.sum()), Y.shape[0]))
        print("band edge). Their Tsys/gain values are meaningless - expect")
        print("spikes there, and treat those channels as bad downstream.")
    T_sys = (T_HOT - Y*T_COLD)/(Y-1)
    gain = cold/(T_COLD + T_sys)
    fstart = fgal.attrs['freq_start']
    fstep = fgal.attrs['freq_step']
    flength = cold.shape[0]
    freq = np.arange(flength)*fstep + fstart
    np.savetxt((out_base+"_Tsys.csv"), T_sys, delimiter="," )
    np.savetxt((out_base+"_gain.csv"), gain, delimiter="," )
    pylab.rcParams['axes.formatter.useoffset'] = False
    pylab.plot(T_sys)
    pylab.ylim(0,600)
    pylab.savefig(out_base+"_Tsys.pdf")
    pylab.clf()
    pylab.plot(gain)
    pylab.savefig(out_base+"_gain.pdf")
    print("DONE SAVING TEMPERATURE.")

