---
layout: page
title: DSPIRA signal-processing exercise downloads
permalink: /dsp-examples/
eyebrow: DSP exercises
lead: Explore signals, Fourier analysis, filters, and receiver designs with GNU Radio.
meta_description: "Download 29 DSPIRA GNU Radio exercises for signals, Fourier analysis, sampling, and filters. Review compatibility checks before using them."
---

Download an exercise and open it in GNU Radio Companion.
These files supplement the [DSP laboratory lessons]({{ '/categories/digital-signal-processing/' | relative_url }}).
They live in the classroom software repository, so updates have one home.

## Compatibility checks

All 29 files generated Python successfully with GNU Radio 3.10.9.2.
Eighteen software-only examples also passed brief runtime checks.
These checks do not verify receiver operation or audio devices.
See the [software compatibility report](https://github.com/WVURAIL/dspira-software/blob/main/docs/compatibility.md) for details.

## Filters

- [Fundamental frequency with FIR filters (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-fir.grc){: download="" data-download=""}
- [Fundamental frequency with IIR filters (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-iir.grc){: download="" data-download=""}
- [Moving average demonstration (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/moving-average-block.grc){: download="" data-download=""}
- [Moving average comparison (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/moving-average-comparison.grc){: download="" data-download=""}

## Fourier Analysis

- [Convolution (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/convolution.grc){: download="" data-download=""}
- [Fourier series (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/fourier-series.grc){: download="" data-download=""}
- [Square-wave Fourier series (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/square-wave-series.grc){: download="" data-download=""}
- [Triangle-wave Fourier series (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/triangle-wave-series.grc){: download="" data-download=""}
- [Sine and cosine transforms (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/sine-cosine-transforms.grc){: download="" data-download=""}
- [Fourier transform pairs (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/transform-pairs.grc){: download="" data-download=""}
- [Sawtooth Fourier transform (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/sawtooth-transform.grc){: download="" data-download=""}
- [Fourier series wave explorer (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/wave-explorer.grc){: download="" data-download=""}

## Modulation

- [Mixing sine waves (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/modulation/sine-mixing.grc){: download="" data-download=""}
- [Frequency and amplitude modulation (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/modulation/frequency-amplitude-modulation.grc){: download="" data-download=""}

## Receivers

- [FM receiver (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/receivers/fm-receiver.grc){: download="" data-download=""}
- [FM receiver with equalizer (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/receivers/fm-receiver-equalizer.grc){: download="" data-download=""}

## Sampling

- [Sampling (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/sampling/sampling.grc){: download="" data-download=""}
- [Sampling demonstration (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/sampling/sampling-demo.grc){: download="" data-download=""}

## Signal Basics

- [Signal controls (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-controls.grc){: download="" data-download=""}
- [Custom noise generator (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/noise-generator.grc){: download="" data-download=""}
- [Signal source exercise (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-source.grc){: download="" data-download=""}
- [Time display exercise (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/time-display.grc){: download="" data-download=""}
- [Signal combination exercise (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-combination.grc){: download="" data-download=""}
- [Frequency display exercise (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/frequency-display.grc){: download="" data-download=""}

## Spectrometry

- [Polyphase spectrometer (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer.grc){: download="" data-download=""}
- [Pluto polyphase spectrometer (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer-pluto.grc){: download="" data-download=""}
- [RTL-SDR polyphase spectrometer (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer-rtl-sdr.grc){: download="" data-download=""}
- [LimeSDR spectrometer demonstration (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/limesdr-spectrometer-demo.grc){: download="" data-download=""}
- [LimeSDR polyphase spectrometer (download GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/limesdr-polyphase-spectrometer.grc){: download="" data-download=""}

## Use the collection

GNU Radio Companion imports these XML files directly.
Generate the moving-average hierarchy before opening its comparison example.
Review output paths and receiver settings before running an example.
The HDF5 spectrometers require your pointing and observation notes before recording.
For telescope applications, return to the [software guide]({{ '/software/' | relative_url }}).
For lecture slides, browse [teaching downloads]({{ '/teaching-resources/' | relative_url }}).
