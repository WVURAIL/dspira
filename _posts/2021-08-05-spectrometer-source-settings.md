---
permalink: /Spectrometer_sourceblock_settings
layout: post
date:   2020-07-27
title: Spectrometer Source Block Settings 
summary:  Settings in spectrometer for different SDR's
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Receiver Electronics']
order: 5
meta_description: "Configure the source block in the DSPIRA spectrometer for your receiver. Find the device settings needed to collect radio astronomy data."
equipment: "The spectrometer flowgraph, your SDR receiver, its driver, and amplifier connections. Some receivers also require external amplifier power."
preparation: "Identify your receiver model first. Apply both sample-rate and frequency changes where specified, and check amplifier power requirements."
---


The default source block settings in the `spectrometer_w_cal.grc` GNU Radio program are for the [Airspy R2](https://airspy.com/airspy-r2) SDR. A different SDR may require changes to the source and `samp_rate Variable` blocks. Sometimes the `freq Variable` block also needs changes. The settings for some common SDR's used with the horn telescopes are described below.

> **Why `freq` sometimes has to change too.** The program records a band
> `samp_rate` wide, centered on `freq`. The defaults are `freq` 1419 MHz and `samp_rate` 10e6.
> This records 1414 to 1424 MHz, comfortably including the hydrogen line at 1420.4058 MHz. Reducing the sample rate shrinks the band around 1419 MHz.
> Without retuning the center, the hydrogen line eventually falls outside that band. Set the sample rate to 2.4e6 and the band becomes 1417.8 to 1420.2 MHz.
> **The line lies about 0.2 MHz outside it.
> The telescope records no hydrogen.** The RTL-SDR and Pluto settings therefore change `freq` too.
> The Airspy Mini and Lime settings do not.
>
> Your band runs from `freq - samp_rate/2` to `freq + samp_rate/2`.
> It must include 1420.4058 MHz with room to spare at both ends.

Options:

+ The [Airspy Mini](https://airspy.com/airspy-r2)

    - Source block: the `osmocom Source` block is used; the "Device Arguments" are the same as for the Airspy R2. So no changes are needed in this block.

    - `samp_rate Variable` block: Find it beside `Options`, at the canvas's upper left in `spectrometer_w_cal.grc`. Open this block by double-clicking it. Change the "Value" to "6e6" (which is 6 MHz).

    <img alt="samp_rate Variable block properties: Id samp_rate, Value 6e6" align="center" width="300" height="146" src="{{ '/images/receiver-electronics/airspy-mini-sample-rate.png' | relative_url }}">

    - `freq Variable` block: leave it at 1419e6. The band becomes 1416 – 1422 MHz, which still holds the line.

+ RTL-SDR

    **Two changes are needed, not one.** The `samp_rate` change alone moves the
    hydrogen line out of the recorded band — see the box above. Make both.

    - Source block: Change the "Device Argument" to: rtl=0, bias=1, pack=0, as shown:

    <img alt="osmocom Source properties: Device Arguments rtl=0,bias=1, Sample Rate samp_rate, Frequency freq, RF/IF/BB gains 17, 12, 10 dB" align="center" width="300" height="385" src="{{ '/images/receiver-electronics/rtl-sdr-source.png' | relative_url }}">

    - `samp_rate Variable` block: Find it beside `Options`, at the canvas's upper left in `spectrometer_w_cal.grc`. Open this block by double-clicking it. Change the "Value" to "2.4e6" (which is 2.4 MHz).

    <img alt="samp_rate Variable block properties: Id samp_rate, Value 2.4e6" align="center" width="300" height="149" src="{{ '/images/receiver-electronics/rtl-sdr-sample-rate.png' | relative_url }}">

    - `freq Variable` block: next to `samp_rate`. Change the "Value" to
      **"1420.5e6"**. The band then runs 1419.3 – 1421.7 MHz, with the line at
      1420.4058 MHz inside it.

    - An RTL-SDR has two limitations at this sample rate. Neither can be fixed in the flowgraph:

        - The band covers only about ±230 km/s, clipping the line's faint wings. No region is guaranteed free of Galactic hydrogen for baseline fitting. Maps are good for seeing where the
          Milky Way is; treat the intensity numbers as indicative.
        - These SDRs produce a spurious tone at the band's exact center. At this tuning, it sits 0.1 MHz from the line. `map_h1_hdf5_drift.py` blanks a 120 kHz strip around it. The strip's proximity to the line costs roughly one quarter of the measured intensity. The comment on `DC_MASK_HALFWIDTH_HZ` in that
          script has the measured figures and the two ways to improve it.

+ Lime 

    - Source block: the Lime uses the `LimeSDR Source (RX)` block. Click on the `osmocom` block and hit Delete. Then in the search window on the tool bar at the top, type "LimeSDR". Grab the `LimeSDR Source (RX)` and drag it onto the canvas where the `osmocom` block was. Connect the blue output of `LimeSDR Source (RX)` to `Stream to Vector`. Also connect it to the three `Delay` blocks and `Complex to Real`. The final connections should look like the following:

    <img alt="LimeSDR Source (RX) output connected to Stream to Vector, three Delay blocks (4.096k, 8.192k, 12.288k), and Complex To Real" align="center" width="239" height="164" src="{{ '/images/receiver-electronics/limesdr-source-connections.png' | relative_url }}">
 
    - Open the `LimeSDR Source (RX)` block (by double-clicking) and set the following:
        - On the "General" tab, set "RF frequency" to "freq" [without the quotes]. Check that "Sample rate" is "samp_rate" [without the quotes]. "Channel" should be on "A" [without the quotes].

        <img alt="LimeSDR Source General tab: Channel A, RF frequency freq, Sample rate samp_rate, Oversample Default, MIMO phase align Disabled" align="center" width="297" height="265" src="{{ '/images/receiver-electronics/limesdr-general-settings.png' | relative_url }}">


        - The settings on the Channel A tab should be as shown:

        <img alt="LimeSDR Channel A tab: NCO frequency 0, Calibration bandwidth samp_rate, LNA path W, Analog filter bandwidth 16e6, Digital filter bandwidth 0, Gain 45 dB" src="{{ '/images/receiver-electronics/limesdr-channel-a.png' | relative_url }}" align="center" width="500px"/>
        
    - `samp_rate Variable` block: The Lime SDR can use a 10 MHz samp_rate; so no change is needed in this block. Leave `freq` at 1419e6 as well — the band stays 1414 – 1424 MHz, the same as the Airspy R2.

    - Install gr-limesdr - software needed for the Lime SDR block to run in GNU Radio.

        - Open a terminal window.

        - Type and enter: `sudo apt install gr-limesdr`

    - POWER TO THE LNA: The Lime SDR does not power the LNA. Supply external +5 V dc power through a [bias-T](https://www.minicircuits.com/WebStore/dashboard.html?model=ZFBT-282-1.5A%2B). Connect it to the LNA and Lime as shown:
        
        <img alt="Mini-Circuits ZFBT-282-1.5A+ bias-tee: one SMA port to the Lime SDR, the other through a female-female SMA adapter to the LNA, DC lead to +5 V power" align="center" width="329" height="199" src="{{ '/images/receiver-electronics/limesdr-bias-tee-connections.png' | relative_url }}">

        Use an [SMA female to female connector/adapter](https://www.data-alliance.net/sma-female-to-sma-female-adapter-coupler-gender-changer/) between the bias-T and LNA cable. Follow the diagram above.

+ ADALM-PLUTO 

    - The Adalm-Pluto SDR uses the `PlutoSDRSource` block that will need to be installed. Complete the [steps outlined here]({{ site.baseurl }}/PlutoSDR_installation) to install this block on your computer.

    - Source block: the Adalm-Pluto uses the `PlutoSDRSource` block. Click on the `osmocom` block and hit Delete. Then in the search window on the tool bar at the top, type "PlutoSDR". Grab the `PlutoSDRSource` and drag it onto the canvas where the `osmocom` block was. Connect the blue output of `PlutoSDRSource` to `Stream to Vector`. Also connect it to the three `Delay` blocks and `Complex to Real`. The final connections should look like the following:

    <img alt="PlutoSDR Source output connected to Stream to Vector, three Delay blocks (4.096k, 8.192k, 12.288k), and Complex To Real" align="center" width="277" height="237" src="{{ '/images/receiver-electronics/plutosdr-source-connections.png' | relative_url }}">

    - Open the `PlutoSDRSource` block (by double-clicking) and set the following:
        - On the "General" tab, set the values as shown:

        <img alt="PlutoSDR Source properties: LO Frequency 2400000000, Sample Rate int(samp_rate), RF Bandwidth 20000000, Buffer size 32768, Manual Gain (RX1) 64 dB" align="center" width="300" height="267" src="{{ '/images/receiver-electronics/plutosdr-source.png' | relative_url }}">

    - The `samp_rate` and `freq` Variable blocks should be set to the values shown — `samp_rate` 3.5e6 **and** `freq` 1421e6. Both changes are needed. A 3.5 MHz band centered at 1419 MHz ends at 1420.75 MHz and clips the line. At 1421 MHz the band is 1419.25 – 1422.75 MHz.

        <img alt="samp_rate Variable block properties: Id samp_rate, Value 3.5e6" align="center" width="300" height="106" src="{{ '/images/receiver-electronics/plutosdr-sample-rate.png' | relative_url }}">
        <img alt="freq Variable block properties: Id freq, Value 1421e6" align="center" width="298" height="130" src="{{ '/images/receiver-electronics/plutosdr-frequency.png' | relative_url }}">
    
    - POWER TO THE LNA: The Pluto SDR does not power the LNA. Supply external +5 V dc power through a [bias-T](https://www.minicircuits.com/WebStore/dashboard.html?model=ZFBT-282-1.5A%2B). Connect it to the LNA and Pluto SDR as shown:
        
        <img alt="Mini-Circuits ZFBT-282-1.5A+ bias-tee: one SMA port to the Pluto SDR, the other through a female-female SMA adapter to the LNA, DC lead to +5 V power" align="center" width="329" height="199" src="{{ '/images/receiver-electronics/plutosdr-bias-tee-connections.png' | relative_url }}">

        Use an [SMA female to female connector/adapter](https://www.data-alliance.net/sma-female-to-sma-female-adapter-coupler-gender-changer/) between the bias-T and LNA cable. Follow the diagram above.


**Cable Hardware:** A [coaxial cable](https://www.coaxrf.com/shop/1-rf-coaxial-cables/times-microwave-lmr240/sma-male-times-microwave-lmr240/lmr240-sma-male-to-sma-male-coaxial-rf-pigtail-cable/) is needed to connect the LNA to the SDR. Typically a 10 ft length is adequate, but any length up to 25 ft should work fine.