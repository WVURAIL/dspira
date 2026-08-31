---
layout: post
date:   2020-07-24
title: Horn Telescope Spectrometer Description
summary:  Description of the spectrometer_w_cal.grc program features
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 4
---

The program used to run the telescope is a GNU Radio program called *spectrometer_w_cal.grc*. It is available from the WVURAIL/gr-radio_astro repository in Github. The *spectrometer_w_cal.grc* program has several features to make data collection with the horn telescope user-friendly. Each feature on the display is described below.

Set up the horn and connect the LNA to the Airspy with a cable, and the Airspy to the computer USB.  Then open the spectrometer_w_cal.grc program in GNU Radio. 
[This video shows how to set up a horn and start the program.](https://youtu.be/Oo28QCEZe_g) 

You can also watch [this video](https://youtu.be/50B2Uv-SoDY), which describes these user interface features in detail.

### **1.	Features of the *Spectrum* Tab**

![spectrometer screen](/dspira-lessons/images/filtered_nocal.png)

   * **Graphical Display** Boxes:

        - **Spectrum** graph – shows the signal vs. frequency spectrum, which is the primary focus of our investigations with a radio telescope.

        - **System Heartbeat** – This is actually a histogram of signals being detected. During normal, this display should continuously jump up and down during a run. As long as its “beating,” things are good. If this graph looks frozen, then the program has probably stopped running, and you will need to restart the program.



   * **Spectrum Display** options:

        - **_filtered spectrum with no calibration_** - the raw spectrum collected is displayed with the noise spikes filtered out.

        - **_spectrum with calibration_** - the hot and cold calibrations are factored in to display the true signal received from the galaxy.

        - **_hot calibration_** - Select when pointing the telescope at the “hot” source (the ground) during the calibration procedure.

        - **_cold calibration_** - Select when pointing the telescope at the “hot” source (the ground) during the calibration procedure.

        - **_unfiltered spectrum with no calibration_** - the raw spectrum collected is displayed with no changes made to it.

   * **Integration Time** options:

        - Because the radio signals being detected are extremely weak, it is necessary for the software to add together (integrate) the signals detected over a period of time. This is the integration time. This averages out the noise in the signal, making the galaxy signal more prominent. The user has the option of setting two different integration times when using this spectrometer. 

        - The user can change these settings in the integration variable blocks before starting the program.

        - **Short Integration**
           + This is useful for quick sampling of what the telescope is looking at.

           + The default setting for the shorter integration time is 0.4 s. 

        - **Long Integration**
           + This is useful for when smoother data is desired. Usually the user will use the longer setting for targeted pointings where “good” data is needed.
           
           + The default setting for the longer integration time is 10 s. 

   * **Integration Reset** – This resets the data averaging when the long integration time is selected. This is needed if the telescope pointing is changed in the middle of a long integration to assure the spectrum displayed is the average of the new pointing.

   * **Full or Clipped Spectrum**

       - **Clipped spectrum** – In this display the ends of the spectrum, between 1414 and 1415 MHz and between 1423 and 1424 MHz, are clipped off. This removes the distracting background portions of the spectrum, as discussed in the *The System Background Signal* in the [What Can a Horn Telescope Measure?]({{ site.baseurl }}/HornOperation_Intro) post.


      - **Full spectrum** – This is self explanatory.

   * **Capture Current Spectrum** button

       - The live spectrum being displayed on the main graph can be captured in a .csv text file for easy access later.

   * **Write to .csv File**

       - This option enables the spectrum to be written to newly created files once every integration time so that data can be collected without the user’s presence.

       - See the video [Saving Data Using the *spectrometer_w_cal.grc* Program](https://youtu.be/dWX0rRU99Z8).


### **2.	Features of the *System Temp/Gain* Tab**

   ![System Temp/Gain screen](/dspira-lessons/images/sys_T&G.png)

   * These graphs are not needed during most telescope runs. They are mainly for those who are interested in the quantitative performance of the telescope.

   * **System Temperature Spectrum** – This graph is an indication of the amount of signal that is coming from the telescope system itself. 

   * **Gain** – This is the factor that is used by the spectrometer to scale the detected signal into known astronomical units.
