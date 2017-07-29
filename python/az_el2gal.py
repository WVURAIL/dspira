import ephem
import numpy as np
import time
import argparse

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
    return gc.lat, gc.long

tel = telescope()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Convert azimuth and elevation to galactic latitude and longitude") # description is the first line of the docstring
    parser.add_argument('-a', '--azimuth', action='store', type=float, default=180, help="Azimuth pointing, east 90, 180 is south, 270 west")
    parser.add_argument('-e', '--elevation', action='store', type=float, default=30, help="Elevation from horizon.  90 is zenith")
    parser.add_argument('-t', '--time', action='store', type=float, default=0, help="time. expects a python time.time() format.  if blank will use now")
    parser.add_argument('-n', '--longitude', action='store', type=str, default="-79.8397", help="longitude on earth, in degrees. Negative if west.  Defaults to Green Bank.")
    parser.add_argument('-d', '--latitude', action='store', type=str, default="38.433", help="latitude on earth, in degrees.  Defaults to Green Bank.")
    args = parser.parse_args()

    Az = args.azimuth*np.pi/180.0
    El = args.elevation*np.pi/180.0
    if args.time == 0:
        t = time.time()
    else:
        t = args.time
    tel = telescope(lat=args.latitude, lon = args.longitude)
    l,b = azEl2Gal(Az, El, t, tel )
    print("Galactic Longitude: {0}".format(l))
    print("Galactic Latitude: {0}".format(b))