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

## Read a notebook

Read each notebook directly on DSPIRA. Each page includes a download for opening the example in Jupyter.

- [Pulsar simulation]({{ '/notebooks/pulsar-simulation/' | relative_url }})
- [Alternative background comparison]({{ '/notebooks/pulsar-background-comparison/' | relative_url }})
- [Earlier peak-search development]({{ '/notebooks/pulsar-search-development/' | relative_url }})
- [Bench data comparison]({{ '/notebooks/bench-development/' | relative_url }})

The [notebook catalog]({{ '/notebooks/' | relative_url }}) also includes the classroom examples.

Use Python 3, Jupyter, NumPy, SciPy, and Matplotlib.
Generated outputs use a local folder. The three pulsar notebooks have no saved outputs.
The bench comparison retains its original results but requires unavailable recordings.
Full simulations can require substantial memory. Their algorithms and scientific results have not been validated by this move.

## Reference datasets

These original binary files have no headers. Their original parameter labels were not independently verified. Download names now identify each processing stage.
Read the [format and provenance notes](https://github.com/WVURAIL/radio-research-software/tree/main/examples/transients#reference-data) before interpreting them.

- [Pulse samples (download BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/signal-int16.bin)
- [Signal-to-noise output (download BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/snr.bin)
- [Correlation output (download BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/correlation.bin)
- [Dispersion trials (download BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/dispersed.bin)
- [Integrated spectra (download BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/integrated-fft.bin)
- [Noise samples (download BIN)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/data/pulse-simulation-2019/noise-int16.bin)

## Design references

- [Full detection flowgraph (download GRC)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/examples/transients/bench/dual-stream-detection.grc){: download="" data-download=""}
- [Full detection diagram (PNG)](https://raw.githubusercontent.com/WVURAIL/radio-research-software/main/docs/images/transients/bench/dual-stream-detection.png)
- [Research notes and limitations](https://github.com/WVURAIL/radio-research-software/tree/main/examples/transients)

The flowgraph references retired GNU Radio 3.7 blocks and needs porting before use.
For classroom telescope work, start with the [DSPIRA software guide]({{ '/software/' | relative_url }}).
