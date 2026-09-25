---
layout: catpag
category: Software Setup
lead: Ubuntu, GNU Radio and the DSPIRA blocks, on a laptop, a flash drive or a Raspberry Pi.
meta_description: "Set up a computer for DSPIRA radio astronomy. Install Ubuntu, GNU Radio, receiver drivers, and telescope software using the lesson sequence."
---

**Overview Software Needed For the Horn Telescope** 

* The horn telescope uses software defined radio (SDR) for collecting and processing the radio signals collected.

* An SDR device (dongle) is needed for this system. See the [SDR Options page.]({{ site.baseurl }}/SDR)

* A computer receives the SDR data. A *spectrometer* program processes it at the telescope's back end.

* The spectrometer program called *spectrometer_w_cal.grc* runs on the free, open-source software *GNU Radio* on the *Ubuntu* operating system. The *Installation of Ubuntu and SDR software on a Windows-based computer* instructions cover the required software. They explain obtaining *Ubuntu*, *GNU Radio*, and *spectrometer_w_cal.grc*.

* Instructions on how to use the *spectrometer_w_cal.grc* program can be found [here]({{ site.baseurl }}/spectrometer_w_cal_Instructions){:target="_blank"}. 

* Another option is to build a simple spectrometer program in *GNU Radio*. Instructions for doing this are provided below under *Build a Simple Spectrometer in GNU Radio*. These instructions teach *GNU Radio*, then introduce digital signal processing (DSP). The DSP lessons explain processes used in the spectrometer. Then steps on how to build a simple spectrometer in *GNU Radio* are provided.  

**Warning-Novice Computer Users - Does *UBUNTU* or *Command Line Interface* sound new to you?**
You may wish to read the following intro to the UBUNTU environment. [**What is UBUNTU?**](https://docs.google.com/document/d/14U9ANGS9YM3PnQY-n2ykO4uKVwVDf8NeHfauRmGDmw0/edit?usp=sharing) before you start downloading and setting up software.

**Acquire Necessary Software:**

* [**Installation on a Bootable Flashdrive**]({{ site.baseurl }}/Install_Ubuntu_spectrometer_onFlashdrive). This is DSPIRA's preferred way to obtain the software needed for the horn telescope.  A 32G flash drive lets users run the software on Windows-based computers without dedicating a PC to it. The bootable flash drive holds all required software: Ubuntu, *GNU Radio*, and *spectrometer_w_cal.grc*.

* [**Installation of Ubuntu and SDR software on a Windows-based computer**]({{ site.baseurl }}/BuildingHorn_SoftwareInfo). Covers installing Ubuntu, *GNU Radio*, and *spectrometer_w_cal.grc*.  APPLE COMPUTERS: DSPIRA has not successfully run GNU Radio on Apple computers. We therefore provide no Apple support material here. 

**Build a Simple Spectrometer in *GNU Radio*:**

* [**Simple Spectrometer**]({{ site.baseurl }}/Simple_Spectrometer). Introduces *GNU Radio*, basic DSP lessons, and steps for building a spectrometer in *GNU Radio*.
