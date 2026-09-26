---
permalink: /Telescope_Setup
layout: post
date:   2020-07-27
title: Setting up the Telescope 
summary:  Details on setting up the telescope for use
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 3
meta_description: "Prepare a DSPIRA horn telescope for observing. Follow the setup guide and video to connect the equipment and get ready to collect data."
equipment: "The equipment checklist, assembled horn, amplifier, receiver, cables, and computer with telescope software."
preparation: "Review the checklist and setup video. Confirm amplifier power and receiver connections before starting the spectrometer."
---


## Equipment checklist

- An assembled horn and feed can.
- A low-noise amplifier (LNA).
- A supported software-defined radio (SDR), such as an Airspy, RTL-SDR, LimeSDR, or PlutoSDR.
- A coaxial cable connecting the LNA to the SDR.
- A USB cable connecting the SDR to the computer.
- A computer with GNU Radio and the DSPIRA telescope software installed.

Check the [receiver settings]({{ '/Spectrometer_sourceblock_settings' | relative_url }}) for your SDR and amplifier power arrangement.

## Setup demonstration

This video covers telescope setup and initial spectrometer settings.
Older videos call the program `spectrometer_w_cal.grc`; the current application is `calibrated-spectrometer.grc`.

<figure class="lesson-video" id="video-Oo28QCEZe_g">
{% include youtube.html title="Horn Operation: Setting Up a Horn" url="https://youtu.be/Oo28QCEZe_g" video="Oo28QCEZe_g" %}
</figure>