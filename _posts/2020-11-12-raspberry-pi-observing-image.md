---
permalink: /RaspberryPi-OsInstall
layout: post
date:   2020-11-12
title: Download and Install WVURAIL Radio Astronomy OS for Raspberry Pi
summary:  Step by Step instructions for downloading and installing Radio Astronomy Operating System for Raspberry Pis.
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 11
meta_description: "Download and install the WVU RAIL radio astronomy operating system for Raspberry Pi. Prepare a compact computer to run a horn telescope."
optional: true
equipment: "A Raspberry Pi 4, power supply, and SD card of at least 16 GB. Also provide a computer and card reader."
preparation: "This is an optional historical setup route. Review image compatibility, remote access, and the software guide before writing the card."
---

## Radio Astronomy with Raspberry Operating System
### Glen Langston,  2020 October 21

[Click to read this Document](https://drive.google.com/file/d/1Clyo3tW8s_1xhXjnvwi-_GTXlZI_uS-Z/view){: .btn .btn-wvu-blue}

***
*The text of the pdf is below*

This document describes our Raspberry Pi operating system for Science Aficionado Radio Astronomy.    The operating system (OS) draws on many volunteers' work. Contributors include the Raspberry Pi Foundation, Ubuntu, GNU Radio, and SDRplay.  The GNU Radio Collaboration made home radio astronomy possible, thanks to their free software for digital signal processing.   These volunteers created an enjoyable package for learning modern communications fundamentals.    SDRplay assembled the base OS package, including GNU Radio. Their goal was to simplify testing RSP1A devices across applications.

These notes describe my additions and telescope-network setup tips. Precise timing is a goal (ideally, time tags accurate to roughly a microsecond).
Purpose

This project helps everyone observe the Milky Way with a homemade radio telescope. Our galaxy surrounds us and is observable day and night.    Figure 1 (below) shows our location in the Milky Way and some calibrated observations, like those you will make.  There are several steps involved to get to this point. After gathering or building the parts, expect about a week's work to reach this level of observations.
   
   This project helps everyone observe the Milky Way with a homemade radio telescope. Our galaxy surrounds us and is observable day and night.    Figure 1 (below) shows our location in the Milky Way and some calibrated observations, like those you will make.  There are several steps involved to get to this point. After gathering or building the parts, expect about a week's work to reach this level of observations.

After you accomplish your first observations, the universe is yours to explore.  Expand the basic telescope with your own additions to explore more observing possibilities.


System Components

A simple metal structure funnels radio signals from the sky into the first low noise amplifier (LNA).  The first amplifier increases the faint signal by a factor of about a million. A Software Defined Radio (SDR) then receives the amplified signal.  These devices range in price from about $30 to $200.  The more expensive ones have many unique capabilities.   The estimated telescope cost is $350 to $500. Your telescope's size and choice of SDR affect the total.

All the SDR devices plug into computers via USB.   A computer is needed to gather the data into a format for display.   You can use your own laptop. However, installing its software can take more work than building the telescope.  We recommend a dedicated Raspberry Pi 4 with power supply, case, and SD card. The estimated cost is $90. (For the full introductory kit, the cost is a little more).

Figure 2 shows all the telescope hardware you’re going to need for your first observations.   The left picture shows a horn made from stovepipe, 1 foot long and 6 inches wide (30x15 cm). It uses an 8-to-6-inch duct reducer (20 to 15 cm).   A metal box, with LNA, is attached to the side of the horn.   For scale, a carpenter’s square is 18 by 24 inches (46 by 60 cm). 

Figure 2: Left is the horn.   The right picture shows the horn from the side. Its computer box contains the SDR and Raspberry Pi 4.   The PI is powered by the blue ethernet cable, which also connects the PI to the computer network.  The PI is in a weatherproof box.

More detail on the components of the computer system and amplifiers is given in the Appendix.
Software Defined Radio

A Software Defined Radio (SDR) contains amplifiers and a high-speed sampler. The sampler measures incoming signals millions of times per second.   The prices of these fantastic devices have dropped dramatically.   This guide targets a minimum-cost telescope. For that system, use the $38 NeSDR,.  Figure 3, at right, shows two SDRs attached to one Raspberry Pi computer.  Only one SDR is needed.  The devices are about 2 cm square and 5 cm long.

Figure 3:  Two low cost SDRs attached to a Raspberry Pi computer.

The NeSDR comes with antennas that you can use for testing (and playing).   However you’ll need to construct the special purpose feed for observations of the Milky Way (see Appendix).

Many other SDRs provide more capabilities.   The software also supports Airspy mini and R2 devices, the Analog Devices PlutoSDR, and SDRPlay devices.   Each of these devices has different, fantastic features and additional costs.    

The Airspy-mini has worked reasonably well for me. It offers a flat bandpass, 6 MHz bandwidth, and ample bias-tee power for the first LNA.  Two amplifiers are needed to use this SDR.  I have seen some internal RFI with these SDRs, so take care with shielding.

I mostly use SDRplay RSP1A devices, which offer good software support and bandwidth up to 10 MHz. I use 8.0 MHz.  The RSP1A's bias tee cannot power more than one amplifier. An additional bias tee may be needed.  The RSP1A has good shielding, built-in filtering and very high gain. Only one GPIOLabs HI LNA is needed to use this SDR.  The RSP1A can run at 10 MHz, but Raspberry Pis can’t keep up with that data rate. Alternate source for the RSP1A.
Critical First LNA
The first Very Low Noise Amplifier is a critical part of all radio telescopes.   The amplifiers used at observatories are often cooled to extremely low temperatures (< 33 Kelvins or -400 Fahrenheit). We need simpler amplifiers. Fortunately, newer designs offer strong performance at relatively low cost.   A short list of amplifiers and places to get them is below, in order of first is best.  The amplifiers have two important features, high gain, > 30 dB (a factor of 1000), and very low equivalent noise temperature.   Lower noise temperature is better.
Prof. Kevin Bandura’s custom HI amplifier has the highest sensitivity, but you have to build it yourself.   The performance is excellent. The measured noise temperature is around 90 Kelvins.
Nick at GPIO Labs in Canada worked with us to design an affordable neutral-hydrogen amplifier with strong performance.  The measured noise temperature is around 120 Kelvins.
NooElec Neutral Hydrogen Amplifier has an amplifier designed for Neutral hydrogen observations.  This amplifier is less expensive and easier to purchase, but has higher measured noise temperature,  greater than 150 Kelvins.   

Computer System Setup

This guide assumes each telescope has a Raspberry Pi 4. You also need a host computer: an x86 Ubuntu laptop or a Mac.   I almost never connect a keyboard and monitor to my Raspberry Pis, unless there is some sort of problem.   Rather the host computer runs Virtual Network Connections to the PIs.   After installation you will have a complete computing environment. This Includes a python programming system and C++ compiler.   

The OS includes GNU Radio and gnuradio-companion, an easy to use tool to explore signal processing.  GNU Radio can be used without any SDRs.  Watch Sophie and Evan introduce GNU Radio in a short video. They use only a laptop microphone and speakers.
Figure 4: Raspberry Pi 4 in hand.
Download

The complete OS is available in one large file: NsfSdr-20Sep18.img.xz

Look in this Shared Folder for the latest version of the OS in directory: RasberryPiOS

This file is a 2.8 GB compressed version of the full 9.5 GB OS.   The OS includes standard programs, GNU Radio 3.7.13.4, and radio astronomy software from West Virginia University.   (I hope to upgrade GNU Radio soon.)

You will need a 16 GB, or larger, SD card to install the OS.

This file must be downloaded to your host computer.  Transfer will take a while.  This software is the product of many hundreds of volunteers.   GNU Radio is a great project built on top of the Linux operating system.   This particular version was created by the folks at sdrplay.com, then tuned for Radio Astronomy by our research group. 
Transfer to SD Card

I use the free Balena Etcher program (https://www.balena.io/etcher/) to write this OS to telescope SD cards.   I usually use 32 GB cards, but 16 GB cards are sufficient, as the OS is only 9.5 GB.   Etcher can write the compressed file directly to the SD card. You do not need to uncompress it first.

After configuring your Raspberry Pi, remove its SD card. Archive the card with the Linux “dd” command. Before writing the SD image, I try to clean up any unused files and observations first.

Initial Configuration

This OS has Wi-Fi and Bluetooth disabled for radio astronomy use.   I rarely connect a keyboard and monitor to the Pi. Instead, I access it through Virtual Network Connection (VNC).  For this to work, you need to know the default IP address of the PI.  For this version the default IP address is 192.168.1.205.   You can turn WIFI on after your first login via VNC.

I chose this address because its subnet appears common on unmanaged Power over Ethernet (POE) switches.   The switch IP address is 192.168.1.1.   The 205 part was chosen because this happened to come from the 5th of the telescopes in my network.
My Linux host uses 192.168.1.200. It collects telescope data and provides a GPS time reference.  

I use the free download version of RealVNC (https://www.realvnc.com/en/).   This enables multiple connections to several Raspberry PIs.   

Each PI automatically starts a passwordless VNC session.  You probably want to give your VNC sessions passwords, but to avoid initial problems I removed the password.  When you start VNC, the VNC session will complain that the session is not secure, because there is no password.

The PI also starts a protected “ssh” server, allowing direct login, without the graphical interface.   To login, the special word is “H1!drogen”, without the quotes.

Use your mouse and keyboard to run various tutorials on the Raspberry pi operating system and configuration.   The top line of the PI has a web browser and a terminal.  
Changing the IP address
Changing the IP address is pretty easy, but requires the use of a text editor.  There are many editors in the Pi OS, including nano, vi and my favorite, emacs.  Nano is probably the easiest to start with.

To change the IP address requires a couple steps.  The first is to find out what IP address  your computer network uses.   To do this, check your home computer. On windows, at the command prompt type:
ipconfig

On a mac or linux system type: 
ifconfig

Lots of info will be printed. To find your network, look for the four numbers following the word inet.   In my case they are inet 192.168.1.99.   Yours will be different.  Change the Pi address's first three numbers to match your network's prefix, shown here as 192.168.1.  To update the Pi IP address you need to be a “super user root”.  To do this on the Pi, click the terminal button on top.  When the terminal appears  type:
sudo su

You are now “root”. Then edit the file dhcpcd.conf in the /etc/ the directory.  To do this type: 
nano /etc/dhcpcd.conf 

Near the bottom of this file you will see this line: 
static ip_address=192.168.1.205 

Change the first three numbers to match your home computer router numbers.   Pick a number not used on your network for the last number.  Usually 205 to 250 are free.

Then you need to reboot to have this take effect.  Type:
shutdown -r now
Starting Radio Astronomy
Now you can begin Radio Astronomy observations.  The SDRplay folks created a list of things to try after the Pi starts up.   Much of this has to do with SDRplay documentation.   I’ve added some radio astronomy programs at the end of their long list.    

Alternatively, you can use a terminal to type commands.  This is the old fashioned way of running a computer.  ( I'm old fashioned.) With amplifiers and an NeSDR attached, type these two commands:

```text
cd examples
python NsfIntegrate24.py
```


The first command changes to the directory (cd) containing the GNU Radio designs for Radio Astronomy.   The second command starts a python program.   The programs are also available for free from our github site, West Virginia University Radio Astronomy Instrumentation Lab (WVURAIL).  These programs have been tested on Linux x86 laptops, Mac computers, Odroid N2 and Raspberry PI (3 and 4) computers.

For AIRSPY, use NsfIntegrate25.py for 2.5 MHz bandwidth. Use NsfIntegrate100.py for 10 MHz.   For AIRSPY-mini, use NsfIntegrate30.py for 3.0 MHz bandwidth. Use NsfIntegrate60.py for 6.0 MHz.   For Pluto SDR, use NsfIntegrate45.py. For SDRplay, use NsfIntegrate80.py for 8.0 MHz bandwidth or NsfIntegrate90.py for 9.0 MHz.

After starting the python program, a graphical user interface appears and lots of messages.   If this fails the first time, try it again.  It seems that the hardware does not wake up on the very first try, but will be fine thereafter.   You will see a display looking like the next figure.

Figure 5:  Raw Radio Observations of the Sky.
First Observations
When you’ve completed the horn construction, you’ll need to first look at the ground to calibrate the observations.  The calibration consists of two observations.  The Hot load is the ground, which has a temperature of about 280 Kelvin.   You will need to set the elevation to -90 degrees and set the Record mode to “Average”.   Wait about a minute.  Set the Observing mode to “Hot/Cold”, then change the record mode to “Save” to save the Hot load observation.   A red line will appear where the average line was.   Set the observing mode back to “Survey” and then set the recording mode to “WAIT”.

The empty sky is very cold, only about 10 Kelvin (-440 F, -260 C).

Go out and move the horn to point straight up.   Next set the elevation to up (elevation +90 degrees).    Set the Record mode to “Average” again.   Wait another minute.  Then set the observing mode to “Hot/Cold” and set the Record mode to “Save”.   A blue line will appear where the average plot was.    You’ve completed calibration!

The blue line will show a very weak bump in the plot, which is our Milky Way Galaxy.   This can be much more clearly seen in the calibrated plot.   Switch the Units to “Kelvins” and the program computes the calibrated spectrum.  The broad peak at 1,420.4 MHz is the signal from the spiral arms of our Galaxy.   Your plot should look similar to the next figure.

Figure 6: Calibrated Radio Observations of the Sky.  The Milky Way galaxy spiral arms are seen as the broad peak between 1420.2 and 1420.6 MHz.
NTP Server
Because the time is critical to Astronomical Observations, it is very important to set the time correctly.   Resetting clocks after outages is tedious. Attach an inexpensive GPS hat or USB GPS mouse to a computer on your network. Some models cost less than $35.

The IP address of a computer is fixed by editing the file “dhcpcd.conf” in the /etc directory.   You will also want to edit the “/etc/hosts” file to give your telescopes some names.

The Pi also starts GPS and Precision Time Protocol daemons. It uses Chrony for the Network Time Protocol (NTP).   You will have to change the IP addresses to set up the time for your network.

Figure 7: Radio astronomy software tests capture of a GPS 1 Pulse Per Second signal.  This software introduces radio astronomy and supports initial cosmic-ray event detection.   

FYI, I use “chrony” as the time control software as it is advertised to provide smoother time transitions.  My understanding is that NTP changes the time without correcting the reference oscillator that drives the clock.   Chrony initially sets the time. It then adjusts the reference oscillator's rate to keep the clock accurate.  I have not confirmed a significant timing-accuracy difference between the “ntpd” and “chrony” daemons.     
Event Detection

Anyone can become a Science Aficionado. Join a worldwide telescope network that monitors the sky for cosmic-ray flashes.  Our software work focuses on detecting bright radio flashes from cosmic rays striking Earth's atmosphere. These flashes last millionths of a second.    These cosmic rays exceed the particle energies achievable in leading physics laboratories.

Each Aficionado can contribute uniquely. A flash covers only about a hundred meters on each side. Without a telescope there, the event is missed.

The Raspberry Pi 4 designs have been tested with Event capture. The test fed a GPS receiver's 1 Pulse-Per-Second (1PPS) output into a NooElec Neutral Hydrogen amplifier. The early, barebones, version of this amplifier has a control port which is intended to be used for calibration.  When the control signal is high, the input is grounding, causing a power change.   The 1PPS is a few millionths of a second long (a few microseconds).  These pulses show up as flashing radio signals in the data stream.   These flashes occur with great timing precision, enabling tests of the timing accuracy of the event captures software.  

The event detection python programs have names beginning with “NsfDetect??.py.   The last two characters are the sampler clock rate.   For example the SDRplay design, sampling at 9MHz has “NsfDetect90.py”.  On a Raspberry Pi 4, the design captured all 600 1 PPS pulses in 10 minutes.   

Raspberry Pi 3 computers are slower. Only designs below 3 MHz can capture events accurately without losing many samples.   A Raspberry Pi 3 and Airspy-mini were tested at 3.0 MHz for 10 minutes. They captured 484 of 600 1 PPS samples.   A Raspberry Pi 4 and RTL-SDR dongle were tested at 2.4 MHz for 10 minutes. They detected all 600 1 PPS events.

The event detection system is still under development and collaborators are welcomed.
Summary
You have the opportunity to discover the Milky Way for yourself, with the tools provided.  These tools are the door to a marvelous, unseen universe.   Join the collaboration and make your own contributions!

LightWork Memos
The more detailed tests of the system are in a set of memos.  You’re invited to contribute to these memos:

[The LightWork memo series](/lightwork/)

Live Video Demo

We demonstrated the horn online during the American Astronomical Society Meeting in June 2020.   The demo shows the telescope in operation, easily finding our Milky Way Galaxy spiral arms in a few seconds.

https://www.gb.nrao.edu/~glangsto/aas2020/Langston2020AasTelescopeWebinar.mp4

Thanks to Katherine LaFleur for pointing the telescope at the Milky Way!
Appendix 1: The complete amplifier and computer system
The complete system for full time observations has several components.   My goal was to let every student, teacher, hobbyist, and aficionado contribute sky observations and transient-event detections.   To achieve this, the computers need to be in weather proof boxes.   

The system also needs lots of gain from low noise amplifiers.   Accurate timing is needed for precise event detection.   We’re still working on getting the event detection time precision to better than a millionth of a second. 

The system below places all computing components in a watertight box beneath the horn telescope. This system has two GPIO Labs Neutral Hydrogen amplifiers, an AIRSPY mini, and a GPS hat. It also includes a Power Over Ethernet splitter, bias-tee, and Raspberry Pi case with a fan.   The assembly of these components is described elsewhere. 

My preferred system uses one GPIO Labs Neutral Hydrogen amplifier, an SDRPlay RSP1A, and a GPS hat. It includes a Power Over Ethernet hat with a fan instead of a splitter. A bias-tee and Raspberry Pi 4 with metal standoffs complete the setup.     The computer and amplifier are connected directly to the horn in metal boxes. The assembly of these components will also be described elsewhere.

To test proper operations, the 50 Ohm Load is also needed.  This 50 Ohm noise source input provides more power than all the power the horn will collect from the sky!

You can certainly improve on these designs.  Give one a try, then improve your telescope.


Appendix Figure 1: Telescope observing system. Components include a Raspberry Pi 4, AIRSPY Mini, and two GPIO Labs Neutral Hydrogen amplifiers with input bias tees.   The power is fed to the amplifiers on the same coaxial cables as the radio frequency signals.   The AIRSPY provides power to the one amplifier and the bias tee powers the other amplifier.   The GPS “hat” comes with the bulkhead cable to allow weather proofing.   The power comes into the box on the Ethernet cable.  The first LNA should be mounted in a weatherproof metal box on the horn..
The input of the first LNA is the SMA bulkhead connector with a 5 cm silver wire soldered on.  This is the only soldering needed for this project.   


Appendix Figure 2: Closeup of the GPIO Labs amplifier, the input feed probe and 50 Ohm Load.  The background has 1 inch square lines.  A long coaxial cable is needed to connect this amplifier to the computer box.  I prefer thicker, stronger, N connectors for making this connection.


Appendix Figure 3: I created a 3d printed ruler for measuring and cutting 5cm of the silver wire.  A hole in the centimeter ruler holds the wire when it is being cut. The ruler is 8 cm long, matching the distance from the horn's end to the feed probe hole.

The soldering is about as easy as can be, if you’ve got a stand to clamp the parts.   The wire should be held with paper to keep from heating up the stand while soldering.

Appendix Figure 4: Left shows the SMA connector and wire before soldering.  After soldering the feed probe is held by the SMA connector bolted to the horn. The first 50 readers who email me can receive a soldered feed probe. Contact: glen.i.langston@gmail.com

Appendix 2: Gparted
The SD card can be used immediately after the OS is transferred.   However the OS was compressed to make downloading quicker.  If you want to use the full sized SD card, the card needs to be re-partitioned after writing.  First test the SD card OS in your Pi. Expand it later if needed. Use gparted to expand the partition to the card's full size.  
Install Linux gparted with `sudo apt-get install gparted`. Insert the SD card into a USB adapter. Use gparted to expand its partition to the card's full size.   

After configuring and testing the radio astronomy software, I shrink the partition with gparted. This keeps the distribution image small.
