---
layout: catpag
category: Digital Signal Processing
lead: Sampling, Fourier transforms and filters, built up in GNU Radio from first principles.
---

***Note: These lessons were constructed using GNU Radio 3.8. They should be able to be done on different versions of GNU Radio, but be aware that there might be slight differences in some of the blocks.

**A. Introduction to GNU Radio and Some Basic DSP**

* These are the lessons that appear on the [Build a Simple Spectrometer]({{ site.baseurl }}/Simple_Spectrometer) page.

    - [Lesson 1]({{ site.baseurl }}/FilesUploaded/Gnuradio_Lesson1_simpleWaveform.pdf) - Introduction to GNU Radio basics.
    - [Lesson 2]({{ site.baseurl }}/FilesUploaded/Gnuradio_Lesson2_MultipleSources.pdf) - Learning more GNU Radio tools building a multiple waveform source.
    - [Lesson 3]({{ site.baseurl }}/FilesUploaded/Gnuradio_Lesson3_FourierSeries.pdf) - Demonstration of Fourier series.
    - [Lesson 4]({{ site.baseurl }}/FilesUploaded/Gnuradio_Lesson4_FFT.pdf) - Demonstration of how an FFT block works.
    - [Lesson 5]({{ site.baseurl }}/FilesUploaded/Gnuradio_Lesson5_Filters.pdf) - Filter basics.

**B. Quadrature sampling**

* [I/Q sampling, worked through in a notebook]({{ '/iq/' | relative_url }}) — why
a receiver keeps two channels a quarter cycle apart, and what the imaginary part
of a sample actually is. Runnable Python with the plots already rendered.
