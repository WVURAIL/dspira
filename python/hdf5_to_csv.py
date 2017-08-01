import numpy as np
import time
import argparse
import glob
import h5py

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create map from csv files in a directory") # description is the first line of the docstring
    parser.add_argument('-f', '--filename', action='store', type=str, default=".", help="hdf5 data file")
    parser.add_argument('-o', '--output_file', action='store', type=str, default='sky.csv', help="Name of output file.")
    args = parser.parse_args()

    f = h5py.File(args.filename,'r')
    spectrum = f['spectrum'][:]          # get the spectrum data
    fstart = f.attrs['freq_start']
    fstep = f.attrs['freq_step']
    flength = spectrum.shape[1]
    freq = np.arange(flength)*fstep + fstart
    f = np.zeros((1,4096))
    f[0] = freq
    data = np.concatenate((f,spectrum), axis=0)
    output = np.transpose(data)
    np.savetxt(args.output_file, output, delimiter=',') # saved to file reshapeddata.txt with a comma delimiter
