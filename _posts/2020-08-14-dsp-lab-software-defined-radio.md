---
layout: post
usemathjax: true
date:   2020-08-14
title: "Digital Signal Processing using GNU Radio - Software Defined Radio"
summary: Connect a radio receiver and investigate amplitude modulation, frequency modulation, and FM reception.
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Digital Signal Processing']
order: 4
permalink: /dsplab-sdr/
meta_description: "Use a software-defined radio with GNU Radio. Explore receiver settings, amplitude and frequency modulation, and an FM radio flowgraph."
equipment: "GNU Radio, GQRX, an SDR receiver with its driver, an antenna, and computer audio output."
preparation: "Complete the introductory lab first. Confirm receiver access in GQRX before building the FM radio flowgraph."
---

## 2. Software Defined Radio - Hardware

In [Lab 1]({{ site.baseurl }}/dsplab-intro/) we learned how to work around GNU Radio Companion (GRC) and simulate signals and instruments. We shall now step into the real world with real signals. 

<!-- TOC -->

- [2. Software Defined Radio - Hardware](#2-software-defined-radio---hardware)
    - [2.1. Introduction](#21-introduction)
    - [2.2 Frequency Correction of the SDR Dongle](#22-frequency-correction-of-the-sdr-dongle)
    - [2.3. GNU Radio FM](#23-gnu-radio-fm)
        - [2.3.1  Signal Modulation](#231--signal-modulation)
            - [2.3.1.1 Amplitude Modulation](#2311-amplitude-modulation)
            - [2.3.1.2 Frequency Modulation](#2312-frequency-modulation)
        - [2.3.2 Let's Make our FM Radio](#232-lets-make-our-fm-radio)
    - [2.4. Fun SDR/GNU Radio things](#24-fun-sdrgnu-radio-things)

<!-- /TOC -->

## 2.1. Introduction

A "simplified" diagram of the device which we shall be using is shown below:

![AIRSPY]({{ site.baseurl }}/images/software-defined-radio/airspy-receiver.png)

Simplifying this further for a general SDR hardware including the energy conversions:

(EM Waves)))) >-(Antenna)-->(Amplifier)--->(Local Oscillators + Filters)-->(Analog to Digital Convertor)-->(networking control: usually USB)--->[Computer]

Radio Waves excite electrons in the antenna and induces a current. The frequencies the antenna is most sensitive to is determined by the geometry of the antenna's design. The electric current is then initially amplified a bit. Use a "Low Noise Amplifier" to minimize noise added by local electronics to the antenna signal. Processing at a fixed frequency improves receiver performance. A local oscillator (LO) enables this conversion. It is an electronic oscillator used with a mixer to change the frequency of a signal. This conversion is called heterodyning. It produces the sum and difference of the input and local oscillator frequencies. The desired frequency is then filtered out and if required amplified again. Finally, digitize the signal and send it to the computer. Our GNU Radio code can then process it.

[↑ Go to the Top of the Page](#)
## 2.2 Frequency Correction of the SDR Dongle

The hardware is well made, but a precision clock is quite expensive. The frequency the "tuner" tunes to may be slightly off from the actual frequency it is tuning to. We can correct for that in the software.  For high-end SDR dongles this correction is virtually non existent but some low-end dongles have higher deviations!

We can transmit a signal using a known and reliable tone. Then we use our receiver set up with gqrx to see the signal. If the incoming signal is exactly at the expected frequency then the internal clock is working well. Otherwise, open gqrx's ``input controls`` tab. Adjust ``freq. correction`` until the peak reaches the correct position.
 This value will be different for all dongles.  It also changes with the temperature of the dongle.  It is interesting to watch this change as the dongle warms up. Note your value for future purposes. 

[↑ Go to the Top of the Page](#)
## 2.3. GNU Radio FM

We used gqrx in section 1.2 to listen to FM now we shall code our own radio using GRC!

### 2.3.1  Signal Modulation

Modulation is a process of mixing a signal with a sinusoid to produce a new signal. Consider a signal represented by the function: 

$$
f(t) = A \sin(\omega t + \phi).
$$

This sinusoid has 3 variables that can be altered to change the function f(t). The first term, A, is called the magnitude, or amplitude of the sinusoid. The next term, $$\omega$$ is known as the frequency, and the last term, $$\phi$$ is known as the phase angle. We can encode our message in either of these three parameters.

The sinusoidal signal that is used in the modulation is known as the carrier signal, or simply "the carrier". The signal modulating the sinusoidal carrier is the "data signal" or "message signal".

Some data signals are unsuitable for direct transmission. Modulation can produce a signal better suited to transmission.

It follows  from above we encode in the above three variables. Consequently, we have 3 basic types of analog modulation:

- Amplitude Modulation
- Frequency Modulation
- Phase Modulation

#### 2.3.1.1 Amplitude Modulation

For our discussion of amplitude modulation consider a carrier wave of frequency $$f_c$$ and amplitude $$A$$ given by:

$$
c(t) = A \cdot \sin(2 \pi f_c t).
$$

Let $$m(t)$$ represent the modulation waveform. Use a sine wave at $$f_m$$ for modulation. Choose a frequency, such as audio, much lower than $$f_c$$:

$$
m(t) = M\cdot \cos(2 \pi f_m t + \phi), 
$$

where $$M$$ is the amplitude of the modulation. If $$M>1$$ then overmodulation occurs and reconstruction of message signal from the transmitted signal is more difficult. Amplitude modulation results when the carrier $$c(t)$$ is multiplied by the positive quantity  $$(1+m(t))$$:


$$
y(t) = [1 + m(t)]\cdot c(t) \\
\ \ = [1 + M\cdot \cos(2 \pi f_m t + \phi)] \cdot A \cdot \sin(2 \pi f_c t)
$$

Using trigonometric identities, $$y(t)$$ can be shown to be the sum of three sine waves:

$$
y(t) = A \cdot \sin(2 \pi f_c t) + \frac{AM}{2} \left[\sin(2 \pi (f_c + f_m) t + \phi) + \sin(2 \pi (f_c - f_m) t - \phi)\right]
$$

The modulated signal has three components. The carrier $$c(t)$$ is unchanged. Two sine-wave sidebands lie just above and below the carrier frequency $$f_c$$.

Demodulation or extracting the message from the carrier involves simply filtering out the carrier signal. We can build an AM receiver in GNU Radio. However, our SDR dongle tunes only from about 20 MHz to 1800 MHz. 

#### 2.3.1.2 Frequency Modulation

The message changes the carrier's instantaneous frequency:

$$ f_i(t) = f_c + f_\Delta x_m(t). $$

Here, \\(f_c\\) is the carrier frequency and \\(f_\Delta\\) sets the frequency deviation.
Phase is the integral of angular frequency, so the transmitted signal is

$$
y(t) = A_c \cos\left(2\pi f_c t + 2\pi f_\Delta\int_0^t x_m(u)\,du + \phi\right).
$$

### 2.3.2 Let's Make our FM Radio

An FM demodulator recovers the message from changes in phase.
Writing the phase as \\(\theta(t)\\) gives

$$
\theta'(t) = 2\pi\left[f_c + f_\Delta x_m(t)\right].
$$

Subtract the carrier term and scale by \\(2\pi f_\Delta\\) to recover \\(x_m(t)\\).

A similar operation can be achieved in GNU radio using the following flow:

FM ---> |Filter out the signal of interest| ---> |Resample Signal| ---> |Quadrature Demodulator|--->|Lowpass Filter| ---> Audio Signal

The quadrature demodulator handles complex input, so it uses a method other than differentiation. Its output is still proportional to changes in input frequency. (That GNU Radio block actually has a good explanation of the math in the description. )   

**Settings for an Airspy R2:**

Close GQRX before opening the receiver in GNU Radio.
Create `samp_rate = 2500000`, `quad_rate = 240000`, and `audio_rate = 48000`.
Use the following settings for the chain above:

| Block | Settings | Output sample rate |
| --- | --- | --- |
| Osmocom Source | Device `airspy=0`; sample rate `samp_rate`; tune to a local FM station | 2,500,000 samples/s |
| Low Pass Filter | Complex input; gain 1; cutoff 100000 Hz; transition 20000 Hz; decimation 10 | 250,000 samples/s |
| Rational Resampler | Complex input; interpolation 24; decimation 25 | 240,000 samples/s |
| Quadrature Demod | Gain `quad_rate/(2*math.pi*75000)`; import `math` with an Import block | 240,000 samples/s |
| Low Pass Filter | Float input; sample rate `quad_rate`; cutoff 15000 Hz; transition 3000 Hz; decimation 5 | 48,000 samples/s |
| Audio Sink | Sample rate `audio_rate` | 48,000 samples/s |

Add a Multiply Const block before the Audio Sink to control volume. Start with a small gain.
Every filter must use its input sample rate when calculating taps.
The second filter reduces the audio rate by five: `240000 / 5 = 48000`.

The [FM receiver example](https://github.com/WVURAIL/dspira-software/blob/main/examples/receivers/fm-receiver.grc) uses the same rate conversion.
Its WBFM Receive block combines demodulation, audio filtering, and de-emphasis.
Radio reception and audio playback still require compatible hardware.

[↑ Go to the Top of the Page](#)

## 2.4. Fun SDR/GNU Radio things

1. AM Radio! (see above)
2. Narrow Band FM ( same are FM but a narrower filter passband)
3. [Listen to and get airplane ADS-B data](http://www.rtl-sdr.com/adsb-aircraft-radar-with-rtl-sdr/)
To check it out on your own get this software: [dump1090](https://github.com/MalcolmRobb/dump1090) 
4. Listen to HAM radio chatter ( usually amplitude modulated )
5. EMS and police and local services radio. [local scanners and frequencies](https://www.radioreference.com/apps/db/)
6. WeatherFAX. Get latest images of weather data from naval bases! [http://www.rtl-sdr.com/receiving-weather-rtty-rtl-sdr/](http://www.rtl-sdr.com/receiving-weather-rtty-rtl-sdr/)  
7. Explore satellite reception using a currently operating satellite and compatible equipment.
The former NOAA-15, NOAA-18, and NOAA-19 APT examples no longer receive live images.
[NOAA retired those satellites in 2025](https://ospo.noaa.gov/operations/poes/status.html).

8. If transmitted nearby get a newspaper over the radio!
9. [Decode high definition radio](https://github.com/theori-io/nrsc5) with `nrsc5`
10. Build your own radio astronomy observatory! ( ok we are totally doing that!)

[↑ Go to the Top of the Page](#) ......[Next Lab]({{ site.baseurl }}/dsplab-fourier1/)
