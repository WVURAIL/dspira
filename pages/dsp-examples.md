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

These sixteen files generated Python successfully with GNU Radio 3.10.9.2.
Generation checks do not confirm runtime behavior or receiver operation.

- [Signal controls (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/a1.grc)
- [Convolution (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/convolution.grc)
- [Custom noise generator (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/custom-noisegen.grc)
- [Signal source exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/ex01-1.grc)
- [Time display exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/ex01-2.grc)
- [Signal combination exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/ex01-3.grc)
- [Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fourier-series.grc)
- [Square-wave Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fourierseries-square.grc)
- [Triangle-wave Fourier series (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fourierseries-triangle.grc)
- [Sine and cosine transforms (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/ft-sine-cos.grc)
- [Fourier transform pairs (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/ftpairs.grc)
- [Fundamental frequency with IIR filters (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fundamentalfreq-iir.grc)
- [Moving average demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/movavggeir.grc)
- [Sampling (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/sampling.grc)
- [Sampling demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/sampling-demo.grc)
- [Sawtooth Fourier transform (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/sawfft.grc)

## Examples requiring updates

These thirteen examples need compatibility work before use.
Problems include old window constants, disconnected ports, and invalid FFT or decimation settings.
Receiver examples also need suitable drivers and equipment settings.

- [Frequency display exercise (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/ex01-4.grc)
- [FM receiver (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fmradio.grc)
- [FM receiver with equalizer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fmradioeq.grc)
- [Fundamental frequency with FIR filters (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/fundamentalfreq.grc)
- [Mixing sine waves (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/mixing-demo-sines.grc)
- [Frequency and amplitude modulation (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/mixing-demo-sines-freq-amplitude-modulation.grc)
- [Moving average comparison (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/movingaverage.grc)
- [Polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/pfb-spectrometer.grc)
- [Pluto polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/pfb-spectrometer-pluto.grc)
- [RTL-SDR polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/pfb-spectrometer-rtlsdr.grc)
- [LimeSDR spectrometer demonstration (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/spectrometer-demo-lime.grc)
- [LimeSDR polyphase spectrometer (GRC)](https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/institute/spectrometer-pfb-lime.grc)

## Use the collection

The original XML files are imported by GNU Radio Companion.
Review output paths and receiver settings before running an example.
For telescope applications, return to the [software guide]({{ '/software/' | relative_url }}).
For lecture slides, browse [teaching downloads]({{ '/teaching-resources/' | relative_url }}).
