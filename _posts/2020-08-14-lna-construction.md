---
permalink: /DetailedLNAInstructions
layout: post
date:   2020-08-14
title: Detailed LNA Construction Instructions
summary:  LNA Soldering Instructions for Each Component
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Receiver Electronics']
order: 2
meta_description: "Build the DSPIRA low-noise amplifier with component-by-component soldering instructions, circuit diagrams, and demonstration videos."
equipment: "The LNA parts list, circuit board, components, soldering tools, and assembly materials listed in the instructions."
preparation: "Use this route when building an amplifier. Review soldering steps and arrange appropriate tools and supervision before assembly."
---

## First: Order the Components of the LNA  

1. Download the [parts ordering guide](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/assembly/parts-guide-v4.pdf). It lists the components and suppliers.
2. Order a bottle of silicone conformal coating. Coat the circuit board after soldering all components. The coating is not an electronic component of the LNA. This coating will protect your LNA from moisture, corrosion, fungus, dirt, dust, thermal shock, short circuits, and static discharge. This product is available through Amazon. You can also do a Google search for silicone conformal coating to find other sellers.  

## Second: Assemble a Soldering Station  

1. Get a soldering iron and a hot air gun that have temperature controls. The cheap hobby soldering iron will not do. You should set the operating temperature of the soldering iron and hot air gun to 350°C.  
2. Get a soldering stand. Include a magnifying glass, light, movable helping hands, cleaning sponge, fine-tip tweezers, and cleaning mesh.  
3. Get a spool of solder. Most solders are a mixture of tin and lead. Tin-and-silver solders are also available. They melt at higher temperatures and are much harder to use. Solder also comes in different thicknesses or diameters. A thickness of 0.025 inches is a good size for the soldering you'll be doing.  
4. The following is a picture of a typical soldering station. It is also called a rework station. The setup shown was purchased from Amazon for about $100. You can also go online and search for soldering irons, hot air guns, rework stations, and soldering stations.   

![A Typical Soldering Station]({{ site.baseurl }}/images/receiver-electronics/soldering-station.jpg)

## Third: Solder the Components onto the Circuit Board  

1. There is no best order for soldering the components onto the circuit board. If you are new to soldering, complete all components of one type before moving to the next. Beginners typically solder components in this order: capacitors, resistors, inductors, transistors, ICs, SMA connectors, and the cover. Capacitors and resistors are easiest to solder onto the board. Start with them to practice the techniques.  
2. Experienced builders can start with the hardest components. Try this order: transistors, ICs, inductors, resistors, capacitors, SMA connectors, and the cover.  
3. The following is an easy to read diagram of the circuit board. Each type of component is color coded and labelled. The orientation of each component is also indicated (vertical or horizontal).

![Image of the Component Locations on the Circuit Board](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/assembly/component-locations.jpg)

## Detailed Soldering Instructions for Each Component

### Soldering a Capacitor

Touch the soldering iron's tip to a pad. Melt a small drop of solder onto it. The drop should barely fill the pad. Place one end of the capacitor onto the drop of solder. Touch the iron's tip to both the capacitor's end and the solder drop. The heat melts the solder, which should pull the capacitor toward the pad. This should make a good connection between the capacitor and pad. Solder the capacitor's other end to the second pad. Touch the iron's tip to both the pad and the capacitor's end. Touch the solder to the end of the capacitor and soldering iron. A drop of solder should melt and adhere to the pad and the end of the capacitor. Watch the video below for a demonstration of soldering a capacitor.

<figure class="lesson-video" id="video-sOWDIGIjmGE">
{% include youtube.html title="Building a Radio Horn Telescope - LNA -Soldering a Capacitor onto the Circuit Board" url="https://youtu.be/sOWDIGIjmGE" video="sOWDIGIjmGE" %}
</figure>

### Soldering a Resistor

Soldering a resistor is identical to soldering a capacitor. You may encounter difficulty in getting solder to melt on the pad. That pad is part of the ground. The ground is copper that extends around the circuit board. You must heat a large portion of the board before that pad reaches the correct temperature. Watch the video below for a demonstration of soldering a resistor.

