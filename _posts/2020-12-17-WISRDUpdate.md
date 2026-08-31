---
layout: post
date:   2020-12-17
title: Cosmic rays and radio, at the WISRD lab
summary:  A student group running the horn telescopes alongside a cosmic ray detector, looking for radio from air showers
tags: ['School-Teachers', 'Students', 'Hobbyists']
categories: ['Community Labs']
order: 1
---

The Wildwood Institute for STEM Research and Development is a student research
lab in Los Angeles. Its radio astronomy group built this hardware and then went
somewhere the DSPIRA curriculum does not: they run the telescopes next to a
[Quarknet](https://quarknet.org/) cosmic ray detector, looking for radio bursts
that arrive at the same moment as an air shower.

The physics they are chasing is that a high-energy particle cascade through the
atmosphere is thought to radiate — Cherenkov and bremsstrahlung — so a cosmic
ray shower and a radio transient should sometimes be the same event seen two
ways. Detecting the coincidence is the hard part, and it is a genuinely open
question rather than a classroom exercise with a known answer.

## What they have published

**[Preparations for the Detection of Radio Waves Created by High-Energy Cosmic
Rays using the WISRD Cosmic Ray Detector](https://drive.google.com/file/d/1IJ3-HkYX14fHSujKklYOS62CL6nTMqmP/view)**
— L. Perttula, R. Cortez, S. Zohar, J. Reis and J. A. Wise. The opening paper
of the *WISRD Research &amp; Engineering Journal*, Volume 4 Issue 1, Spring 2022,
pages 2 to 12. It covers the Quarknet detector — four scintillators on
photomultiplier tubes, with a FermiLab data acquisition board — how they
calibrated it, and how they are pairing it with the radio telescopes.

**[Cosmic ray detector calibration, spring 2023](https://drive.google.com/file/d/1blapCsGn7M0rHwacW5Ehk3zLXRY6rN84/view)**
— a progress poster. They are replacing a voltage box and stepper motors with a
Raspberry Pi driving digital potentiometers so the detectors can be calibrated
remotely, and they report an unexplained oscillation in the rate of anomalous
events they are still chasing down.

## If you want to try this

Coincidence detection is what the `radio_astro` event blocks were written for —
`detect`, `dedispersion`, `correlate` and the triggered CSV sink are in
[gr-radio_astro](https://github.com/WVURAIL/gr-radio_astro), and the
[LightWork memo series](/lightwork/) covers the event-capture
side in memos 023 and 027.

The group's own site is at [wisrd.org](https://www.wisrd.org/).
