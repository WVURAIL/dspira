---
permalink: /gr_radio_astro_Installation_Ubuntu20
layout: post
date: 2023-06-27
title: Historical GNU Radio 3.8 Setup on Ubuntu 20.04
summary: Recover the older combined package for an existing GNU Radio 3.8 environment.
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 8
meta_description: "Recover a historical DSPIRA setup on Ubuntu 20.04 with GNU Radio 3.8. Use the preserved gr38 release for an existing telescope environment."
optional: true
equipment: "An Ubuntu 20.04 computer with GNU Radio 3.8 and the listed build dependencies."
preparation: "Use this optional historical route only for the matching environment. Otherwise, follow the current DSPIRA installation guide."
---

This historical guide uses the frozen `gr38` tag. It preserves the older combined package and its application paths.
For current software, use the [DSPIRA software guide]({{ '/software/' | relative_url }}).


This installs *spectrometer_w_cal.grc* and other GNU Radio astronomy programs on Ubuntu 20.04.

Complete the following steps:

   1. Open a terminal window in Ubuntu.

   2. Install GNU Radio external python dependencies and SDR drivers by typing the following and hit enter:
   ```
      sudo apt install gnuradio gr-osmosdr airspy python3-h5py python3-ephem git cmake liborc-0.4-dev -y
   ```
   3. To clone the repository: in the terminal, type and Enter: `git clone --branch gr38 https://github.com/WVURAIL/radio-research-software.git gr-radio_astro`

   4. Switch to the gr-radio_astro directory: `cd gr-radio_astro`

   5. Confirm the historical release by typing: `git describe --tags --exact-match`

   6. Make a build directory: `mkdir build`, and then move to it: `cd build`  
      
   7. Then run the following in the build directory:

      ```
      cmake ..
      sudo make
      sudo make install
      ```
**Additional Steps for setting the proper Python environment:**

   8. Open a terminal window.
   
   9. Make sure you are at the home directory (type and Enter `cd` ). Then type `gedit .bashrc` to open the *.bashrc* file in an editor.
   
   10. Scroll to the file's bottom and add a blank line. Paste this code: `export PYTHONPATH=/usr/local/lib/python3/dist-packages:/usr/local/lib/python3.8/dist-packages:$PYTHONPATH`

   11. Save and close (x in upper right corner).
   
   12. Additionally you can create appropriate symbolic links
       1.  Open `gnuradio-companion` in a terminal, then click `Help --> About`. Note the Python version in the dialog.  
       2.  For Python 3.8, type `cd /usr/local/lib/python3.8/dist-packages`. For Python 3.9, use `cd /usr/local/lib/python3.9/dist-packages`. 
       3.  Type `ln -s /usr/local/lib/python3/dist-packages/radio_astro`   
 
**Check that the Installation was Successful**

   1.  *Restart your terminal window*. Run the program in GNU Radio:
         - In a terminal window type `gnuradio-companion`
         - Open the *spectrometer_w_cal.grc* program as follows: 
            
           `File --> Open --> gr-radio_astro --> examples --> DSPIRA --> spectrometer_w_cal.grc `
         - Plug an Airspy radio, with the LNA attached, into the USB port. Run the program by hitting the start triangle ("execute the flowgraph") on the menu bar at top. If no errors occur, you are all set!  
   
## Updating an older installation

The `gr38` tag is a frozen release, not an update branch.
Keep existing receiver settings and customized flowgraphs before changing environments.
For current development, use the [DSPIRA installation guide]({{ '/install-software/' | relative_url }}) with GNU Radio 3.10.
Do not use `git pull` to update this historical tag.
