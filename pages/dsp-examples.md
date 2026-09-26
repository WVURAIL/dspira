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

- [Fundamental frequency with FIR filters (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-fir.grc)
- [Fundamental frequency with IIR filters (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-iir.grc)
- [Moving average demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/moving-average-block.grc)
- [Moving average comparison (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/moving-average-comparison.grc)

## Fourier Analysis

- [Convolution (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/convolution.grc)
- [Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/fourier-series.grc)
- [Square-wave Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/square-wave-series.grc)
- [Triangle-wave Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/triangle-wave-series.grc)
- [Sine and cosine transforms (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/sine-cosine-transforms.grc)
- [Fourier transform pairs (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/transform-pairs.grc)
- [Sawtooth Fourier transform (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/sawtooth-transform.grc)
- [Fourier series wave explorer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/wave-explorer.grc)

## Modulation

- [Mixing sine waves (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/modulation/sine-mixing.grc)
- [Frequency and amplitude modulation (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/modulation/frequency-amplitude-modulation.grc)

## Receivers

- [FM receiver (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/receivers/fm-receiver.grc)
- [FM receiver with equalizer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/receivers/fm-receiver-equalizer.grc)

## Sampling

- [Sampling (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/sampling/sampling.grc)
- [Sampling demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/sampling/sampling-demo.grc)

## Signal Basics

- [Signal controls (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-controls.grc)
- [Custom noise generator (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/noise-generator.grc)
- [Signal source exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-source.grc)
- [Time display exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/time-display.grc)
- [Signal combination exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-combination.grc)
- [Frequency display exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/frequency-display.grc)

## Spectrometry

- [Polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer.grc)
- [Pluto polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer-pluto.grc)
- [RTL-SDR polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer-rtl-sdr.grc)
- [LimeSDR spectrometer demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/limesdr-spectrometer-demo.grc)
- [LimeSDR polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/limesdr-polyphase-spectrometer.grc)

## Use the collection

GNU Radio Companion imports these XML files directly.
Generate the moving-average hierarchy before opening its comparison example.
Review output paths and receiver settings before running an example.
The HDF5 spectrometers require your pointing and observation notes before recording.
For telescope applications, return to the [software guide]({{ '/software/' | relative_url }}).
For lecture slides, browse [teaching downloads]({{ '/teaching-resources/' | relative_url }}).
