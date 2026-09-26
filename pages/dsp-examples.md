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

## Examples with successful generation checks

These seventeen files generated Python successfully with GNU Radio 3.10.9.2.
Generation checks do not confirm runtime behavior or receiver operation.

- [Signal controls (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-controls.grc)
- [Convolution (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/convolution.grc)
- [Custom noise generator (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/noise-generator.grc)
- [Signal source exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-source.grc)
- [Time display exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/time-display.grc)
- [Signal combination exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/signal-combination.grc)
- [Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/fourier-series.grc)
- [Square-wave Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/square-wave-series.grc)
- [Triangle-wave Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/triangle-wave-series.grc)
- [Sine and cosine transforms (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/sine-cosine-transforms.grc)
- [Fourier transform pairs (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/transform-pairs.grc)
- [Fundamental frequency with IIR filters (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-iir.grc)
- [Moving average demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/moving-average-block.grc)
- [Sampling (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/sampling/sampling.grc)
- [Sampling demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/sampling/sampling-demo.grc)
- [Sawtooth Fourier transform (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/sawtooth-transform.grc)
- [Fourier series wave explorer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/fourier-analysis/wave-explorer.grc)

## Examples requiring updates

These twelve examples need compatibility work before use.
Problems include old window constants, disconnected ports, and invalid FFT or decimation settings.
Receiver examples also need suitable drivers and equipment settings.

- [Frequency display exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/signal-basics/frequency-display.grc)
- [FM receiver (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/receivers/fm-receiver.grc)
- [FM receiver with equalizer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/receivers/fm-receiver-equalizer.grc)
- [Fundamental frequency with FIR filters (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-fir.grc)
- [Mixing sine waves (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/modulation/sine-mixing.grc)
- [Frequency and amplitude modulation (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/modulation/frequency-amplitude-modulation.grc)
- [Moving average comparison (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/moving-average-comparison.grc)
- [Polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer.grc)
- [Pluto polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer-pluto.grc)
- [RTL-SDR polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/polyphase-spectrometer-rtl-sdr.grc)
- [LimeSDR spectrometer demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/limesdr-spectrometer-demo.grc)
- [LimeSDR polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/spectrometry/limesdr-polyphase-spectrometer.grc)

## Use the collection

The original XML files are imported by GNU Radio Companion.
Review output paths and receiver settings before running an example.
For telescope applications, return to the [software guide]({{ '/software/' | relative_url }}).
For lecture slides, browse [teaching downloads]({{ '/teaching-resources/' | relative_url }}).
