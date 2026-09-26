---
permalink: /Simple_Spectrometer
layout: post
date:   2021-07-04
title:  Build a Simple Spectrometer
summary:  Introductory GNU Radio lessons are presented along with steps for building a simple spectrometer
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 9
meta_description: "Build a simple radio astronomy spectrometer in GNU Radio. Follow introductory lessons and connect the processing blocks into a flowgraph."
equipment: "GNU Radio and the linked lesson PDFs. The waveform exercises need no receiver; live telescope input requires an SDR."
preparation: "Begin with the introductory waveform lessons. Review FFTs and filters before building the spectrometer."
---


+ Introductory Lessons on Using GNU Radio and Some Basic DSP
    - [Lesson 1]({{ site.baseurl }}/assets/worksheets/simple-spectrometer/01-simple-waveform.pdf) · [Editable Word]({{ '/assets/worksheets/simple-spectrometer/01-simple-waveform.docx' | relative_url }}) - Introduction to GNU Radio basics.
    - [Lesson 2]({{ site.baseurl }}/assets/worksheets/simple-spectrometer/02-multiple-sources.pdf) · [Editable Word]({{ '/assets/worksheets/simple-spectrometer/02-multiple-sources.docx' | relative_url }}) - Learning more GNU Radio tools building a multiple waveform source.
    - [Lesson 3]({{ site.baseurl }}/assets/worksheets/simple-spectrometer/03-fourier-series.pdf) · [Editable Word]({{ '/assets/worksheets/simple-spectrometer/03-fourier-series.docx' | relative_url }}) - Demonstration of Fourier series.
    - [Lesson 4]({{ site.baseurl }}/assets/worksheets/simple-spectrometer/04-fft.pdf) · [Editable Word]({{ '/assets/worksheets/simple-spectrometer/04-fft.docx' | relative_url }}) - Demonstration of how an FFT block works.
    - [Lesson 5]({{ site.baseurl }}/assets/worksheets/simple-spectrometer/05-filters.pdf) · [Editable Word]({{ '/assets/worksheets/simple-spectrometer/05-filters.docx' | relative_url }}) - Filter basics.

+ [Build a Simple Spectrometer]({{ site.baseurl }}/assets/lessons/simple-spectrometer/build-a-spectrometer.pdf) · [Editable Word]({{ '/assets/lessons/simple-spectrometer/build-a-spectrometer.docx' | relative_url }}) - Directions on building a simple spectrometer for a horn telescope, with detailed explanations of the blocks.

Teachers can download [editable Word versions of all five worksheets]({{ '/teaching-resources/#editable-gnu-radio-worksheets' | relative_url }}).

## Notes for the spectrometer guide

The PDF uses older GNU Radio screenshots. Use the [current receiver settings]({{ '/Spectrometer_sourceblock_settings' | relative_url }}) when configuring your SDR.

The [current examples]({{ '/dsp-examples/' | relative_url }}) include flowgraphs checked with GNU Radio 3.10.
