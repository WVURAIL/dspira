# A drift scan with the Green Bank Telescope

`gbt_drift_scan.ipynb` analyzes a real observation. The 2017 RET-DSPIRA cohort fixed the **Green Bank Telescope** on one position for a 24-hour drift scan. They recorded it with their own GNU Radio spectrometer.

It is worth reading even if you never run it. The calibration section shows how the GBT's noise diode converts arbitrary units to kelvin. This known-temperature source switches on and off throughout the observation. This follows the hot/cold calibration principle in [the Observations lesson](https://wvurail.org/dspira/Observations/). The instrument can perform it continuously.

The observation began at 2017-08-01 09:25:56 and ended the following morning. Its dataset contains 19,280 integrations of 4,096 channels.

## Running it

You need `h5py`, `numpy` and `matplotlib`.

**The data file is not in this repository.** The 300 MB HDF5 file remains on Green Bank's systems. The notebook opens it through an absolute path on its original machine:

```python
'/home/dspradio/grc_data/2017-08-01_09.25.56_GBTdrift.h5'
```

The format matches `hdf5_sink` output, so you can apply these techniques to your drift scans. However, this notebook requires adaptation. Three details are specific to this observation. The frequency axis reverses the **GBT's intermediate-frequency downconversion** (`1670.4e6 -
...`). For a horn, use `np.arange(flength)*fstep + fstart` instead. Timestamps include a **+12 h correction for that day's clock error**. Several cells select ranges specific to this 19,280-integration file. Read it as a worked example; the noise-diode
calibration is the part that transfers.

`gbt_rendered_2017.html` preserves the original 2017 run **with its plots**. Read it in any browser without Jupyter. The notebook file itself has cleared outputs.

## What changed when this moved here

The notebook is unchanged apart from two things.

**Its outputs were removed.** The original file was **1.35 MB**. About 99% was JavaScript embedded by `%matplotlib notebook` for interactive plot widgets. Those widgets require classic Jupyter Notebook with a live kernel. They display nothing on GitHub, in JupyterLab, or in modern viewers. So the file was over a megabyte of markup that
displayed no plots. Cleared, it is 13 KB.

**`%matplotlib notebook` is now `%matplotlib inline`.** Running it saves plots into the notebook so they survive sharing. That is the
change that makes the outputs worth keeping next time.
