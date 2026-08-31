---
layout: post
date:   2020-08-30
title: Horn Construction Information
summary:  An overview of horn construction is described, with appropriate links
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Horn Construction']
order: 2
---

A complete horn telescope system can be built for a few hundred dollars, the actual cost depending on the options you choose and whether or not you have a computer. 

A horn telescope consists of 3 major parts: the antenna, the support stand, and the back-end electronics. The first two are what you see below; the third sits behind the can, out of shot.

![A finished horn telescope standing in a field. The pyramidal antenna is folded from foil-faced insulation board and feeds a square paint-thinner can at its throat; below it, a wooden cradle lets the horn turn in elevation on a stand of dimensional lumber.]({{ site.baseurl }}/images/programme/horn-on-stand.jpg)

Below we present descriptions of the different parts with links to details how to purchase the parts and how to assemble them.

## The Antenna
    
The antenna consists of the horn panels, a metal can, the wire probe, and a low noise amplifier.

The **horn panels and metal can** are assembled as a single unit. Detailed instructions on the parts involved and their assembly can be found [here.](https://drive.google.com/file/d/1qdc5lhKErFyIsc8b52ZIkCPJLi-XykSb/view?usp=sharing)

The **low noise amplifier** (LNA) is an electronic circuit that connects to the antenna probe through a standard SMA connector that is part of the can assembly. (See above.) 
    
Some options for obtaining a low noise amplifier include the following. All of these will work with the dSPIRA horn telescope and software.

+ Best option: the DSPIRA LNA – This amplifier was designed for a 1420 MHz radio telescope by Professor Kevin Bandura at WVU. This option requires ordering the circuit board and components, and then assembling the components by soldering. Details on ordering the parts and instructions on how to solder the circuit are provided [here.]({{ site.baseurl }}/DetailedLNAInstructions)

    The total cost for the parts of this circuit is approximately $30.

+ Next best option: [Low Noise Amplifier Filtered Hydrogen Line 1420 MHz LNA *32 dB* Gain LNA with Bias Tee](https://gpio.com/products/hydrogen-line-lna-with-bias-tee); $54.
+ Next best option: [Nooelec SAWbird+ H1](https://www.nooelec.com/store/sdr/sdr-addons/sawbird-h1.html) - Premium SAW Filter & Cascaded Ultra-Low Noise Amplifier (LNA) Module for Hydrogen Line (21cm) Applications; $44.95.



## The Support Stand 

The support stand described here is intended to be simple and affordable to anyone. It can be constructed out of standard lumber that can be found at any home improvement store.

It consists of a cradle that holds the horn/can assembly and a base to support the cradle.

Details on how to construct the stand shown in the picture above are provided in the document [here.](https://drive.google.com/file/d/1qdc5lhKErFyIsc8b52ZIkCPJLi-XykSb/view?usp=sharing)

The cost of the parts is under $50.
  
## The Back-end Electronics

The radio signals detected by the horn telescope are digitized by a **software defined radio** (SDR) and then processed by a digital signaling processing software.

The SDR we prefer is the [Airspy R2](https://airspy.com/airspy-r2), $169. This operates with a 10 MHz bandwidth and is the SDR that the DSPIRA software is coded for.

A less expensive option is the [Airspy Mini](https://airspy.com/airspy-r2), $99. It operates with a 6 MHz bandwidth. Only a minor adjustment to the software is needed if this SDR is used. Contact us for more information about the changes that would need to be done.

A [coaxial cable](https://www.coaxrf.com/shop/1-rf-coaxial-cables/times-microwave-lmr240/sma-male-times-microwave-lmr240/lmr240-sma-male-to-sma-male-coaxial-rf-pigtail-cable/) is needed to connect the LNA to the SDR. Refer to the diagram above. Typically a 10 ft length is adequate, but any length up to 25 ft should work fine.

The SDR comes with a cable for plugging it into a USB port on the computer. The spectrometer program on the computer is run on GNU Radio, which is a free and open source software program. Information about setting up the computer with the necessary software can be found [here.]({{ site.baseurl }}/HornOperation_computerSystems)

