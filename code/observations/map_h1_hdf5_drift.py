import sys
import ephem
import numpy as np
import time
import argparse
import glob
import re
import h5py

# =====================================================================
# WHICH RADIO ARE YOU USING?
#
# Change the line below to match your SDR, or pass --sdr on the command
# line. This picks the frequency windows the script integrates the
# hydrogen line over, and the ones it fits the baseline on.
#
# It matters because the radios record very different amounts of band.
# An Airspy at 10 MHz sees +-700 km/s either side of the line and there
# is room to spare; an RTL-SDR at 2.4 MHz sees barely +-230 km/s, and
# asking it for a window it never recorded gives you nothing.
#
SDR = "airspy"      # run with --help to see the full list
#
# =====================================================================

# Windows per radio, in Hz. Velocities are relative to the 1420.40575 MHz
# rest frequency; positive means receding (redshifted, lower frequency).
#
#   band     - what that setup records, for the sanity check further down
#   hi       - integrate the hydrogen line over this range
#   baseline - fit the continuum here and subtract it. These must be
#              free of Galactic hydrogen, which is why they sit far out
#              in the band.
#
# Each entry matches the setup the lessons tell you to build, on
#   wvurail.org/dspira-lessons/Spectrometer_sourceblock_settings
# and NOT the old per-radio flowgraphs in the archived dspira repository.
# Those are GNU Radio 3.7 files that 3.8 and later cannot open, and they used
# different tunings from the documented procedure. If you have changed freq or
# samp_rate yourself, the check further down tells you the windows do not fit
# your file rather than quietly mapping the wrong part of the band.
#
SDR_WINDOWS = {
    # Airspy R2 and LimeSDR: the flowgraph's own defaults - freq 1419 MHz,
    # samp_rate 10e6 - so 1414-1424 MHz. Room for the whole line and a clean
    # baseline either side. The Lime swaps in its own source block, but the
    # lessons leave freq and samp_rate alone, so the band is identical.
    "airspy": {
        "band": (1414.0e6, 1424.0e6),
        "hi": (1419.0e6, 1421.8e6),                      # +297 to -295 km/s
        "baseline": [(1415.0e6, 1418.0e6),               # +1141 to +508 km/s
                     (1422.5e6, 1423.5e6)],              #  -442 to  -653 km/s
    },
    "lime": {
        "band": (1414.0e6, 1424.0e6),
        "hi": (1419.0e6, 1421.8e6),
        "baseline": [(1415.0e6, 1418.0e6), (1422.5e6, 1423.5e6)],
    },
    # Airspy Mini: samp_rate 6e6, freq left at 1419 MHz -> 1416-1422 MHz.
    # The line fits, but 1422.5-1423.5 does not, so there is only room for a
    # baseline on the red side.
    "airspy-mini": {
        "band": (1416.0e6, 1422.0e6),
        "hi": (1419.0e6, 1421.6e6),                      # +297 to -253 km/s
        "baseline": [(1416.3e6, 1418.0e6)],              # +866 to +508 km/s
    },
    # PlutoSDR: samp_rate 3.5e6 AND freq 1421e6 -> 1419.25-1422.75 MHz.
    # Both changes are in the lesson and both matter - at the default
    # 1419 MHz a 3.5 MHz band stops at 1420.75 MHz and clips the red wing.
    # There is no room for a red-side baseline (1419.25-1419.5 is band edge),
    # so the continuum is fitted on the blue side only and extrapolated
    # across the line.
    "pluto": {
        "band": (1419.25e6, 1422.75e6),
        "hi": (1419.5e6, 1421.8e6),                      # +191 to -295 km/s
        "baseline": [(1421.95e6, 1422.55e6)],            # -326 to -452 km/s
    },
    # RTL-SDR: samp_rate 2.4e6 AND freq 1420.5e6 -> 1419.3-1421.7 MHz.
    #
    # The freq change is not optional, and until August 2026 the lesson page
    # did not mention it. Left at the flowgraph's default 1419 MHz, a 2.4 MHz
    # band runs 1417.8-1420.2 MHz and the 1420.4058 MHz line sits 0.2 MHz
    # outside it: the radio records no hydrogen at all. If your older RTL-SDR
    # files map to nothing, check freq_start in the file - that is why.
    #
    # Even tuned correctly this one is tight. The whole band is only
    # +-230 km/s, so:
    #  - the line is clipped at both ends;
    #  - there is NO part of the band guaranteed free of Galactic
    #    hydrogen, so the baseline strips below are the least-bad
    #    choice rather than a clean one. Faint high-velocity emission
    #    can end up subtracted along with the continuum.
    #  - the radio is tuned only 0.1 MHz above the line, so its
    #    centre-of-band spurious tone lands at -20 km/s, right on the
    #    hydrogen. The script masks it (see dc_freq below), but
    #    retuning the flowgraph a MHz away would be better.
    # Maps from an RTL-SDR are fine for seeing where the Milky Way is.
    # Treat the numbers as indicative.
    "rtlsdr": {
        "band": (1419.3e6, 1421.7e6),
        "hi": (1419.6e6, 1421.4e6),                      # +170 to -210 km/s
        "baseline": [(1419.40e6, 1419.55e6),             # +212 to +180 km/s
                     (1421.45e6, 1421.60e6)],            #  -220 to  -252 km/s
    },
}

