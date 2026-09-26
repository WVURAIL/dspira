---
permalink: /PlutoSDR_installation
layout: post
date:   2021-08-04
title: PlutoSDR software Installation 
summary:  Steps for installing the PlutoSDR software on your computer
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Receiver Electronics']
order: 4
meta_description: "Install the software needed to use PlutoSDR with a DSPIRA telescope. Follow the setup steps to connect the receiver to your computer."
optional: true
equipment: "An ADALM-PLUTO receiver and a computer with GNU Radio, internet access, and software installation permissions."
preparation: "Use this optional route only for PlutoSDR. Use GNU Radio 3.10 with its included IIO blocks. Check the USB connection before configuring telescope reception."
---

GNU Radio 3.10 includes the IIO blocks used by PlutoSDR.
Follow the [DSPIRA installation guide]({{ '/install-software/' | relative_url }}) first.
The [Analog Devices guide](https://wiki.analog.com/resources/tools-software/linux-software/gnuradio) explains version compatibility.

## Check the installed blocks

On Ubuntu, install the device inspection utility:

```sh
sudo apt install libiio-utils
python3 -c "from gnuradio import iio; print(iio.__file__)"
```

Restart GNU Radio Companion and search for **PlutoSDR Source**.
Use the block from the installed GNU Radio IIO package.
The older `upgrade-3.8` source-build instructions apply to GNU Radio 3.8, not the current DSPIRA setup.

## Connect the receiver

Connect the PlutoSDR to the computer with a USB data cable.
List available IIO contexts:

```sh
iio_info -s
```

Copy the detected receiver's URI into the source block's **IIO context URI** field.
If no receiver appears, follow Analog Devices' USB and device-access troubleshooting guidance.

## Configure the telescope

Follow the [receiver settings]({{ '/Spectrometer_sourceblock_settings' | relative_url }}) for tuning, sample rate, connections, and amplifier power.
Set **LO Frequency** to `int(freq)` and **Sample Rate** to `int(samp_rate)`.
Use `freq = 1421e6` and `samp_rate = 3.5e6` for this lesson.
Confirm reception and calibration with your equipment before collecting observations.
