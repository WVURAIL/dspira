# 1. Fourier Analysis

Fourier Analysis is a very powerful tool that comes into play when we discuss periodic signals. Colloquially, a periodic signal repeats.  

<!-- TOC -->

- [1. Fourier Analysis](#1-fourier-analysis)
    - [1.1. Introduction](#11-introduction)
    - [1.2. Fourier Series](#12-fourier-series)
    - [1.3. A Sqaure Wave](#13-a-sqaure-wave)
    - [1.4. A Triangle Wave](#14-a-triangle-wave)

<!-- /TOC -->

## 1.1. Introduction

Mathematically a signal $$x(t)$$ is periodic if there exists a positive constant $$T$$ such that:
$$
x(t) = x(t + T)
$$
for all values of $$t$$. The smallest value of $$T$$ for which this is true is called the fundamental period and is denoted $$T_o$$. The corresponding *fundamental frequency* is $$f_o = \frac{1}{T_o}$$. If $$T_o$$ is in seconds, then $$f_o$$ is in Hertz (Hz). The fundamental angular frequency is $$\omega_o = 2\pi f_o$$ and is measured in rad/sec.

[↑ Go to the Top of the Page](#)

## 1.2. Fourier Series

A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines. The computation and study of Fourier series is known as harmonic analysis and is extremely useful as a way to break up an arbitrary periodic function into a set of simple terms that can be plugged in, solved individually, and then recombined to obtain the solution to the original problem or an approximation to it to whatever accuracy is desired or practical. [^1]

[^1]: http://mathworld.wolfram.com/FourierSeries.html

Mathermatically in a simple sense an arbitrary function $$f(t)$$ can be decomposed as:

$$
f(x) = a_0 + \sum_{n=1}^{\infty} a_n cos(nx) + b_n sin(nx) 
$$ 


We shall explore this concept by making two waveforms using sinosoids:

## 1.3. A Sqaure Wave

From [Lab 1](../01/), we have te function generator. We use that to make a square wave of amplitude = 1. 

Mathematically it can be written as:

$$
f(x) = 
  \begin{cases} 
   0 & \text{if } -\pi \leq x \lt 0 \\
   1       & \text{if } 0 \leq x \lt \pi
  \end{cases}\ and\ f(x+2\pi)=f(x)
$$ 

The correposdonding fourier series of the square wave
$$
f(x) = \frac{1}{2} + \sum_{n=1}^{\infty} \frac{2}{(2k-1)\pi} sin(2k-1)x \\
\ \ \ = \frac{1}{2} + \frac{2}{\pi}sin(x) + \frac{2}{3\pi}sin(3x) + \frac{2}{5\pi}sin(5x) + \frac{2}{7\pi}sin(7x) + ... + + \frac{2}{n\pi}sin(nx)\ (\ n\ is\ odd)
$$

Use at least five ( or more ) sources to add sinusoids and see what waveform do you get after each added term

It should look like this:

![square wave](img/1.png) 

[↑ Go to the Top of the Page](#)

## 1.4. A Triangle Wave

The triangular wave is defined as:
$$
f(x)=|x|\  for\ -1\leq x \leq 1\ ans\ f(x+2)=f(x)\ for\ all\ x
$$

Its corresponding fourier series is:

$$
f(x) = \frac{1}{2} - \sum_{n=1}^{\infty} \frac{4}{(2k-1)^2\pi^2} cos(2k-1)\pi x \\
= \frac{1}{2} - \frac{4}{\pi^2}cos(\pi x) - \frac{4}{9\pi^2}cos(3 \pi x) - \frac{4}{25\pi^2}cos(5\pi x) - ...
$$

Make a flowgraph out of the four expanded terms above and check the output after each operation. 

It should give an output like this:

![Triangle wave](img/2,png) 

---

As an added exercise for later. Derive the fourier series for:

1.  Sqaure Wave
2.  Triangular Wave
3.  Sawtooth Wave

Try coding a flowgraph for 3.

---

[↑ Go to the Top of the Page](#) ......[Next Lab](../04)