# Rest frequency of the 21 cm line. Everything velocity-related is measured
# from here.
H1_REST_HZ = 1420.40575177e6
C_KMS = 299792.458

# How much of the band centre to blank, either side, in Hz.
#
# These radios put a spurious tone at the centre of the band - the LO leaking
# into a zero-IF receiver. It is at the tuning frequency wherever you tune, so
# the script computes its position from each file rather than hardcoding one.
#
# The width below is inherited: the original script blanked a fixed
# 1419.98-1420.1 MHz, 120 kHz wide, and this keeps that width while fixing
# where it is centred. It is generous. The artefact itself is essentially one
# FFT bin - 586 Hz on an RTL-SDR at 2.4 MHz with vec_length 4096 - so 120 kHz
# is about two hundred times wider than what it removes.
#
# That does not matter on a radio with band to spare. It matters a lot on an
# RTL-SDR, because the blanked strip lands next to the line. One identical
# synthetic 20 K line, analytic answer 1587.2 K km/s, through this script:
#
#     tuning        band recorded        reported     error
#     1420.4 MHz    1419.2-1421.6 MHz     1093.7      -31%   (line dead centre)
#     1420.5 MHz    1419.3-1421.7 MHz     1177.6      -26%   (what the lesson says)
#     1420.8 MHz    1419.6-1422.0 MHz     1568.6      -1.2%
#
# So an RTL-SDR map is currently about a quarter low, and there are two ways
# to fix it: retune the flowgraph to 1420.8 MHz, or narrow this constant. A
# few thousand Hz would be physically ample. Neither has been checked against
# a real observation, which is the only reason the default has not moved -
# changing it changes every RTL-SDR number the lab has.
DC_MASK_HALFWIDTH_HZ = 6.0e4


POINTING_HELP = (
    "The 'pointing' box in the hdf5_sink block records where the telescope was\n"
    "aimed. Write it as azimuth then elevation in degrees, for example:\n"
    "    A180E40      (azimuth 180, elevation 40)\n"
    "    180,40       also accepted\n"
    "The block ships with 'AZ,EL' in that box. Replace it before you observe -\n"
    "it is a placeholder, not a value, and a file saved with it cannot be mapped."
)

_NUM = r"(-?\d+(?:\.\d+)?)"
_SEP = r"[\s,;/°]*"
# Azimuth first: A / Az / azimuth, then E / El / elevation. The lookbehind
# stops the 'a' inside ordinary words ("Data", "Path", "Antenna") from being
# read as an azimuth marker - that mistake returned (5, 40) for
# "Data 5 A180E40" in an earlier version of this parser.
_AZ_EL = re.compile(
    r"(?<![A-Za-z])A(?:Z(?:IMUTH)?)?\s*[:=]?\s*" + _NUM + _SEP +
    r"E(?:L(?:EVATION)?)?\s*[:=]?\s*" + _NUM, re.I)
# Elevation first: EL / ALT spellings, then AZ.
_EL_AZ = re.compile(
    r"(?<![A-Za-z])(?:EL(?:EVATION)?|ALT(?:ITUDE)?)\s*[:=]?\s*" + _NUM + _SEP +
    r"A(?:Z(?:IMUTH)?)?\s*[:=]?\s*" + _NUM, re.I)


