---
layout: post
date: 2020-07-25
title: Running the spectrometer_w_cal.grc Program
summary:  Instructions on how to use the spectrometer_w_cal.grc program in GNU Radio
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 5
meta_description: "Run the DSPIRA spectrometer in GNU Radio. Follow the startup steps, choose the receiver settings, and begin viewing radio telescope data."
---

The video shown [here](https://youtu.be/50B2Uv-SoDY) explains the features in this program.

## Before Starting The Program

The video [here](https://youtu.be/Oo28QCEZe_g) explains how set up the horn and make adjustments to the user-defined settings referred to below.

   * Check the user-defined settings illustrated below. These are the `Variable` blocks in the upper right corner of the GNU Radio canvas.

      ![User-defined blocks]({{ site.baseurl }}/images/UserDefinedBlocks.png)

      - Double-click the box, enter a new value in the Value box, and click OK.

      - `integration_time1` is the short integration time, and `integration_time2` is the long integration time. These can be changed to any value at 0.4 s or above.

      - Be sure that the file path in the `prefix` box is correct. This is the folder where the data files will be saved.

        Hints on setting the file path correctly:
        (These steps are explained in the [setting up the horn video](https://youtu.be/Oo28QCEZe_g).)
        1. Open the File Navigation window (folder icon).
        2. Navigate to the folder to which you want to save the spectrum files.
        3. Right click on the folder.
        4. Select `Properties`. 
        5. Double click the `Parent folder:` path and copy it to the clipboard.
        6. In the `prefix` variable box paste the path name inside quotes in the `Value` box. (Delete any existing path name.)
        7. Then append the actual folder name to the end of the parent path. Be sure to separate folder names with / and end with /.

            EXAMPLE:
            
            Parent folder: `home/Jansky/radio_astronomy`
            
            data folder name: `horn_data_2020`

            Value to put into the `prefix` variable box:   
	    "home/Jansky/radio_astronomy/horn_data_2020/"
	    (Include the quotes)

   * CAUTION: Plug your laptop into power. Otherwise, it may enter sleep mode and stop the program during a long run. Change the power settings on your computer so that it never suspends or goes to sleep.


## After Starting The Program

   * The first screen that appears looks like the following:

![Opening screen]({{ site.baseurl }}/images/filtered_nocal.png)

   * This display is used for most observations that are uncalibrated.

   * Adjust the `ymin` and `ymax` values to scale the graph as desired.

   * Fill in the `azimuth`, `elevation`, and `location`, if desired. 
   
      - **NOTE: Press ENTER after each value so the program records it.**

      - These parameters are included in the title, as described in the *Saving a Spectrum to a Data File* section below. This is also demonstrated in [this video.](https://youtu.be/dWX0rRU99Z8).

   * The `Short Integration` option is good for quick observations and demonstrations. Once the pointing is settled, switch to `Long Integration` for a longer run with smoother data.

   * The `Clipped Spectrum` is the better selection for most viewings. The `Full Spectrum` is good for demonstrating how the signal processing affects the spectrum. It also might be useful for the expert user who wants the full spectrum for some reason.

## Saving a Spectrum to a Data File

   * [Video](https://youtu.be/dWX0rRU99Z8) - describes how to save data

   * Click `Capture Current Spectrum` to save the displayed spectrum as a .csv data file. The data file is written to the folder under the path in the `prefix` Variable box.

   * Select `Writing to file` under `Write to csv File`. The program then creates a new file in the data folder after each integration period. For instance, if Long Integration is selected and is 10 s, then every 10 s a new file is written. So for a 20 minute run, a total of 120 files will be written to the data folder.

   Use this option for drift scans or unattended observations scheduled for later.

   * Data File Format:
      - The .csv format is a .txt data file that can be opened in any spreadsheet.

      - When opened in a spreadsheet, the data will appear in 2 columns. The first columns contains the frequency, in MHz, from 1414 MHz to 1424 MHz. The second column is the signal.

      - A graph of Signal vs. Frequency can easily be created after opening a file in a spreadsheet.

      - The file name has a format that contains the date, time, location, azimuth, and elevation, with “_spectrum” at the end. The location, azimuth, and elevation are recorded with the values in the corresponding fields on the spectrometer interface screen.

      - For example, `2020-07-15_Morgantown_200_30_spectrum.csv` identifies data collected in Morgantown on July 15, 2020. The telescope pointed at azimuth 200 degrees and elevation 30 degrees.
    
