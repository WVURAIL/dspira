# =====================================================================
# WARNING - THIS SCRIPT PRODUCES SKY MAPS WITH THE WRONG POINTING.
#
# Line 114 below reads the elevation as float(str(e)[:-1]), which drops the
# last character before converting. A pointing written "A180E55" - the
# default in this repository's own flowgraphs - is read as elevation 5
# degrees, not 55. Nothing fails and nothing warns; the hydrogen is
# measured correctly and filed at the wrong place on the sky, typically
# 27 to 70 degrees away against a beam about 15 degrees across.
#
# It was not always wrong. Under h5py 2.x the pointing attribute read back
# as bytes, so str() wrapped it in b'...' and the closing quote happened to
# supply the character this code discards. h5py 3.0 (October 2020) returns
# str, and from that point the bug became live for anyone who simply
# updated their packages.
#
# Elevation affects position only - never flux, calibration, system
# temperature or line profiles. Affected maps can be regenerated exactly,
# because the raw HDF5 files still carry the true pointing string.
#
# A corrected version, with a test covering 30 pointing spellings, is at:
#   https://github.com/WVURAIL/dspira-lessons -> code/observations/
#
# This repository is archived and read-only; the code below is left as the
# historical record of what was run, not as something to use.
# =====================================================================

import ephem
import numpy as np
import time
import argparse
import glob
import h5py
import astropy.coordinates as c
import astropy.units as u
from numba import jit

def distance(phi1,lam1,phi2,lam2):
    '''based on vincenty formula   phi is latitude, lam is longitude'''
    num = np.sqrt((np.cos(phi2)*np.sin(np.abs(lam1-lam2)))**2 + (np.cos(phi1)*np.sin(phi2) - np.sin(phi1)*np.cos(phi2)*np.cos(np.abs(lam1-lam2)))**2)
    denom = ( np.sin(phi1)*np.sin(phi2) + np.cos(phi1)*np.cos(phi2)*np.cos(np.abs(lam1-lam2)))
    dist = np.arctan2(num,denom)
    return dist

def telescope(lat = "38.433", lon = "-79.8397" ):
    ## gbo
    tel = ephem.Observer()
    tel.long = lon                
    tel.lat = lat
    tel.pressure = 0
    tel.temp = 0                         
    return tel

seconds_per_julian_day = 86400
d = ephem.Date('1970/01/01 00:00:00:00')

def azEl2Gal(Az, El, t, tel):
    djd = d + t/seconds_per_julian_day
    tel.date=djd
    ra, dec = tel.radec_of(Az,El)
    eq = ephem.Equatorial(ra,dec)
    gc = ephem.Galactic(eq)
    return gc.long, gc.lat

tel = telescope()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Create map from h5 files in a directory") # description is the first line of the docstring
    parser.add_argument('-d', '--directory', action='store', type=str, default=".", help="directory where hdf5 data files are stored")
    parser.add_argument('-n', '--longitude', action='store', type=str, default="-79.8397", help="longitude on earth, in degrees. Negative if west.  Defaults to Green Bank.")
    parser.add_argument('-l', '--latitude', action='store', type=str, default="38.433", help="latitude on earth, in degrees.  Defaults to Green Bank.")
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

    tel = telescope(lat=args.latitude, lon = args.longitude)

    mapsize = 128
    gls = np.arange(mapsize)*2.0*np.pi/mapsize
    gbs = np.arange(mapsize/2.0)*np.pi/(mapsize/2.0) - np.pi/2

    h1map = np.zeros((mapsize,mapsize//2))
    hitmap = np.zeros((mapsize,mapsize//2))
    beamsize2 = 10.0*np.pi/180.0

    for f in fs:
        print(f)
        hf = h5py.File(f, 'r')
        spec = hf['spectrum']
        times = hf['timestamp']
        pointing = str(hf.attrs['pointing'])
        print(pointing)
        ast,e = pointing.split("E")
        #print(ast,e)
        gg, a = ast.split('A')
        #print(gg,a)
        #print(str(a))
        Az = float(str(a))*np.pi/180.0
        try:
            El = float(str(e)[:-1])*np.pi/180.0
        except:
            print("didnt understand Elevation, moving on...")
            continue
        print("Az,El",Az,El)
        ## choose 30s integrations
        deltat = times[1] - times[0]
        nstep = int(30/deltat)
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
            #### correct for gain shifts ####
            #mask_correct_gain_fluctuations = ( freq > 1418.5e6) & (freq < 1419.8e6)    #( freq > 1416.0e6) & (freq < 1419.0e6)
            #offset = s[mask_correct_gain_fluctuations].mean()
            mask_polyfit = ( freq > 1420.8e6) & (freq < 1421.3e6)
            fit = np.polyfit(freq[mask_polyfit],s[mask_polyfit],1)
            fit_function = np.poly1d(fit)
            s = s - fit_function(freq)
            #### mask out airspy tone always there ####
            rfimask = ( freq > 1419.980e6) & (freq < 1420.1e6)
            s[rfimask] = 0
            #### Integrate neutral hydrogen ####
            galmask = ( freq > 1420.3e6) & (freq < 1420.8e6)  #( freq > 1419.0e6) & (freq < 1421.8e6)
            intH1 = s[galmask].sum()
            print("integrated power",intH1)
            l,b = azEl2Gal(Az, El, t, tel )
            print("galactic locatoin",l,b)

            #### Find anything within 15 degrees ####
            #### Add to map all within 15 degrees ####
            #center = c.SkyCoord(frame = "galactic", l=l*u.radian,b=b*u.radian)
            for j,b_pix in enumerate(gbs):
                #print(b_pix)
                #c2 = c.SkyCoord(frame = "galactic", l=l*u.radian,b=b_pix*u.radian)
                #sep = center.separation(c2)
                sep = distance(b,l, b_pix, l)
                if sep < beamsize2:
                    for i,l_pix in enumerate(gls):
                        #c2 = c.SkyCoord(frame = "galactic", l=l_pix*u.radian,b=b_pix*u.radian)
                        sep = distance(b,l, b_pix, l_pix)
                        if sep < beamsize2:
                            h1map[i,j] += intH1
                            hitmap[i,j] += 1
            # except:
            #     print("exception!")
            #     pass

    np.savetxt(("h1map_drift.csv"), h1map, delimiter="," )
    np.savetxt(("hitmap_drift.csv"), hitmap, delimiter="," )