# 5. Fourier Analysis - Expert Mode! 

As we observed in the previous labs and theory with their corresponding exercises, Fourier analysis is a very important tool in Signal Processing. 

<!-- TOC -->

- [5. Fourier Analysis - Expert Mode!](#1-fourier-analysis---expert-mode)
    - [5.1. Fourier Transform Pairs](#11-fourier-transform-pairs)
    - [5.2. IQ signals *or* What is up with all the Complex Numbers](#12-iq-signals-or-what-is-up-with-all-the-complex-numbers)
    - [5.3. Fast Fourier Transforms (FFT)](#13-fast-fourier-transforms-fft)
        - [5.3.1. 8 Point Fast Fourier Transform **[OPTIONAL]**](#131-8-point-fast-fourier-transform-optional)
    - [5.4. Fourier Analysis in Radio Astronomy: A Spectrometer](#14-fourier-analysis-in-radio-astronomy-a-spectrometer)
    - [5.5. Revisiting the spectrometer's purpose](#15-revisiting-the-spectrometers-purpose)
    - [5.6. The Window Field in the FFT block](#16-the-window-field-in-the-fft-block)
    - [5.7. Spectral Leakage & Polyphase Filter Bank (PFB)](#17-spectral-leakage--polyphase-filter-bank-pfb)
    - [5.8. Final Upgrade: PFB Spectrometer](#18-final-upgrade-pfb-spectrometer)
    - [5.9. Saving Data](#19-saving-data)

<!-- /TOC -->

## 5.1. Fourier Transform Pairs

Let us revisit fourier transform by exploring the concept through their various properties. Refer to this [Table of Fourier Transform Pairs and Properties](http://www.ws.binghamton.edu/fowler/fowler%20personal%20page/EE301_files/FT%20Tables_rev3.pdf) and implement in gnuradio the following :

1. Fourier Transform a Sinusoid and 
2. Fourier transform of the sinusoid delayed by one sample
3. The output of the Fourier transform of a constant source of the value 1 is a dirac delta function. Find the FT of the dirac delta function and the dirac delta function time delayed.
4. Fourier transform of $$ e^{h\omega_o t} $$
5. Demonstrate the convolution property (use square wave) *Hint: Inverse Fourier transform can be implemented by choosing ``reverse`` in the ``Forward/Reverse`` Option. Hint: The output should be a triangle wave*
6. Fourier transform  a square pulse of different widths (i.e. tau *refer lab 1.3.1*)

Try to implement other properties from the link of fourier transform pairs and properties as well. 

**NOTE: Use the ``FFT`` Block for the above exercises. Use complex sources. The `FFT` block takes an input vector and outputs a complex vector. Use to appropriate stream to vector and complex to real/imaginary convertor blocks where necessary**

**The power of the FFT output is given by multiplying the complex output of the FFT by its complex conjugate**

[↑ Go to the Top of the Page](#)

## 5.2. IQ signals *or* What is up with all the Complex Numbers

If you remember from the [lab 2 introduction](../02/#21-introduction) an SDR dongle passes the incoming signal through a mixer where the receiver sets the frequency you observe by setting the "LO" frequency which is mixed (multiplied) with the incoming signal.  The signal is actually mixed with 2 LO's, one cosine wave and one sine wave.  This is called quadrature sampling, and is done so that it is possible to distinguish a signal that is some frequency(say 2MHz) below the "LO" frequency, or 2MHz above the LO frequency.  With just a single mixing and one measurement, one just cannot distinguish between a signal at those two frequencies.

![IQ](img/iq.png)

[See this jupyter notebook](I_Q_quadrature_sampling.html) for an 
introduction to the idea.  

Now demonstrate IQ processing in gnuradio.  We can demonstrate this at much lower frequencies as well.  Set the sample-rate to 48kHz.  Create 2 tones(cosine signals), one at 8kHz, one at 12kHz.  Create your LO at 10kHz, one a cosine and one a sine.

Try using the two signals independently, and added together, this is the overall 'signal'.
Now multiply this signal by the cosine and the sine "LO's".  This now will become your IQ signal.  In gnuradio, this is passed into a "float to complex" block,
where the cosine LO mixed signal is the real, and the sine multiplied is the imaginary.  This can then be passed into a sink.  

Add different syncs along the way, looking at just the cosine ("I") or sine ("Q")
multiplied signals.  With just the single incoming tone, demonstrate that you can in fact recover it after mixing.  Do we need a filter?  Where? Add one if needed.  






[↑ Go to the Top of the Page](#)

## 5.3. Fast Fourier Transforms (FFT)

The Discrete Fourier Transform for N samples is given by:

$$
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^\frac{-2\pi kn}{N}
$$

Evaluating the DFT's sums directly involves $$ N^2 $$ complex multiplications and N(N−1) complex additions, of which $$ O(N) $$ operations can be saved by eliminating trivial operations such as multiplications by 1. Multiplications are particularly expensive computations. 

Fast Fourier transform algorithms drastically reduce the computational complexity. The radix-2 Cooley–Tukey algorithm is a widely used FFT algorithm.  In comparison to the traditional DFT it can compute the same result with only $$ \frac{N}{2}log_2(N) $$ complex multiplications (again, ignoring simplifications of multiplications by 1 and similar) and $$ Nlog_2(N) $$ complex additions. 

[Check out this link for a derviation of the Cooley-Tukey Algorithm](http://en.dsplib.org/content/fft_dec_in_freq.html)

[↑ Go to the Top of the Page](#)

### 5.3.1. 8 Point Fast Fourier Transform **[OPTIONAL]**

The DFT implemented through a Cooley-Tukey Decimation in frequency FFT algorithm has the flowgraph shown below.
![8pfft](img/fft8p.png)

Use appropriate Constant multiplies and and adders to construct the above in gnuradio. Are the outputs the Valid frequency domain results? 

[↑ Go to the Top of the Page](#)

<!--
## 5.4. Fourier Analysis in Radio Astronomy: A Spectrometer

[↑ Go to the Top of the Page](#)

## 5.5. Revisiting the spectrometer's purpose

## 5.6. The Window Field in the FFT block

[↑ Go to the Top of the Page](#)

## 5.7. Spectral Leakage & Polyphase Filter Bank (PFB)

[↑ Go to the Top of the Page](#)

## 5.8. Final Upgrade: PFB Spectrometer

[↑ Go to the Top of the Page](#)

## 5.9. Saving Data

[↑ Go to the Top of the Page](#)
-->
