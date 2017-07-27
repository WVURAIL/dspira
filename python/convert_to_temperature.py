import h5py
import pylab
import argparse
import numpy as np


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Convert telescope data to temperature.") # description is the first line of the docstring
    parser.add_argument('-g', '--ground', action='store', type=str, default='gnd.h5', help="File with data while pointing to the ground")
    parser.add_argument('-s', '--sky', action='store', type=str, default='sky.h5', help="File with data while pointing to an empty sky.")
    parser.add_argument('-o', '--output_file', action='store', type=str, default='tsys.pdf', help="Name of output file.")
    args = parser.parse_args()

    fgal = h5py.File(args.sky,'r')
    fgd = h5py.File(args.ground, 'r')
    #Should parse to see how much data in the files.  
    cold = fgal['spectrum'][0,:]
    hot = fgd['spectrum'][0,:]
    Y = hot/cold #in linear ratio.  otherwise:Y = 10**((hot-cold)/10.0)
    T_sys = (300.0 - Y*10.0)/(Y-1)  #10 is assumed "cold sky" temperature 300gnd
    fstart = fgal.attrs['freq_start']
    fstep = fgal.attrs['freq_step']
    flength = cold.shape[0]
    freq = np.arange(flength)*fstep + fstart
    np.savetxt((args.output_file[:-4]+".csv"), T_sys, delimiter="," )
    pylab.rcParams['axes.formatter.useoffset'] = False
    pylab.plot(T_sys)
    pylab.ylim(0,600)
    pylab.savefig(args.output_file)
    print("DONE SAVING TEMPERATURE.")

