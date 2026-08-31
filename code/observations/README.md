# Reducing observation data

Six scripts that turn the files your spectrometer saves into a sky map, a
rotation curve, or a plot of power against time. They came from the older
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

(An earlier version of this page also listed `astropy` and `numba`. Neither is
used - they were imported for code that is commented out - and `numba` was a
hard failure on machines it has no build for. The imports are gone.)

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

Writes **four** files, named from what you pass to `-o` with its extension
dropped — `-o tsys.pdf` and `-o tsys` both give:

| File | What it is |
|---|---|
| `tsys_gain.csv` | gain per channel — pass to `-g` below |
| `tsys_Tsys.csv` | system temperature per channel — pass to `-t` below |
| `tsys_gain.pdf`, `tsys_Tsys.pdf` | the same, plotted |

It assumes the ground is 300 K and empty sky is 10 K — `T_HOT` and `T_COLD`
at the top of the file. Channels where ground and sky power are nearly equal
(dead channels, band edges) get a warning: their calibration values are
meaningless and show up as spikes.

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

Writes `h1map_drift.csv` and `hitmap_drift.csv` into the current directory. The
map you want is `h1map / hitmap`: the first is summed signal, the second counts
how many samples landed in each pixel.

> **Tell it which radio you used.** The script's frequency windows depend on
> it, because the radios record very different amounts of band — an Airspy at
> 10 MHz sees ±700 km/s around the line, an RTL-SDR at 2.4 MHz barely ±230.
> Either edit `SDR = "airspy"` near the top of `map_h1_hdf5_drift.py`, or pass
> `--sdr airspy` / `airspy-mini` / `lime` / `pluto` / `rtlsdr` on the command
> line. Each preset matches the setup on the [source block settings
> page](https://wvurail.org/dspira-lessons/Spectrometer_sourceblock_settings),
> not the old per-radio flowgraphs in the archived `dspira` repository — those
> are GNU Radio 3.7 files that 3.8 and later will not open, and three of them
> used different tunings. If the windows don't match the file, the script says
> so rather than producing an empty map.
>
> **If your map comes out empty, check the tuning first.** Until August 2026 the
> RTL-SDR instructions changed `samp_rate` to 2.4e6 but never mentioned `freq`,
> which left the band at 1417.8 – 1420.2 MHz with the 1420.4058 MHz line
> 0.2 MHz outside it. The telescope recorded no hydrogen and the script mapped
> the leftover continuum without complaint. It now reports the band in MHz and
> km/s and skips the file. An RTL-SDR needs **both** `samp_rate` 2.4e6 **and**
> `freq` 1420.5e6.
>
> RTL-SDR users: your band is tight enough that the line is clipped at both
> ends and there is no part of it guaranteed free of hydrogen to fit a baseline
> on, so treat the values as indicative. The tuning also puts the radio's
> spurious centre-of-band tone 0.1 MHz from the line; the script blanks a
> 120 kHz strip there, which on an identical synthetic line costs 26% of the
> measured intensity — 1177.6 against an analytic 1587.2 K·km/s. Retuning to
> 1420.8 MHz brings that to 1.2%, and narrowing `DC_MASK_HALFWIDTH_HZ` would
> too. Neither has been checked against a real observation, so the default has
> not moved; the comment on that constant carries the figures.
>
> Maps from different radios, or different `vec_length` settings, can be
> combined: the script integrates over velocity, so the same sky gives the same
> number regardless of how finely the radio slices the band. Calibrated data
> comes out in **kelvin·km/s**, the standard integrated-intensity unit. The one
> residual difference between radios is window coverage — an RTL-SDR's narrow
> band clips the line's wings, so its values run slightly low on wide lines.

> **The pointing string matters.** This script has to know where the telescope
> was aimed, and the only place that is recorded is the free-text **pointing**
> box in the `hdf5_sink` block. Write azimuth then elevation in degrees —
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

You will see `RuntimeWarning: invalid value encountered in divide`. That is
expected: pixels you have not observed yet have zero hits, so `h1map/hitmap` is
undefined there and they are drawn blank. A partial map is meant to have holes.

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
  mis-read labelled strings (`Data 5 A180E40` came out azimuth 5). The parser
  now reads only unambiguous strings, range-checks the result, and **skips
  loudly rather than guessing** — `test_parse_pointing.py` runs 30 cases,
  including the ones that broke both earlier versions.
- **Repeated timestamps produced a silent blank map.** The sink writes one
  timestamp per work() call, repeated for every vector in it, so the first
  two timestamps are often equal. The cadence now comes from the whole span,
  and if nothing at all could be mapped the script refuses to write map files
  and exits with an error instead of writing zeros that look like empty sky.
- **The RFI mask is now computed, not hardcoded.** The SDR's spurious tone
  sits at the centre of the band wherever the radio is tuned; the old mask
  assumed one particular tuning, missed the spike with the shipped flowgraph,
  and would have integrated it as hydrogen with the radio tuned to the line.
- `map_from_csv.py` draws with `nearest` interpolation (gaussian smeared the
  empty pixels over the observed ones and erased most of a sparse map), puts
  pixels at their true coordinates (everything sat half a pixel off), and
  draws galactic longitude increasing to the left, matching published maps.
- `hdf5_to_csv.py` honours the file's own vector length instead of assuming
  4096. `plot_total_power.py` processes files in time order.
- **The reported intensity depended on the channel width.** The script summed
  channels, so the same sky read twice as high at `vec_length` 8192 as at
  4096, and an RTL-SDR read 4.2× an Airspy. Verified against a synthetic
  20 K line: 308 / 616 / 1232 at three channelisations, against an analytic
  answer of 317.4 K·km/s. It now multiplies by the channel width in km/s —
  a proper integral over velocity — and all three channelisations return
  317.431 exactly.
- **It crashed on modern NumPy.** The timestamp dataset is shaped `(n, 1)` and
  the script called `int()` on a one-element array — an error since NumPy 2.

## Known limitations

- **RTL-SDR has no clean baseline region.** Its 2.4 MHz band is entirely
  within ±250 km/s of the line, so the strips the baseline is fitted on are the
  least-bad available rather than genuinely line-free. Faint high-velocity
  emission can be subtracted along with the continuum.
- **Absolute values have not been validated against a known observation.** The
  windows below were derived from each radio's recorded band, not from a
  calibrated comparison. Maps are good for seeing where the Milky Way is;
  treat the numbers as indicative.
- Files written with the sink's complex IO type, or with more than one input,
  are not handled specially: complex data is cast to real with only a warning,
  and multiple inputs are averaged together.

## What has not been checked

These have been run end to end against synthetic HDF5 files built to match what
`hdf5_sink` writes, which is what caught both bugs above. They have **not** been
re-run against real telescope data. If you have a drift scan from a previous
season, running it through and comparing against the map you got at the time is
worth doing — particularly if that map was made with pointing strings in the
`A180E40` form, since those were being read at a tenth of the intended
elevation.
