# A drift scan with the Green Bank Telescope

`gbt_drift_scan.ipynb` walks through a real observation: the 2017 RET-DSPIRA
cohort pointed the **Green Bank Telescope** at a fixed spot and let the sky drift
past for 24 hours, recording with the GNU Radio spectrometer they had built
themselves that summer.

It is worth reading even if you never run it. The calibration section explains
how the GBT's noise diode — a source of known temperature switched on and off
through the observation — turns arbitrary units into kelvin. That is the same
idea as the hot/cold load calibration in
[the Observations lesson](https://wvurail.org/dspira-lessons/Observations/), done
by an instrument that can do it continuously.

The observation ran from 2017-08-01 09:25:56 to the following morning, and the
spectrum dataset is 19,280 integrations of 4,096 channels.

## Running it

You need `h5py`, `numpy` and `matplotlib`.

**The data file is not in this repository.** It is a 300 MB HDF5 file on Green
Bank's systems, and the notebook opens it by an absolute path from the machine it
was written on:

```python
'/home/dspradio/grc_data/2017-08-01_09.25.56_GBTdrift.h5'
```

The file format is the same one `hdf5_sink` writes, so reading your own drift
scan with the same techniques works — but this notebook is not a drop-in
program for it. Three things are specific to this observation: the frequency
axis undoes the **GBT's intermediate-frequency downconversion** (`1670.4e6 -
...`; a horn's file wants the plain `np.arange(flength)*fstep + fstart`), the
timestamps carry a **+12 h correction for a clock that was set wrong that
day**, and several cells slice integration ranges that only exist in this
19,280-integration file. Read it as a worked example; the noise-diode
calibration is the part that transfers.

`gbt_rendered_2017.html` alongside is the original 2017 run rendered **with
its plots**, readable in any browser with no Jupyter needed — the notebook
file itself ships with outputs cleared.

## What changed when this moved here

The notebook is unchanged apart from two things.

**Its outputs were removed.** The original was **1.35 MB**, and about 99% of that
was the JavaScript bootstrap that `%matplotlib notebook` embeds for its
interactive plot widgets. Those widgets only render inside classic Jupyter
Notebook with a live kernel — on GitHub, in JupyterLab, or in any modern viewer
they show nothing at all. So the file was over a megabyte of markup that
displayed no plots. Cleared, it is 13 KB.

**`%matplotlib notebook` is now `%matplotlib inline`,** so that when you do run
it the plots are saved into the notebook and survive being shared. That is the
change that makes the outputs worth keeping next time.
