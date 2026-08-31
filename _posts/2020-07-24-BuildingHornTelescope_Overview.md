---
layout: post
date:  2020-07-25
title: What is Needed to Build a Horn Radio Telescope
summary:  Overview of the different parts of a horn telescope
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Horn Construction']
order: 1
---
A list of the components that are needed to build and operate a horn radio telescope system is presented below. Links to documentation and instructional videos are provided where applicable.

For the reasoning behind the design — why the horn has the dimensions it does,
and how that follows from observing the 21 cm line — see
[Horn Telescope Design]({{ site.baseurl }}/FilesUploaded/HornTelescope_Design.pdf){: .button}

### What's Needed for a Complete Horn Radio Telescope System
   - the horn & antenna assembly

      * the front end horn [Click here for horn details](https://drive.google.com/file/d/1qdc5lhKErFyIsc8b52ZIkCPJLi-XykSb/view?usp=sharing)
      * the back end can and feedthrough antenna [Click here for CAN details]({{ site.baseurl }}/assemblingcan)
      * the front end and back end support stand [Click here for stand details](https://drive.google.com/file/d/1qdc5lhKErFyIsc8b52ZIkCPJLi-XykSb/view?usp=sharing)

   - a low noise amplifier (LNA)
   
       All of the following work fine for use with the horn telescope. The DSPIRA LNA is the most stable and long lasting.

      * Best option: the DSPIRA LNA – click on the [Detailed Information and Instructions Link]({{ site.baseurl }}/DetailedLNAInstructions)
      * Next best option: [Low Noise Amplifier Filtered Hydrogen Line 1420 MHz LNA *32 dB* Gain LNA with Bias Tee](https://gpio.com/products/hydrogen-line-lna-with-bias-tee) 
      * Next best option: [Nooelec SAWbird+ H1](https://www.nooelec.com/store/sdr/sdr-addons/sawbird-h1.html) - Premium SAW Filter & Cascaded Ultra-Low Noise Amplifier (LNA) Module for Hydrogen Line (21cm) Applications

   - an Airspy Software Defined Radio: [Airspy R2](https://airspy.com/airspy-r2) 

   - A [coaxial cable](https://www.coaxrf.com/shop/1-rf-coaxial-cables/times-microwave-lmr240/sma-male-times-microwave-lmr240/lmr240-sma-male-to-sma-male-coaxial-rf-pigtail-cable/) with SMA connectors is needed to connect the LNA to the SDR.

   - computer & software options:

      * computer with a Linux (Ubuntu) operating system

         + install GNU Radio 3.8

         + install the program *spectrometer_w_cal.grc* from the Github repository gr-radio_astro


      * computer with Windows operating system - the GNU Radio and spectrometer_w_cal.grc program can be run from a bootable flash drive

      * computer with Mac operating system - the GNU Radio and spectrometer_w_cal.grc program can be run from a bootable flash drive

