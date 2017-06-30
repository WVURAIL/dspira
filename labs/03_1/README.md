# 1. Fourier Series and Fourier Transforms
<!-- TOC -->

- [1. Fourier Series and Fourier Transforms](#1-fourier-series-and-fourier-transforms)
    - [1.1. An Example](#11-an-example)
    - [1.2. Fourier Transform Things Now](#12-fourier-transform-things-now)

<!-- /TOC -->

## 1.1. An Example

We can use gnuradio-companion to graphically figure out what the fourier components should be using a fourier transform.  Create a flow-graph with a signal source->FFT(fourier transform)-> complex to real/imag -> vector sinks.  The output of the real-part contains the cosine components of the transform.  The imaginary part contains the sine components of the fourier expansion.  

It is also helpful to plot the timeseries to see what your input is and the frequency sink to make it easier to just read off the frequency of the components.  

An example flowgraph looks like:
![sawtooth](img/3.png) 

We shall try to segue into the concept of fourier transforms directly by seeing how they relate to fourier series. First some mathematics to associate familiarity, the fourier transform of $$x(t)$$ is given by:

$$
X(\omega) = \int_{-\infty}^{+\infty}x(t)e^{-i\omega t}dt
$$

For the complex representation of a fourier series of a periodic function $$x(t)$$ :

$$
x(t) = \sum_{-\infty}^{\infty} c_n e^{jn\omega t}
$$

The co-effecients, $$ C_n $$ of $$ x(t) $$ (which  has the period $$ T $$ is given by the relation:

$$
c_n = \frac{1}{T} X(n\omega_o)
$$

where $$X(\omega)$$ is the fourier transform and $$\omega_o = \frac{2\pi}{T}$$

**In summary, the fourier series is a decomposition of a signal into a sum of sines and cosines. This is shown in a neat animation as shown below ( *credit: wikipedia* ) and in the next section**

![animation FS](img/Fourier_series_and_transform.gif)

## 1.2. Fourier Transform Things Now

Use the [Square Wave](../03/#13-a-sqaure-wave) and the [Triangle Wave](../03/#14-a-triangle-wave) flowgraphs from the previous exercise.

First use a ``signal source`` block to make a square wave and feed the signal into a ``QT frequency sink``

**The Frequency Sink takes the Fourier Transform the incoming signal and plots the output of the fourier transform**

Place another ``QT Frequency Sink`` and change the number of inputs to the number of fourier series sinusoids you have in your flowgraph and feed all the sinusoids (vis-a-vis the individual fourier series terms) into the frequency sink 

The output looks like this:

![1.png](img/1.png)

The couloured peaks are the Fourier transforms of the individual sinusoids. Do they align with the Fourier Transform of the pure square wave? If you add more terms of the fourier series to the sink, how do they compare?

Repeat this exercise for the triangle wave.

We've been taking fourier transform of the signal everytime we see a plot with frequency in the time axes. 

As seen in section 1.1 the FFT block is a special block which does the fourier transform really fast. We shall visit fourier transforms in detail again that in Lab 5. 