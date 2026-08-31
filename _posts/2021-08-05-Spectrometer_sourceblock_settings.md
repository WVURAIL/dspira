---
layout: post
date:   2020-07-27
title: Spectrometer Source Block Settings 
summary:  Settings in spectrometer for different SDR's
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Receiver Electronics']
order: 5
---


The default source block settings in the `spectrometer_w_cal.grc` GNU Radio program are for the [Airspy R2](https://airspy.com/airspy-r2) SDR. If a different SDR is used, changes in the source block, the `samp_rate Variable` block, and sometimes the `freq Variable` block may be needed. The settings for some common SDR's used with the horn telescopes are described below.

> **Why `freq` sometimes has to change too.** The program records a band
> `samp_rate` wide, centred on `freq`. The default is `freq` 1419 MHz with
> `samp_rate` 10e6, which records 1414 – 1424 MHz — the hydrogen line at
> 1420.4058 MHz sits comfortably inside. Narrow the sample rate without moving
> the centre and the band shrinks around 1419 MHz, and at some point the line
> falls off the end of it. Halve the sample rate to 2.4e6 and the band becomes
> 1417.8 – 1420.2 MHz: **the line is 0.2 MHz outside it and the telescope
> records no hydrogen at all.** That is why the RTL-SDR and Pluto settings
> below change `freq` as well, and the Airspy Mini and Lime do not.
>
> A quick check: your band runs from `freq - samp_rate/2` to
> `freq + samp_rate/2`, and 1420.4058 MHz needs to be inside it with room to
> spare at both ends.

Options:

+ The [Airspy Mini](https://airspy.com/airspy-r2)

    - Source block: the `osmocom Source` block is used; the "Device Arguments" are the same as for the Airspy R2. So no changes are needed in this block.

    - `samp_rate Variable` block: This block is in the upper left corner of the canvas in the `spectrometer_w_cal.grc` program next to the `Options` block. Open this block by double-clicking it. Change the "Value" to "6e6" (which is 6 MHz).

    <img alt="samp_rate Variable block properties: Id samp_rate, Value 6e6" align="center" width="300" height="146" src="/dspira-lessons/images/AirspyMini_samp_rate.png">

    - `freq Variable` block: leave it at 1419e6. The band becomes 1416 – 1422 MHz, which still holds the line.

+ RTL-SDR

    **Two changes are needed, not one.** The `samp_rate` change alone moves the
    hydrogen line out of the recorded band — see the box above. Make both.

    - Source block: Change the "Device Argument" to: rtl=0, bias=1, pack=0, as shown:

    <img alt="osmocom Source properties: Device Arguments rtl=0,bias=1, Sample Rate samp_rate, Frequency freq, RF/IF/BB gains 17, 12, 10 dB" align="center" width="300" height="385" src="/dspira-lessons/images/RTL_SDR_source.png">

    - `samp_rate Variable` block: This block is in the upper left corner of the canvas in the `spectrometer_w_cal.grc` program next to the `Options` block. Open this block by double-clicking it. Change the "Value" to "2.4e6" (which is 2.4 MHz).

    <img alt="samp_rate Variable block properties: Id samp_rate, Value 2.4e6" align="center" width="300" height="149" src="/dspira-lessons/images/RTL_SDR_samp_rate.png">

    - `freq Variable` block: next to `samp_rate`. Change the "Value" to
      **"1420.5e6"**. The band then runs 1419.3 – 1421.7 MHz, with the line at
      1420.4058 MHz inside it.

    - Two things to know about an RTL-SDR at this sample rate, neither of them
      a fault you can fix in the flowgraph:

        - The band is only ±230 km/s wide, so the faint wings of the line are
          clipped and there is no stretch of it guaranteed free of Galactic
          hydrogen to fit a baseline on. Maps are good for seeing where the
          Milky Way is; treat the intensity numbers as indicative.
        - Every SDR of this type puts a spurious tone at the exact centre of
          its band, which at this tuning is 0.1 MHz from the line.
          `map_h1_hdf5_drift.py` blanks a 120 kHz strip there, and because the
          strip is next to the line that costs roughly a quarter of the
          measured intensity. The comment on `DC_MASK_HALFWIDTH_HZ` in that
          script has the measured figures and the two ways to improve it.

+ Lime 

    - Source block: the Lime uses the `LimeSDR Source (RX)` block. Click on the `osmocom` block and hit Delete. Then in the search window on the tool bar at the top, type "LimeSDR". Grab the `LimeSDR Source (RX)` and drag it onto the canvas where the `osmocom` block was. Then one-by-one connect the blue output of the `LimeSDR Source (RX)` block to the `Stream to Vector` block, the three `Delay` blocks, and the `Complex to Real`. The final connections should look like the following:

    <img alt="LimeSDR Source (RX) output connected to Stream to Vector, three Delay blocks (4.096k, 8.192k, 12.288k), and Complex To Real" align="center" width="239" height="164" src="/dspira-lessons/images/Lime_connections.png">
 
    - Open the `LimeSDR Source (RX)` block (by double-clicking) and set the following:
        - On the "General" tab, set "RF frequency" to "freq" [without the quotes], and check that the "Sample rate" is "samp_rate" [without the quotes]. "Channel" should be on "A" [without the quotes].

        <img alt="LimeSDR Source General tab: Channel A, RF frequency freq, Sample rate samp_rate, Oversample Default, MIMO phase align Disabled" align="center" width="297" height="265" src="/dspira-lessons/images/Lime_General.png">


        - The settings on the Channel A tab should be as shown:

        <img alt="LimeSDR Channel A tab: NCO frequency 0, Calibration bandwidth samp_rate, LNA path W, Analog filter bandwidth 16e6, Digital filter bandwidth 0, Gain 45 dB" src="/dspira-lessons/images/Lime_channelA.png" align="center" width="500px"/>
        
    - `samp_rate Variable` block: The Lime SDR can use a 10 MHz samp_rate; so no change is needed in this block. Leave `freq` at 1419e6 as well — the band stays 1414 – 1424 MHz, the same as the Airspy R2.

    - Install gr-limesdr - software needed for the Lime SDR block to run in GNU Radio.

        - Open a terminal window.

        - Type and enter: `sudo apt install gr-limesdr`

    - POWER TO THE LNA: The Lime SDR does not power the LNA. Therefore, it is necessary to provide +5 V dc external power to the LNA through a [bias-T](https://www.minicircuits.com/WebStore/dashboard.html?model=ZFBT-282-1.5A%2B), which is connected to the LNA and Lime as shown:
        
        <img alt="Mini-Circuits ZFBT-282-1.5A+ bias-tee: one SMA port to the Lime SDR, the other through a female-female SMA adapter to the LNA, DC lead to +5 V power" align="center" width="329" height="199" src="/dspira-lessons/images/Bias_T_connections.png">

        An [SMA female to female connector/adapter](https://www.data-alliance.net/sma-female-to-sma-female-adapter-coupler-gender-changer/) will be needed for the connection from the bias-T to the LNA cable, as indicated in the diagram above.

+ ADALM-PLUTO 

    - The Adalm-Pluto SDR uses the `PlutoSDRSource` block that will need to be installed. Complete the [steps outlined here]({{ site.baseurl }}/PlutoSDR_installation) to install this block on your computer.

    - Source block: the Adalm-Pluto uses the `PlutoSDRSource` block. Click on the `osmocom` block and hit Delete. Then in the search window on the tool bar at the top, type "PlutoSDR". Grab the `PlutoSDRSource` and drag it onto the canvas where the `osmocom` block was. Then one-by-one connect the blue output of the `PlutoSDRSource` block to the `Stream to Vector` block, the three `Delay` blocks, and the `Complex to Real`. The final connections should look like the following:

    <img alt="PlutoSDR Source output connected to Stream to Vector, three Delay blocks (4.096k, 8.192k, 12.288k), and Complex To Real" align="center" width="277" height="237" src="/dspira-lessons/images/PlutoSDR_sourceBlock_connections.png">

    - Open the `PlutoSDRSource` block (by double-clicking) and set the following:
        - On the "General" tab, set the values as shown:

        <img alt="PlutoSDR Source properties: LO Frequency 2400000000, Sample Rate int(samp_rate), RF Bandwidth 20000000, Buffer size 32768, Manual Gain (RX1) 64 dB" align="center" width="300" height="267" src="/dspira-lessons/images/PlutoSDR_Source.png">

    - The `samp_rate` and `freq` Variable blocks should be set to the values shown — `samp_rate` 3.5e6 **and** `freq` 1421e6. Both are needed: 3.5 MHz around the default 1419 MHz would stop at 1420.75 MHz and clip the line. At 1421 MHz the band is 1419.25 – 1422.75 MHz.

        <img alt="samp_rate Variable block properties: Id samp_rate, Value 3.5e6" align="center" width="300" height="106" src="/dspira-lessons/images/PlutoSDR_samp_rate.png">
        <img alt="freq Variable block properties: Id freq, Value 1421e6" align="center" width="298" height="130" src="/dspira-lessons/images/PlutoSDR_freq.png">
    
    - POWER TO THE LNA: The Pluto SDR does not power the LNA. Therefore, it is necessary to provide +5 V dc external power to the LNA through a [bias-T](https://www.minicircuits.com/WebStore/dashboard.html?model=ZFBT-282-1.5A%2B), which is connected to the LNA and Pluto SDR as shown:
        
        <img alt="Mini-Circuits ZFBT-282-1.5A+ bias-tee: one SMA port to the Pluto SDR, the other through a female-female SMA adapter to the LNA, DC lead to +5 V power" align="center" width="329" height="199" src="/dspira-lessons/images/Bias_T_connections_PlutoSDR.png">

        An [SMA female to female connector/adapter](https://www.data-alliance.net/sma-female-to-sma-female-adapter-coupler-gender-changer/) will be needed for the connection from the bias-T to the LNA cable, as indicated in the diagram above.


**Cable Hardware:** A [coaxial cable](https://www.coaxrf.com/shop/1-rf-coaxial-cables/times-microwave-lmr240/sma-male-times-microwave-lmr240/lmr240-sma-male-to-sma-male-coaxial-rf-pigtail-cable/) is needed to connect the LNA to the SDR. Typically a 10 ft length is adequate, but any length up to 25 ft should work fine.