---
layout: catpag
category: Receiver Electronics
lead: "Everything between the antenna and the laptop: the amplifier, the SDR, and the settings that match them."
---

A horn on a stand is an antenna, not yet a telescope. What makes it one is the
receiver chain: a **low-noise amplifier** on the probe inside the can, which
lifts a signal far too faint to digitise up to something an SDR can see, and a
**software-defined radio** that samples the amplified signal and hands it to a
computer over USB.

The amplifier is the component that decides how good your telescope is, and it
is the one most worth spending time on. There are three routes to one: build the
DSPIRA board from parts for around $30, or buy one of two ready-made modules.

The SDR matters less. Several will work, but each has its own sample rate and
gain, and the spectrometer has to be told which one you have. That is what the
source-block settings lesson is for.

Read this module alongside
[Software Setup]({{ '/categories/software-setup/' | relative_url }}), which
covers the programs the SDR feeds.
