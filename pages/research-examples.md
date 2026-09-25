---
layout: page
title: Radio transient simulation notebooks and data
permalink: /research-examples/
eyebrow: Research examples
lead: Explore pulsar simulations, reference samples, and transient-detection designs.
meta_description: "Download radio transient research notebooks, binary reference data, and detection diagrams. Read compatibility notes and limitations before using the examples."
---

These exploratory examples support advanced work on pulsars and radio transients.
Andrew Dyck developed them in 2019, with project setup and documentation by Pranav Sanghavi.
They live with the shared astronomy software in `gr-radio_astro`.

## Download a notebook

- [Pulsar simulation (Jupyter notebook)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/pulsar-simulation.ipynb)
- [Alternative background comparison (Jupyter notebook)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/pulsar-background-comparison.ipynb)
- [Earlier peak-search development (Jupyter notebook)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/pulsar-search-development.ipynb)

Use Python 3, Jupyter, NumPy, SciPy, and Matplotlib.
Generated outputs use a local folder. Saved notebook outputs were cleared during migration.
Full simulations can require substantial memory. Their algorithms and scientific results have not been validated by this move.

## Reference datasets

These original binary files have no headers. Their names reflect historical labels, which were not independently verified.
Read the [format and provenance notes](https://github.com/WVURAIL/gr-radio_astro/tree/main/examples/transients#reference-data) before interpreting them.

- [Pulse samples (BIN)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/data/pulse_sim_10mhz_int16_5ms_period_60dm_1400MHz_center_150ms_long.bin)
- [Signal-to-noise output (BIN)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/data/pulse_sim_10mhz_int16_5ms_period_60dm_1400MHz_center_150ms_long_SNR.bin)
- [Correlation output (BIN)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/data/pulse_sim_10mhz_int16_5ms_period_60dm_1400MHz_center_150ms_long_corr.bin)
- [Dispersion trials (BIN)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/data/pulse_sim_10mhz_int16_5ms_period_60dm_1400MHz_center_150ms_long_dispersed.bin)
- [Integrated spectra (BIN)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/data/pulse_sim_10mhz_int16_5ms_period_60dm_1400MHz_center_150ms_long_integrated_FFT.bin)
- [Noise samples (BIN)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/data/pulse_sim_10mhz_int16_5ms_period_60dm_1400MHz_center_150ms_long_noise.bin)

## Design references

- [Full detection flowgraph (GRC)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/dual-stream-detection.grc)
- [Full detection diagram (PNG)](https://raw.githubusercontent.com/WVURAIL/gr-radio_astro/main/examples/transients/dual-stream-detection.grc.png)
- [Research notes and limitations](https://github.com/WVURAIL/gr-radio_astro/tree/main/examples/transients)

The flowgraph references retired GNU Radio 3.7 blocks and needs porting before use.
For classroom telescope work, start with the [DSPIRA software guide]({{ '/software/' | relative_url }}).