def parse_pointing(pointing):
    """Read an azimuth and elevation in degrees out of the sink's pointing string.

    Returns (azimuth, elevation) in degrees, or None if the string cannot be
    read UNAMBIGUOUSLY. Returning None for a doubtful string is deliberate:
    a skipped file gets noticed, a sample quietly placed at the wrong spot on
    the map does not.

    Accepted: 'A180E40', 'A180E40.', 'Az180 El40', 'AZ 180 EL 40',
    'azimuth=180, elevation=40', 'El40 Az180', 'ALT 40 AZ 180', and a bare
    '180,40' (read as azimuth, elevation). Labels before the pointing are fine
    as long as they contain no digits that could be confused with it.

    Rejected, on purpose: the block's 'AZ,EL' placeholder; strings with no
    numbers; strings with extra numbers and no AZ/EL markers ('scan 3: 180,40'
    - is that azimuth 3 or 180?); and anything whose azimuth is outside
    0..360 or elevation outside -90..90.
    """
    if pointing is None:
        return None
    s = str(pointing).strip()

    m = _AZ_EL.search(s)
    if m:
        az, el = float(m.group(1)), float(m.group(2))
    else:
        m = _EL_AZ.search(s)
        if m:
            el, az = float(m.group(1)), float(m.group(2))
        else:
            nums = re.findall(r"-?\d+(?:\.\d+)?", s)
            # Only trust bare numbers when there are exactly two of them -
            # with a third number in the string there is no way to know which
            # two are the pointing.
            if len(nums) != 2:
                return None
            az, el = float(nums[0]), float(nums[1])

    if not (0.0 <= az <= 360.0) or not (-90.0 <= el <= 90.0):
        return None
    return az, el


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
    parser.add_argument('-s', '--sdr', action='store', type=str, default=SDR,
                        choices=sorted(SDR_WINDOWS),
                        help="which radio recorded the data - sets the frequency "
                             "windows. Defaults to the SDR setting near the top of "
                             "this file (currently %r)." % SDR)
    args = parser.parse_args()

    win = SDR_WINDOWS[args.sdr]
    print("using windows for: %s" % args.sdr)
    print("  hydrogen integrated over %.3f - %.3f MHz"
          % (win['hi'][0]/1e6, win['hi'][1]/1e6))

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

    checked_band = set()

    for f in fs:
        print(f)
        hf = h5py.File(f, 'r')
        spec = hf['spectrum']
        times = hf['timestamp']

        # ---- is the hydrogen line even in this file? -------------------
        # A radio can only see what it recorded. The commonest way to get an
        # empty map is not a bug in this script but a flowgraph left tuned
        # where the line is outside the band - the published RTL-SDR
        # procedure did exactly that for years. Say so, in MHz, rather than
        # integrating a stretch of empty sky and calling it hydrogen.
        try:
            f0 = float(hf.attrs['freq_start'])
            df = float(hf.attrs['freq_step'])
            nch = int(spec.shape[-1])
        except Exception:
            f0 = df = nch = None
        if f0 is not None:
            flo, fhi = f0, f0 + nch*df
            key = (round(flo, -3), round(fhi, -3))
            if H1_REST_HZ < flo or H1_REST_HZ > fhi:
                vlo = (H1_REST_HZ - fhi)/H1_REST_HZ*C_KMS
                vhi = (H1_REST_HZ - flo)/H1_REST_HZ*C_KMS
                print("  This file covers %.3f - %.3f MHz, which is %+.0f to "
                      "%+.0f km/s." % (flo/1e6, fhi/1e6, vlo, vhi))
                print("  The 21 cm line is at %.5f MHz (0 km/s) and that is "
                      "OUTSIDE the band," % (H1_REST_HZ/1e6))
                print("  so the recording is missing the line itself and "
                      "everything on the")
                print("  other side of it. Nothing useful can be mapped from "
                      "it.")
                print("  Check freq and samp_rate in the flowgraph against")
                print("  wvurail.org/dspira-lessons/Spectrometer_sourceblock_settings")
                print("  - an RTL-SDR needs BOTH samp_rate 2.4e6 and freq "
                      "1420.5e6. Set only")
                print("  the sample rate and you get exactly this band.")
                print("  Skipping.")
                hf.close()
                continue
            # Right line, wrong preset: warn once per distinct band.
            blo, bhi = win['band']
            if key not in checked_band:
                checked_band.add(key)
                if abs(flo - blo) > 0.5e6 or abs(fhi - bhi) > 0.5e6:
                    print("  NOTE: this file covers %.3f - %.3f MHz, but the "
                          "--sdr %s windows" % (flo/1e6, fhi/1e6, args.sdr))
                    print("  were written for %.3f - %.3f MHz. The line is in "
                          "band so the map will" % (blo/1e6, bhi/1e6))
                    print("  still build, but check you picked the right radio.")

        pointing = str(hf.attrs['pointing'])
        print(pointing)
        parsed = parse_pointing(pointing)
        if parsed is None:
            print("  Could not read a pointing from %r - skipping this file." % pointing)
            print("  " + POINTING_HELP.replace("\n", "\n  "))
            continue
        az_deg, el_deg = parsed
        print("  read azimuth %g deg, elevation %g deg" % (az_deg, el_deg))
        Az = az_deg*np.pi/180.0
        El = el_deg*np.pi/180.0
        ## choose 30s integrations
        # The sink stores timestamps as an (n, 1) dataset, so flatten before
        # doing arithmetic. NumPy 1.25 deprecated int() on a one-element array
        # and NumPy 2 made it an error, which is why this used to work and
        # then stopped.
        #
        # Do NOT infer the cadence from times[1] - times[0]: the sink writes
        # ONE timestamp per work() call and repeats it for every vector that
        # call delivered, so the first difference is often exactly zero. The
        # span divided by the sample count is immune to that.
        times = np.asarray(times).reshape(-1)
        ntotal = times.shape[0]
        if ntotal < 2 or times[-1] <= times[0]:
            print("  %s has only one distinct timestamp - cannot tell the" % f)
            print("  cadence, so it cannot be averaged into 30 s steps. Skipping.")
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
            #### mask the SDR's DC spike ####
            # The spurious tone these SDRs put in every spectrum sits at the
            # CENTRE of the band, wherever the radio is tuned - so compute it
            # from the file instead of hardcoding a frequency. (The previous
            # hardcoded 1419.98-1420.1 MHz mask assumed one particular tuning;
            # with the shipped flowgraph, tuned to 1419 MHz, it missed the
            # spike entirely, and with a radio tuned to the line it would have
            # let the spike be integrated as hydrogen.)
            dc_freq = fstart + (flength * fstep) / 2.0
            rfimask = ((freq > dc_freq - DC_MASK_HALFWIDTH_HZ) &
                       (freq < dc_freq + DC_MASK_HALFWIDTH_HZ))
            #### correct for gain shifts ####
            #mask_correct_gain_fluctuations = ( freq > 1418.5e6) & (freq < 1419.8e6)    #( freq > 1416.0e6) & (freq < 1419.0e6)
            #offset = s[mask_correct_gain_fluctuations].mean()
            mask_polyfit = np.zeros_like(freq, dtype=bool)
            for blo, bhi in win['baseline']:
                mask_polyfit |= (freq > blo) & (freq < bhi)
            mask_polyfit &= ~rfimask
            if mask_polyfit.sum() < 8:
                print("  The baseline windows for --sdr %s are not in this file's" % args.sdr)
                print("  band (%.3f - %.3f MHz). Wrong --sdr setting? Skipping."
                      % (freq[0]/1e6, freq[-1]/1e6))
                break
            fit = np.polyfit(freq[mask_polyfit],s[mask_polyfit],1)
            fit_function = np.poly1d(fit)
            s = s - fit_function(freq)
            s[rfimask] = 0
            #### Integrate neutral hydrogen ####
            galmask = (freq > win['hi'][0]) & (freq < win['hi'][1]) & ~rfimask
            if galmask.sum() < 8:
                print("  The hydrogen window for --sdr %s is not in this file's" % args.sdr)
                print("  band (%.3f - %.3f MHz). Wrong --sdr setting? Skipping."
                      % (freq[0]/1e6, freq[-1]/1e6))
                break
            # Integrate over VELOCITY, not channels. Summing channels made
            # the answer depend on how finely the radio slices the band:
            # the same 20 K test line read 308 at vec_length 2048, 616 at
            # 4096 and 1232 at 8192 - exactly proportional to the channel
            # count - and an RTL-SDR read 4.2x an Airspy for identical
            # sky. Multiplying by the channel width in km/s makes it a
            # Riemann sum of T dv: the same sky gives the same number on
            # every radio and every vec_length, and calibrated data comes
            # out in K km/s, the standard integrated-intensity unit (the
            # one the LightWork memo maps use).
            dv_kms = (fstep / H1_REST_HZ) * C_KMS
            intH1 = s[galmask].sum() * dv_kms
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

    if hitmap.sum() == 0:
        print("")
        print("No usable data: every file was skipped or empty, so there is")
        print("nothing to map. NOT writing h1map_drift.csv / hitmap_drift.csv -")
        print("an all-zero map looks exactly like an unobserved sky, and that")
        print("is a bad thing to discover three weeks into a drift scan.")
        sys.exit(1)

    np.savetxt(("h1map_drift.csv"), h1map, delimiter="," )
    np.savetxt(("hitmap_drift.csv"), hitmap, delimiter="," )
    print("wrote h1map_drift.csv and hitmap_drift.csv")