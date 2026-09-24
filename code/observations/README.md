# Reducing observation data

Six scripts convert spectrometer files into sky maps, rotation curves, or plots of power against time. They came from the older
`dspira` repository, which is being retired.

They read the HDF5 files written by the `hdf5_sink` block in
[gr-radio_astro](https://github.com/WVURAIL/gr-radio_astro). If you saved with a
plain file sink instead, the reshaping recipe in the
[Observations lesson](https://wvurail.org/dspira-lessons/Observations/) covers
that case.

## What you need

```bash
pip install numpy h5py matplotlib ephem
```

(An earlier version of this page also listed `astropy` and `numba`. Neither is used; both were imported for commented-out code. Importing `numba` failed on machines without a compatible build. The imports are gone.)

## The order to run them in

```
    spectrometer  ──>  *.h5 files
                         │
        ┌────────────────┼─────────────────────┐
        │                │                     │
   (calibrate)      (make a map)         (look at one thing)
        │                │                     │
convert_to_temperature   map_h1_hdf5_drift   plot_total_power
        │                │                   hdf5_to_csv
   gain + Tsys csv ──────┤                   az_el2gal
                         │
                  h1map + hitmap csv
                         │
                   map_from_csv  ──>  gal_map.pdf
```

### 1. Calibrate — `convert_to_temperature.py`

Point at the ground for a "hot" reference and at empty sky for a "cold" one,
save each, then:

```bash
python3 convert_to_temperature.py -g gnd.h5 -s sky.h5 -o tsys.pdf
```

Writes **four** files using the name passed to `-o`, without its extension. Both `-o tsys.pdf` and `-o tsys` produce:

| File | What it is |
|---|---|
| `tsys_gain.csv` | gain per channel — pass to `-g` below |
| `tsys_Tsys.csv` | system temperature per channel — pass to `-t` below |
| `tsys_gain.pdf`, `tsys_Tsys.pdf` | the same, plotted |

It assumes a ground temperature of 300 K and a sky temperature of 10 K. See `T_HOT` and `T_COLD` at the file's top. Channels with nearly equal ground and sky power produce a warning. These include dead channels and band edges. Their calibration values are meaningless and appear as spikes.

One thing it does **not** check: that the calibration and the observation were
taken at the same tuning. The csv files carry no frequency axis, so applying a
gain solution from a different tuning goes undetected. Calibrate at the tuning
you observe with.

### 2. Make a sky map — `map_h1_hdf5_drift.py`

```bash
python3 map_h1_hdf5_drift.py -d ~/my_observation/ -n -79.872 -l 39.659 \
        -g tsys_gain.csv -t tsys_Tsys.csv
```

`-n` is longitude, negative west; `-l` is latitude. Both default to Green Bank.
`-g` and `-t` are optional — without them you get uncalibrated units.

Writes `h1map_drift.csv` and `hitmap_drift.csv` into the current directory. Use `h1map / hitmap` for your map. `h1map` is summed signal; `hitmap` counts samples in each pixel.

> **Tell it which radio you used.** This setting determines the script's frequency windows.
> At 10 MHz, an Airspy covers about ±700 km/s around the line.
> At 2.4 MHz, an RTL-SDR covers barely ±230 km/s.
> Edit `SDR = "airspy"` near the top of `map_h1_hdf5_drift.py`.
> Alternatively, pass `--sdr airspy` on the command line.
> Other supported values are `airspy-mini`, `lime`, `pluto`, and `rtlsdr`. Each preset matches the [source block settings page](https://wvurail.org/dspira-lessons/Spectrometer_sourceblock_settings).
> Archived per-radio flowgraphs in the `dspira` repository use GNU Radio 3.7.
> Versions 3.8 and later cannot open them.
> Three archived flowgraphs also used different tunings. If the windows don't match the file, the script says
> so rather than producing an empty map.
>
> **If your map comes out empty, check the tuning first.** Until August 2026, the RTL-SDR instructions changed `samp_rate` to 2.4e6 without changing `freq`.
> That produced a 1417.8 to 1420.2 MHz band.
> The hydrogen line at 1420.4058 MHz lay about 0.2 MHz outside it. The telescope recorded no hydrogen and the script mapped
> the leftover continuum without complaint. It now reports the band in MHz and
> km/s and skips the file. An RTL-SDR needs **both** `samp_rate` 2.4e6 **and**
> `freq` 1420.5e6.
>
> RTL-SDR users: the narrow band clips both ends of the line.
> No region is guaranteed free of hydrogen for baseline fitting.
> Treat the resulting values as indicative. This tuning places the radio's spurious central tone 0.1 MHz from the line.
> The script blanks a 120 kHz strip there.
> For an identical synthetic line, this loses 26% of the intensity.
> The result is 1177.6 K·km/s, compared with the analytic 1587.2 K·km/s. Retuning to
> 1420.8 MHz brings that to 1.2%, and narrowing `DC_MASK_HALFWIDTH_HZ` would
> too. Neither has been tested against real observations, so the default remains unchanged.
> The constant's comment records these figures.
>
> You can combine maps from different radios or `vec_length` settings.
> Integration over velocity makes results independent of channel width for the same observed sky. Calibrated data
> comes out in **kelvin·km/s**, the standard integrated-intensity unit. Window coverage still differs between radios.
> The RTL-SDR's narrow band clips line wings, slightly underestimating wide-line intensities.

> **The pointing string matters.** The script needs the telescope's pointing.
> This is recorded only in the `hdf5_sink` block's free-text **pointing** box. Write azimuth then elevation in degrees —
> `A180E40` — before you start observing.
>
> The block ships with `AZ,EL` in that box. That is a placeholder, not a value.
> A file saved with it cannot be mapped; the script will say so and skip it.

### 3. Turn the map into a picture — `map_from_csv.py`

```bash
mkdir ~/my_maps && cp h1map_drift.csv hitmap_drift.csv ~/my_maps/
python3 map_from_csv.py -d ~/my_maps/
```

Opens the map in galactic coordinates and saves `gal_map.pdf`. Put several
observations' csv files in the same directory — with distinct names — and they
are combined into one map.

You will see `RuntimeWarning: invalid value encountered in divide`. This is expected. Unobserved pixels have zero hits, making `h1map/hitmap` undefined. They appear blank. A partial map is meant to have holes.

### The other three

| Script | What it does |
|---|---|
| `hdf5_to_csv.py` | One HDF5 file to one csv, frequency in the first column. For opening a spectrum in a spreadsheet. |
| `plot_total_power.py` | **Band-average power** against time across a directory of files — the average over the whole band, not the hydrogen line. Writes `total_power.csv` and `times.csv` and opens a plot, in time order. Useful for watching the system behave during a drift scan. |
| `az_el2gal.py` | Converts one azimuth/elevation and a time into galactic longitude and latitude. `--help` explains the arguments. Handy for planning. |

## Fixes made since these moved here

All found by running the scripts against synthetic HDF5 files built to match
what `hdf5_sink` writes, not by reading them. In `map_h1_hdf5_drift.py`:

- **The elevation was read wrong.** The original parser dropped the last
  character, so `A180E40` was elevation 4, silently. Its first replacement
  mis-read labelled strings (`Data 5 A180E40` came out azimuth 5). The parser accepts only unambiguous strings and checks their ranges. It **reports and skips invalid values instead of guessing**. `test_parse_pointing.py` covers 30 cases, including failures from both earlier versions.
- **Repeated timestamps produced a silent blank map.** The sink repeats one timestamp for every vector in a work() call. The first two timestamps are therefore often equal. Cadence now uses the observation's full span. If nothing can be mapped, the script exits with an error and writes no map files. It no longer writes zeros resembling empty sky.
- **The RFI mask is now computed, not hardcoded.** The SDR's spurious tone always falls at the band center. The old mask assumed a fixed tuning and missed the shipped flowgraph's spike. Tuning the radio to the hydrogen line would have included that spike in the hydrogen integral.
- `map_from_csv.py` uses `nearest` interpolation. Gaussian interpolation blurred empty pixels into observed ones, erasing much of a sparse map. Pixels now use their true coordinates, correcting a half-pixel offset. Galactic longitude increases leftward, as in published maps.
- `hdf5_to_csv.py` honours the file's own vector length instead of assuming
  4096. `plot_total_power.py` processes files in time order.
- **The reported intensity depended on the channel width.** The script previously summed channels. Changing `vec_length` from 4096 to 8192 doubled the same sky's result. An RTL-SDR result was 4.2 times an Airspy result. A synthetic 20 K line gave 308, 616, and 1232 for three channelizations. The analytic value was 317.4 K·km/s. It now multiplies by channel width in km/s to integrate over velocity. All three channelizations return exactly 317.431.
- **It crashed on modern NumPy.** The timestamp dataset has shape `(n, 1)`. The script applied `int()` to a one-element array, which NumPy 2 rejects.

## Known limitations

- **RTL-SDR has no clean baseline region.** Its 2.4 MHz band lies entirely within ±250 km/s of the line. Baseline-fitting regions are the best available, but they are not guaranteed line-free. Faint high-velocity
  emission can be subtracted along with the continuum.
- **Absolute values have not been validated against a known observation.** The
  windows below were derived from each radio's recorded band, not from a
  calibrated comparison. Maps are good for seeing where the Milky Way is;
  treat the numbers as indicative.
- Complex IO and multiple inputs receive no special handling. Complex data becomes real with only a warning. Multiple inputs are averaged together.

## What has not been checked

These scripts were tested end to end using synthetic HDF5 files matching `hdf5_sink` output. Those tests exposed both bugs above. They have **not** been
re-run against real telescope data. Reprocess an earlier season's drift scan and compare the resulting maps. This is especially useful for pointing strings such as `A180E40`. The old parser read those elevations at one tenth of their intended values.
