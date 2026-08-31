---
layout: post
date: 2020-07-25
title: Running the spectrometer_w_cal.grc Program
summary:  Instructions on how to use the spectrometer_w_cal.grc program in GNU Radio
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order: 5
---

The video shown [here](https://youtu.be/50B2Uv-SoDY) explains the features in this program.

#### Before Starting The Program

The video [here](https://youtu.be/Oo28QCEZe_g) explains how set up the horn and make adjustments to the user-defined settings referred to below.

   * Check the user-defined settings illustrated below. These are the `Variable` blocks in the upper right corner of the GNU Radio canvas.

      ![User-defined blocks](/dspira-lessons/images/UserDefinedBlocks.png)

      - To change a value, double click on the box and then type the value in the Value box and hit OK.

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

   * CAUTION: If you run the program on a laptop without the power cord plugged in, the computer may go into a sleep mode and stop running the program, depending on the length of the run. Change the power settings on your computer so that it never suspends or goes to sleep.


### After Starting The Program

   * The first screen that appears looks like the following:

![Opening screen](/dspira-lessons/images/filtered_nocal.png)

   * This display is used for most observations that are uncalibrated.

   * Adjust the `ymin` and `ymax` values to scale the graph as desired.

   * Fill in the `azimuth`, `elevation`, and `location`, if desired. 
   
      - **NOTE: When entering these values, you must hit ENTER after each entry in order for it to get recorded by the program.**

      - These parameters are included in the title, as described in the *Saving a Spectrum to a Data File* section below. This is also demonstrated in [this video.](https://youtu.be/dWX0rRU99Z8).

   * The `Short Integration` option is good for quick observations and demonstrations. Switch to `Long Integration` for smoother data when a pointing is settled on and you are ready for a longer run.

   * The `Clipped Spectrum` is the better selection for most viewings. The `Full Spectrum` is good for demonstrating how the signal processing affects the spectrum. It also might be useful for the expert user who wants the full spectrum for some reason.

### Saving a Spectrum to a Data File

   * [Video](https://youtu.be/dWX0rRU99Z8) - describes how to save data

   * The spectrum that is currently being displayed on the screen can be written to a .csv data file by clicking the `Capture Current Spectrum` button. The data file is written to the folder under the path in the `prefix` Variable box.

   * When `Writing to file` is selected under the `Write to csv File` window, a data file will be written to a new file in the data folder each time an integration time elapses. For instance, if Long Integration is selected and is 10 s, then every 10 s a new file is written. So for a 20 minute run, a total of 120 files will be written to the data folder.

   This option is useful when running a drift scan or for when the user sets the telescope to collect data at a later time when the user is not able to be present.

   * Data File Format:
      - The .csv format is a .txt data file that can be opened in any spreadsheet.

      - When opened in a spreadsheet, the data will appear in 2 columns. The first columns contains the frequency, in MHz, from 1414 MHz to 1424 MHz. The second column is the signal.

      - A graph of Signal vs. Frequency can easily be created after opening a file in a spreadsheet.

      - The file name has a format that contains the date, time, location, azimuth, and elevation, with “_spectrum” at the end. The location, azimuth, and elevation are recorded with the values in the corresponding fields on the spectrometer inferface screen.

      - As an example, the filename `2020-07-15_Morgantown_200_30_spectrum.csv`  contains data that was collected on July 15, 2020 in Morgantown with the telescope pointed at an azimuth of 200 degrees and an elevation of 30 degrees.
    
