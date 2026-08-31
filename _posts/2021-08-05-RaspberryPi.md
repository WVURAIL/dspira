---
layout: post
date:  2021-07-01
title: Raspberry Pi
summary:  Details for setting up Raspberry Pi for Radio Astronomy
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 10
---

Raspberry Pi's are inexpensive and the more modern Pi's are powerful enough to keep up with the level of signal processing on GNU Radio associated with Radio Astronomy applications. 


  - [Supported Raspberry Pi Devices](#supported-raspberry-pi-devices)
  - [Installing Ubuntu image with radio astronomy preinstalled on a Raspberry Pi](#installing-ubuntu-image-with-radio-astronomy-preinstalled-on-a-raspberry-pi)
  - [Setting OS and installing software from scratch](#setting-os-and-installing-software-from-scratch)
    - [Operating system requirement](#operating-system-requirement)
    - [Installing Ubuntu on Raspberry Pi](#installing-ubuntu-on-raspberry-pi)
      - [Prerequisites](#prerequisites)
    - [Post OS Installation actions](#post-os-installation-actions)
      - [Interacting with the Raspberry Pi](#interacting-with-the-raspberry-pi)
      - [Installing gr-radio_astro](#installing-gr-radio_astro)


## Supported Raspberry Pi Devices

*All devices must have RAM greater than 4GB*
1. Raspberry Pi 4 Model B
2. Raspberry Pi 400


## Installing Ubuntu image with radio astronomy preinstalled on a Raspberry Pi
This image requires a minimum of 16GB of space on the SD card. 
1. Download the image [here](https://drive.google.com/file/d/1KzfgMEwgwTTZUaCeNR5kRgLj9MfMKyAh/view?usp=sharing)
2. Unzip the `.zip` file.
3. Use [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to install this image. 
   1. Insert SD card into your card reader on your computer
   2. Open Raspberry Pi imager.
   3. Click `Choose OS`, and choose `Use Custom`. 
   4. Select the correct image file downloaded in step 1 and 2 from your system.
   5. Click `Choose storage` and select your inserted SD card.
   6. Click write. 
   7. More info [here](https://www.raspberrypi.org/documentation/installation/installing-images/) and a [video](https://www.youtube.com/watch?v=ntaXWS8Lk34) 
4. Insert SD card to Raspberry Pi and power it up.
5. The default user name is `pi`, with password `raspberry`. Change the password after first boot. 


## Setting OS and installing software from scratch. 
## Operating system requirement

1. Ubuntu for Raspberry Pi [Click here for more Info](https://ubuntu.com/raspberry-pi)

_Note_: The custom `gr-radio_astro` [software]({{ site.baseurl }}/gr_radio_astro_Installation)  is now only supported for `GNURadio 3.8` only. The Raspberry Pi OS by default installs `GNURadio 3.7` which is not longer supported. 

## Installing Ubuntu on Raspberry Pi
### Prerequisites

1. Support Raspberry Pi
2. A microSD card (9GB minimum, 16GB recommended)
3. A computer with a microSD card drive
4. A micro USB-C power cable 
5. A monitor with an HDMI interface (Optionally for installing Ubuntu Server)
6. A micro HDMI cable (Optionally for installing Ubuntu Server)
7. A USB keyboard and mouse (Optionally for installing Ubuntu Server)

[Instructions from Ubuntu to install the OS on the Raspberry Pi 4](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview){:target="_blank"}

_NOTE_: Firstly, for Ubuntu desktop a monitor and mouse and keyboard is required. If you do not want to access the full desktop interface of ubuntu and only interact via command line interface you can install Ubuntu Server [instruction for Ubuntu server installation here](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview){:target="_blank"}. Secondly, Raspberry Pi is built on an ARM based architecture  any version of Ubuntu will not work. The OS has to specific to the Pi.

## Post OS Installation actions: 

### Interacting with the Raspberry Pi

1. Using a moniter and mouse and keyboard like any other desktop. 
2. Using SSH:
   1. This method can be used on any machine with ssh server enabled.
   2. Install X server on your computer. [VcXcrv](https://sourceforge.net/projects/vcxsrv/){:target="_blank"} on windows and [XQuartz](https://www.xquartz.org/){:target="_blank"} for macOS. 
   3. Power up the Raspberry Pi and connect your computer via ethernet cable
   4. First we need to determine the IP address of the raspberry PI: [How to determine Raspberry PI IP address](https://www.raspberrypi.org/documentation/remote-access/ip-address.md){:target="_blank"}
   5. If the determined IP address is `<IP address>` then in the terminal type `ssh -Y pi@<IP address>`
   6. More info on SSH [here](https://www.raspberrypi.org/documentation/remote-access/ssh/){:target="_blank"}
3. Using PuTTy on Windows: 
   1. [Download PuTTy](https://www.putty.org){:target="_blank"}.
   2. Add IP address in the hostname field.
4. Using VNC: More info [here](https://www.raspberrypi.org/documentation/remote-access/vnc/README.md){:target="_blank"} 
    
    

### Installing gr-radio_astro

[Installing gr-radio_astro]({{ site.baseurl }}/gr_radio_astro_Installation){: .button target="_blank"}

Notes: run `volk_profile` after installing everything to make sure GNU Radio is optimized to work on your device.

. 