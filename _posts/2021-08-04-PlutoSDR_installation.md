---
layout: post
date:   2021-08-04
title: PlutoSDR software Installation 
summary:  Steps for installing the PlutoSDR software on your computer
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Receiver Electronics']
order: 4
---


The steps below outline the installation of software that is needed to run the Pluto SDR in GNU Radio. More information and support about GNU Radio and IIO Devices can be found at: [https://wiki.analog.com/resources/tools-software/linux-software/gnuradio](https://wiki.analog.com/resources/tools-software/linux-software/gnuradio)

**Step 1: Install Dependencies**

Open a terminal window. Then type (or copy and paste) and enter the following:

1. `sudo apt install libxml2 libxml2-dev bison flex cmake git libaio-dev libboost-all-dev`

2. `sudo apt install libusb-1.0-0-dev`

3. `sudo apt install libavahi-common-dev libavahi-client-dev`

4. `git clone https://github.com/analogdevicesinc/libiio.git`

5. `cd libiio`

6. `cmake .`

7. `make`

8. `sudo make install`

9. `cd ..`

**Download and build libad9361-iio**

1. `git clone https://github.com/analogdevicesinc/libad9361-iio.git`

2. `cd libad9361-iio`

3. `cmake .`

4. `make`

5. `sudo make install`

6. `cd ..`


**Additional Installations**

1. `sudo apt install bison flex cmake git libgmp-dev`

2. `sudo apt install liborc-dev`


**Build and install gr-iio from source:**

1. `git clone -b upgrade-3.8 https://github.com/analogdevicesinc/gr-iio.git`

2. `cd gr-iio`

3. `cmake .`

4. `make`

5. `sudo make install`

6. `cd ..`

7. `sudo ldconfig`

Your system should now be ready to install the PlutoSDR Source block in GNU Radio. If there are any problems, refer to the information at: [https://wiki.analog.com/resources/tools-software/linux-software/gnuradio](https://wiki.analog.com/resources/tools-software/linux-software/gnuradio)