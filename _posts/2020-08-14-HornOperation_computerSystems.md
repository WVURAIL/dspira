---
layout: post
date:   2020-08-14
title: Computer and Software Needs for the Horn Telescope Spectrometer
summary:  Details on computer systems that can be used to operate the horn spectrometer
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 1
meta_description: "Choose a computer and software for the DSPIRA horn spectrometer. Find setup guidance for laptops, desktop computers, and Raspberry Pi."
equipment: "A computer for comparing installation routes. USB and Raspberry Pi routes require the additional storage and hardware described below."
preparation: "Choose one route for your computer and receiver. Check the current software guide before using historical installation instructions."
---

Choose a computer and installation route that match your receiver.
The telescope also needs a horn, amplifier, and suitable cables.
See the [complete system overview]({{ site.baseurl }}/BuildingHornTelescope_Overview) before choosing parts.

Read the [software compatibility guide]({{ '/software/' | relative_url }}) before installing or scheduling observations.
Generation checks do not establish that a receiver or complete telescope works.

## Bootable USB drive

The [bootable USB guide]({{ site.baseurl }}/Install_Ubuntu_spectrometer_onFlashdrive) provides images containing Ubuntu and telescope software.
The Ubuntu 22.04 image requires a 32 GB drive; the Ubuntu 24.04 image requires a 128 GB drive.
Check that your computer can boot the selected image from USB before relying on this route.
Back up the USB drive before writing the image.

These images may contain older application files. Check receiver settings and recording paths before observing.

## Install on an Ubuntu computer

Follow the [software installation steps]({{ site.baseurl }}/BuildingHorn_SoftwareInfo) to install GNU Radio and the shared radio astronomy blocks.
Download the classroom applications separately through the [software guide]({{ '/software/' | relative_url }}).
Check the Ubuntu and GNU Radio versions expected by each instruction page.

Installing or repartitioning an operating system requires preparation and permission on school computers.
Back up existing data before changing a drive's layout.

## Raspberry Pi

The [Raspberry Pi guide]({{ site.baseurl }}/RaspberryPi) describes an alternative computer setup.
It includes older images and installation instructions whose compatibility needs checking.
Choose this route only after reviewing the device, storage, and software requirements.
