# 1. DSP in Radio Astronomy

<!-- TOC -->

- [1. DSP in Radio Astronomy](#1-dsp-in-radio-astronomy)
    - [1.1. Introduction](#11-introduction)
    - [1.2. Software Defined Radio](#12-software-defined-radio)
    - [1.3. Labs](#13-labs)

<!-- /TOC -->

## 1.1. Introduction 

Digital Signal Processing in Radio Astronomy (DSPIRA) is an NSF Research Experiences for Teachers (RET) in Engineering and Computer Science Site at the West Virginia University Lane Department of Computer Science and Engineering. The Principal Investigators are Professors Natalia Schmid and Kevin Bandura. The GBO coordinator is Richard Prestage

Aims of this program: 
1. Prepare teachers to implement DSP projects with their students, exposing them to exciting STEM career opportunities;
2. Inspire high school students to pursue careers in STEM disciplines; 
3. Broaden the reach of the DSP activities developed through DSPIRA, and 
4. Develop the communication / pedagogical skills of the teachers, project staff, graduate and undergraduate students. 

## 1.2. Software Defined Radio


A software defined radio (SDR) is a “Radio in which some or all of the physical layer functions are software defined.” A radio is any kind of device that transmits and/or receives signals wirelessly in the radio frequency (RF) spectrum from about 3 kHz to 300 GHz. Traditional radio devices are defined by their hardware and are typically only usable in a specific frequency band and for a particular type of modulation. SDRs, on the other hand, perform most of the complex signal processing needed for modern communications systems at baseband, using digital signal processing (DSP). Analog hardware is then used to translate between a (complex-valued) baseband signal and its corresponding (real-valued) bandpass signal in a frequency band that is suitable for wireless transmission and reception. In its purest form, a SDR consists of an antenna and an analog-to-digital converter for the receiving part and a digital-to-analog converter connected to a power amplifier and an antenna for the transmitting part. All the filtering and signal processing then takes place in the digital domain that can be more precisely controlled in an economic fashion than is possible for traditional analog signal processing. In modern practice, DSP is used for frequencies up to several tens or a few hundreds of MHz and analog hardware is used for frequencies of several hundreds of MHz and beyond. Often the device that translates the digial baseband signal to the analog bandpass signal is referred to as the SDR and then the device (computer) that generates the digital baseband signal is referred to as the DSP.

The main advantage of an SDR over a traditional radio is that (most of) the radio’s operating functions (often referred to as physical layer processing) are implemented through modifiable and upgradable software and firmware on programmable devices such as field programmable gate arrays (FPGA), DSPs, general purpose computers (GPP), programmable System on a Chip (SoC), etc. The use of these technologies allows new wireless features and capabilities to be added to an existing radio system without replacing or modifying its hardware.

```
Add a paragraph about SDR and Radio Astronomy
```

## 1.3. Labs

We shall explore SDR through guided labs leading up to a project of building a radio telescope and do some science.
The modules would be structure as below and you get begin by clicking [here](labs)

1. Introduction to GNU Radio & Signals
2. Signal Modulation & First steps with SDR Hardware   
3. Fourier Transforms   
4. Filters   
5. Project: A Radio Telescope    
