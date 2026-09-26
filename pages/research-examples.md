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
They live in `radio-research-software`, alongside the research applications.

## Download a notebook

- [Pulsar simulation (Jupyter notebook)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/pulsar-simulation.ipynb)
- [Alternative background comparison (Jupyter notebook)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/pulsar-background-comparison.ipynb)
- [Earlier peak-search development (Jupyter notebook)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/pulsar-search-development.ipynb)

Use Python 3, Jupyter, NumPy, SciPy, and Matplotlib.
Generated outputs use a local folder. Saved notebook outputs were cleared during migration.
Full simulations can require substantial memory. Their algorithms and scientific results have not been validated by this move.

## Reference datasets

These original binary files have no headers. Their original parameter labels were not independently verified. Download names now identify each processing stage.
Read the [format and provenance notes](https://github.com/WVURAIL/radio-research-software/tree/main/examples/transients#reference-data) before interpreting them.

- [Pulse samples (BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/signal-int16.bin)
- [Signal-to-noise output (BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/snr.bin)
- [Correlation output (BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/correlation.bin)
- [Dispersion trials (BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/dispersed.bin)
- [Integrated spectra (BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/integrated-fft.bin)
- [Noise samples (BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/noise-int16.bin)

## Design references

- [Full detection flowgraph (GRC)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/bench/dual-stream-detection.grc)
- [Full detection diagram (PNG)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/docs/images/transients/bench/dual-stream-detection.png)
- [Research notes and limitations](https://github.com/WVURAIL/radio-research-software/tree/main/examples/transients)

The flowgraph references retired GNU Radio 3.7 blocks and needs porting before use.
For classroom telescope work, start with the [DSPIRA software guide]({{ '/software/' | relative_url }}).
