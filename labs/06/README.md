# A Radio Telescope

That's been a lot of Digital Signal Processing so let us just go ahead and build our radio telecope already!

<!-- TOC -->autoauto- [A Radio Telescope](#a-radio-telescope)auto    - [6.1. Horn Antenna](#61-horn-antenna)auto    - [6.2  21cm Low Noise Amplifier](#62--21cm-low-noise-amplifier)auto    - [6.3 Spectrometer.](#63-spectrometer)auto        - [Updating software](#updating-software)autoauto<!-- /TOC -->

## 6.1. Horn Antenna 

We are building a special kind of radio telescope which uses a Horn Antenna. 

[Follow these instructions for Horn Assembly](https://github.com/WVURAIL/dspira/blob/master/labs/06/DSPIRA_Horn_Assembly.pdf)

## 6.2  21cm Low Noise Amplifier

The Neutral Hydrogen signal from the Milky Way galaxy is very faint, and the telescope needs an amplifier that adds as little noise to the signal as possible.  We have designed a low noise amplifier for you to use which will add less than 50 Kelvin noise temperature to the incoming signal.  See the attached pdf for assembly instructions:

[LNA assembly Instructions](https://github.com/WVURAIL/dspira/blob/master/labs/06/2018_06_22.pdf)

A brief memo on the initial design and performance of the LNA is here:

[LNA memo](https://github.com/WVURAIL/dspira/blob/master/labs/06/DSPIRA_memo2_LNA.pdf)

## 6.3 Spectrometer.

Use the spectrometer you designed in [Lab 5](../05)

You may want to upgrade your spectrometer to use a different output than just a standard binary data file (which you'll have to know ahead of time how to interpret).

You can use an out-of-tree module to instead save the data to an HDF5 file, which will then include additional information about what the data is, to help interpretation. Follow the instructions from the readme file at this website:

[gnuradio OOT radio astronomy package ](https://github.com/WVURAIL/gr-radio_astro)

1.) Clone the repository into an appropriate folder/repository: 

```bash
git clone https://github.com/WVURAIL/gr-radio_astro.git
```

2.) Go to the ``gr-radio_astro`` folder/repository, create a build directory inside the repository:

```bash
cd gr-radio_astro
mkdir build
```

3.)  run cmake inside the build directory:

```bash
cd build;  cmake ..
```

4.) run make inside build directory

```bash
make
```

5.)  If no errors, install

```bash
sudo make install
```

Blocks should now be available in gnuradio-companion.
 
 **Additionally install h5py**
  
 ```bash
 sudo apt install python-h5py
 sudo apt install pyhton-ephem
 ```

Blocks should now be available in gnuradio-companion, in the 'radio_astro' section.


----
### Updating software

```bash
# go to gr-radio_astro directory
git pull # pull updated changes to software
cd build # change working directory to build
cmake ..
make
sudo make install 
```
this will install the updated software

----
[↑ Go to the Top of the Page](#) ......[Next Lab](../07)
