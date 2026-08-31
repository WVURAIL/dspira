---
layout: post
date:   2020-08-14
title: Computer and Software Needs for the Horn Telescope Spectrometer
summary:  Details on computer systems that can be used to operate the horn spectrometer
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 1
---

- Installation of any of the following software options will allow the user to run the spectrometer program to operate a horn telescope that is equipped with an LNA, software defined radio (Airspy or equivalent), and the proper cables. See the document [What is Needed to Build a Horn Telescope]({{ site.baseurl }}/BuildingHornTelescope_Overview) and links therein for more details about the telescope system.

- Different options for operating the horn telescope spectrometer program, *spectrometer_w_cal.grc*, are presented here. The options provided vary depending on the user's computer system and his or her comfort level working with computers.

The options presented below include a brief description of the system requirements and what is involved in the installation process.

1. [Download a fully operating image onto a flash drive that can be operated from most computer systems.]({{ site.baseurl }}/Install_Ubuntu_spectrometer_onFlashdrive)

    - Easiest for those who are the less experienced in working with computer system software.

    - Requires a computer and a 32 GB, 3.0 USB flash drive. 

    - Once the flash drive image is created, the spectrometer program can be run on the following systems:

        - pc with Windows: minimum system specs?, brand names?

        - MAC with OS ?? or higher

        - Linux system, such as one running Ubuntu 20.04.

        - The software needed is to complete the installation is free and easy to install.

    - Click [here]({{ site.baseurl }}/Install_Ubuntu_spectrometer_onFlashdrive) for installation instructions.
    
2. [Install the free & open-source software, *GNU Radio*, on a Linux system operating Ubuntu 20.04.]({{ site.baseurl }}/BuildingHorn_SoftwareInfo)

    - This option is for those who are more experienced with computers and feel comfortable installing software on a hard drive.

    - Requires a computer that either already runs on the Ubuntu operating system, or has a hard drive running Windows that can be partitioned.

    - It may require partitioning a hard drive in Windows and installing Ubuntu 20.04 on it, if the system is not already running Ubuntu.

    - Once Ubuntu is installed, further installations include installing the free & open-source software *GNU Radio*, and then installing the spectrometer program from Github.

    - After installation, the computer will be able to run the telescope system directly.

    - Click [here]({{ site.baseurl }}/BuildingHorn_SoftwareInfo) for installation instructions.

3. Install the spectrometer program on a Raspberry Pi.

    - This can be done, but the details have not been fully worked out by us (the DSPIRA group). 

    - Details to follow.
