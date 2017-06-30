# 1. Fourier Series and Fourier Transforms

We shall try to segue into the concept of fourier transforms directly by seeing how they relate to fourier series. Mathematically, the fourier transform of $$ f(t) $$ is given by:

$$
F(\omega) = \int_{-\infty}^{+\infty}f(t)e^{-i\omega t}dt
$$

If we consider a discrete signal $$ x[n] $$ which is sampled at disctrete times, the discrete time fourier transform is given by:

$$
x[k] = \sum_{N=0}^{N-1} x[n]e^{-i\omega n}
$$



<!-- TOC -->

- [1. Fourier Series and Fourier Transforms](#1-fourier-series-and-fourier-transforms)
- [An Example](#an-example)

<!-- /TOC -->

# An Example

We can use gnuradio-companion to graphically figure out what the fourier components should be using a fourier transform.  Create a flow-graph with a signal source->FFT(fourier transform)-> complex to real/imag -> vector sinks.  The output of the real-part contains the cosine components of the transform.  The imaginary part contains the sine components of the fourier expansion.  

It is also helpful to plot the timeseries to see what your input is and the frequency sink to make it easier to just read off the frequency of the components.  

An example flowgraph looks like:
![sawtooth](img/3.png) 


-->