---
permalink: /HornOperation_Calibration
layout: post
date:   2020-07-26
title: How to Calibrate the Horn Telescope
summary:  The procedure for calibrating the telescope using the calibrated spectrometer is outlined.
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 6
meta_description: "Calibrate a horn radio telescope with the DSPIRA spectrometer. Follow the setup steps to prepare the system for measuring hydrogen signals."
timing: "Allow about 20 minutes for warm-up before calibrating. Wait for the display to settle during each measurement."
keywords: ["calibration", "calibrate", "hot cold"]
equipment: "A working horn telescope and running spectrometer. The horn must be movable between ground and open sky."
preparation: "Complete telescope setup and read the spectrometer controls. Warm up the system before collecting hot and cold references."
---

[Instructional video](https://youtu.be/r8iYuaiFOd8) - Demonstrates steps for calibrating the horn telescope.

[<img alt="Watch the horn telescope calibration instructional video on YouTube" src="{{ '/images/observing/calibration-video-thumbnail.jpg' | relative_url }}" width="400" height="300" />](https://youtu.be/r8iYuaiFOd8)

Use the written procedure below as the current reference beside the video.
Software checks confirm the reference-saving behavior described here. The full procedure still needs a recorded hardware check.

## Some preliminary pointers: 

   * For the best results, after starting the program, allow the system to warm up for approximately 20 minutes before calibrating.

   * Re-calibrations can be done any time during a viewing session. 

   * For consistency, it is recommended to re-calibrate occasionally during a viewing session.

## Procedure 

   1. Point the telescope toward the ground. The video above shows how this is done.

   2. Switch the `Spectrum Display` to `Hot Calibration`.

   3. Select the `Time Integration` to `Long Integration`.

   4. Adjust `ymax` if needed to see the spectrum. Wait for the display to settle.

   5. Switch to `Cold Calibration` before moving the telescope. This preserves the hot reference. Then select `Short Integration`.

   6. Point the telescope at open sky. Keep redirecting it until you find sky without a hydrogen peak near 1420.4 MHz. After doing so, switch to `Long Integration`.

   7. Wait for the display to settle. Switch to `Spectrum with Calibration` before moving the telescope. This preserves the cold reference.

   8. The display now applies both references. Inspect the baseline and hydrogen line before collecting observations.

`Hot Calibration` and `Cold Calibration` continuously replace their respective references while selected.
`Spectrum with Calibration` uses those saved references without replacing them.

## Some More Things to Note: 

   * After completing a calibration, the signal is in units of Kelvin (K). This sounds odd, but it is how radio astronomers quantify radio signals. (For most amateur applications, it is not necessary to get bogged down trying to understand why the units are Kelvin.)

   * After calibration, the baseline would ideally remain steady near 10 K. This approximates the cold sky's temperature. However, in reality, the base level after calibration will drift up and down. Several factors cause this drift. The main contributor is the LNA, whose temperature changes during an observing session.

   * A negative or drifting baseline is a reason to check the setup and repeat calibration.
     The model assumes a 10 K cold reference, not a 20 K target.
     Adjusting `y-min` changes the display scale; it does not correct calibration.
 
   * A constant background offset does not shift peak positions. Frequency-dependent drift or interference can change the spectrum's shape.

   * Review baseline stability before quantitative analysis. Subtracting a constant offset cannot repair every calibration error.
    