<figure class="lesson-video" id="video-EFwzL3n3f7s">
{% include youtube.html title="Building a Radio Horn Telescope - LNA -Soldering a Resistor onto the Circuit Board" url="https://youtu.be/EFwzL3n3f7s" video="EFwzL3n3f7s" %}
</figure>

### Soldering an Inductor

Begin soldering an inductor as you would other components. Melt a small drop of solder onto a pad. An inductor's metal plate is underneath it. This makes soldering harder than with resistors or capacitors, whose contacts are on their sides. It is important to have the tip of the soldering iron touching the bottom plate of the inductor. It is also important to leave as much room as possible on the other pad. The pad will be soldered to the thin side of the bottom plate of the inductor. Watch the video below for a demonstration of soldering an inductor.

<figure class="lesson-video" id="video-9CNtz4u5we0">
{% include youtube.html title="Building a Radio Horn Telescope - LNA -Soldering an Inductor onto the Circuit Board" url="https://youtu.be/9CNtz4u5we0" video="9CNtz4u5we0" %}
</figure>

### Soldering a Transistor

There are three different types of transistors to be soldered onto the circuit board. Each one has its own difficulties in soldering onto the circuit board. You should watch each of the following videos before soldering to determine the orientation of each transistor.

#### Transistors U1 and U3

<figure class="lesson-video" id="video-DP3ABBXyuwY">
{% include youtube.html title="Building a Radio Horn Telescope - LNA -Soldering a Transistor (U1 and U3) onto the Circuit Board" url="https://youtu.be/DP3ABBXyuwY" video="DP3ABBXyuwY" %}
</figure>

#### Transistor U2

<figure class="lesson-video" id="video-kvlXMtPB2FY">
{% include youtube.html title="Building a Radio Horn Telescope - LNA: Soldering a Transistor (U2) onto the Circuit Board" url="https://youtu.be/kvlXMtPB2FY" video="kvlXMtPB2FY" %}
</figure>

#### Transistors U4 and U5

<figure class="lesson-video" id="video-xhfXKow-tOs">
{% include youtube.html title="Building a Radio Horn Telescope - LNA: Soldering a Transistor (U4 and U5) onto the Circuit Board" url="https://youtu.be/xhfXKow-tOs" video="xhfXKow-tOs" %}
</figure>

### Soldering an Integrated Circuit \(IC\)

Soldering an IC is similar to soldering transistors U1 and U3. Watch the video below for a demonstration of soldering an IC.

<figure class="lesson-video" id="video-Vwu3AeRIN9w">
{% include youtube.html title="Building a Radio Horn Telescope - LNA -Soldering an IC onto the Circuit Board" url="https://youtu.be/Vwu3AeRIN9w" video="Vwu3AeRIN9w" %}
</figure>

### Soldering the SMA Connectors

There are two SMA connectors on the circuit board: X1 and X2. One SMA connects the antenna feed to the LNA \(X1\). The other connects the LNA output to the AirSpy \(X2\). Watch the video below for a demonstration of soldering an SMA connector.

<figure class="lesson-video" id="video-3jxUv_rlqTI">
{% include youtube.html title="Building a Radio Horn Telescope - LNA -Soldering a SMA onto the Circuit Board" url="https://youtu.be/3jxUv_rlqTI" video="3jxUv_rlqTI" %}
</figure>

### Soldering on the Protective Cover/RF Shield

The protective cover should not be soldered on until after the LNA is tested and is determined to function properly. Once the protective cover is soldered on, it will be difficult to make any repairs. The protective cover is also hard to remove after it has been soldered on. Watch the video below for a demonstration of soldering on the protective cover.

<figure class="lesson-video" id="video-H1GZ_IfYmNQ">
{% include youtube.html title="Building a Radio Horn Telescope - LNA: Attaching the RF Shield" url="https://youtu.be/H1GZ_IfYmNQ" video="H1GZ_IfYmNQ" %}
</figure>

### Applying the Protective Coating

Applying the silicone conformal coating is the last step for constructing the LNA. Watch the video below for a demonstration of how to cover the LNA with the silicone conformal coating.

<figure class="lesson-video" id="video-aINHPuxA2VM">
{% include youtube.html title="Building a Radio Horn Telescope - LNA: Applying the Conformal Coating" url="https://youtu.be/aINHPuxA2VM" video="aINHPuxA2VM" %}
</figure>