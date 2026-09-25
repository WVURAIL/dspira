---
layout: post
date:   2020-07-24
title: What Can a Horn Telescope Measure?
summary:  An overview of what a horn telescope detects
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 2
meta_description: "Find out what a horn radio telescope can measure. Explore hydrogen signals from the Milky Way and the main parts of the DSPIRA receiver."
---

## The Horn Telescope: An Overview

A horn telescope is simply an antenna designed to pick up radio waves. The DSPIRA horn detects radio waves from neutral hydrogen in the Milky Way. These waves have a frequency near 1420 MHz. 
A horn is an antenna, so it receives incident radio waves from any source. The displayed spectrum therefore includes signals from space and the local environment on Earth. Some of these signals are inherent in the data processing system. 

We want to study signals from astronomical objects, such as our galaxy. We therefore subtract other signals the telescope receives. The spectrometer_w_cal.grc GNU Radio program performs this subtraction. It lets us view spectra from the astronomical object of interest.

## What Can a Horn Telescope Measure?

The graph below shows a typical neutral-hydrogen spectrum recorded with a horn and the DSPIRA spectrometer program.

![sample spectrum]({{ site.baseurl }}/images/Sample_spectrum.png)

This graph shows signal amplitude across frequencies from 1414 MHz to 1424 MHz. The neutral hydrogen signal appears at approximately 1420.4 MHz.

So what are the features appearing in this graph?

### The System Background Signal

As mentioned above, part of the signal displayed in the graph is from sources that are not from the galaxy. This can be from noise sources in the local environment as well as signals from the horn detector system itself. Red highlights the signal contributed by the horn system's electronics and digital processing. This pattern is typical of the Airspy software defined radio used with the DSPIRA telescope.

![spectrum background]({{ site.baseurl }}/images/Sample_spectrum_Fig2.png)

Point the telescope toward different sky regions, the ground, a building, or a tree. The highlighted spectral feature keeps its characteristic shape. For stronger signals, the height of the graph will increase, but this general background shape is always there. This is a result of the data signal processing electronics of the telescope system.

The Airspy SDR also typically produces a single spike at 1420.0 MHz. This comes from the Airspy electronics and is not of interest to us.

The *spectrometer_w_cal.grc* program can reduce noise spikes and subtract the characteristic background signal. This allows the user to display the spectrum of signals that come from only the galaxy.

### The Signal from Neutral Hydrogen

For spectral-line observations, look for the small peak near 1420.4 MHz. This is the peak identified in the spectrum below.

![spectrum HI peak]({{ site.baseurl }}/images/HornIntro_Fig3.png)

This 1420.4 MHz signal is from radio waves detected from neutral hydrogen atoms in our galaxy. These radio waves result from a transition involving the electrons in hydrogen atoms. The signal emitted from each atom is extremely weak. Our galaxy contains abundant neutral hydrogen. This lets us detect its signal with a radio telescope on Earth. We cannot see these hydrogen atoms directly with the naked eye. This is where the horn radio telescope becomes useful!
