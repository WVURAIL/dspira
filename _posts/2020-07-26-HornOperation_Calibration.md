---
layout: post
date:   2020-07-26
title: How to Calibrate the Horn Telescope
summary:  The procedure for calibrating the telescope using the spectrometer_w_cal program is outlined.
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 6
meta_description: "Calibrate a horn radio telescope with the DSPIRA spectrometer. Follow the setup steps to prepare the system for measuring hydrogen signals."
timing: "Allow about 20 minutes for warm-up before calibrating. Wait for the display to settle during each measurement."
keywords: ["calibration", "calibrate", "hot cold"]
---

[Instructional video](https://youtu.be/r8iYuaiFOd8) - Demonstrates steps for calibrating the horn telescope.

[<img alt="Watch the horn telescope calibration instructional video on YouTube" src="{{ '/images/CHIME_dishes.jpg' | relative_url }}" width="400" height="300" />](https://youtu.be/r8iYuaiFOd8)

## Some preliminary pointers: 

   * For the best results, after starting the program, allow the system to warm up for approximately 20 minutes before calibrating.

   * Re-calibrations can be done any time during a viewing session. 

   * For consistency, it is recommended to re-calibrate occasionally during a viewing session.

## Procedure 

   1. Point the telescope toward the ground. The video above shows how this is done.

   2. Switch the `Spectrum Display` to `Hot Calibration`.

   3. Select the `Time Integration` to `Long Integration`.

   4. Watch the spectrum displayed. You may need to change the `ymax` value so that all of the signal is visible on the graph. Wait for the graph to settle to a steady display. Then switch the `Spectrum Display` to `Cold Calibration`. DO NOT MOVE THE TELESCOPE UNTIL THE SPECTRUM DISPLAYED HAS BEEN CHANGED TO `Cold calibration`.

   5. Switch the display to `Cold Calibration` and the integration to `Short Integration`.

   6. Point the telescope at open sky. Keep redirecting it until you find sky without a hydrogen peak near 1420.4 MHz. After doing so, switch to `Long Integration`.

   7. Wait for the graph to settle to a steady display. Then switch the `Spectrum Display` to `Spectrum with Calibration`.  DO NOT MOVE THE TELESCOPE UNTIL THE SPECTRUM DISPLAYED HAS BEEN CHANGED TO `Spectrum with calibration`.

   8. The spectrometer is now calibrated, and the graph should now be showing only signals from the galaxy.

## Some More Things to Note: 

   * After completing a calibration, the signal is in units of Kelvin (K). This sounds odd, but it is how radio astronomers quantify radio signals. (For most amateur applications, it is not necessary to get bogged down trying to understand why the units are Kelvin.)

   * After calibration, the baseline would ideally remain steady near 10 K. This approximates the cold sky's temperature. However, in reality, the base level after calibration will drift up and down. Several factors cause this drift. The main contributor is the LNA, whose temperature changes during an observing session.

   * The background level can actually go negative! No need to worry. Re-calibrating usually takes care of this and brings the base level back up to approximately 20 K. Also, the `y-min` value can be adjusted to negative values.
 
   * The value of the background level will not affect any peak positions or shapes.

   * The calibrated spectrum remains useful for quantitative analysis despite baseline changes. Offset the data to bring the background level to zero. This is typically what is done when analyzing the area of the peaks.
    
