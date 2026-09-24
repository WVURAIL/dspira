---
layout: post
date:   2026-08-15
title: Correlation and the Two-Element Interferometer
summary:  Convolution, autocorrelation and cross-correlation, and why two horns see what one cannot
usemathjax: true
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Digital Signal Processing']
order: 8
permalink: /correlation-and-interferometry/
meta_description: "Explore convolution, autocorrelation, and cross-correlation. Use GNU Radio labs to understand how two horn telescopes form an interferometer."
---

Every measurement a radio telescope makes is a correlation of some kind. A
single horn correlates a signal with itself; two horns correlate one against
the other. This lesson explains convolution, autocorrelation, and cross-correlation. It then uses these operations to explain what a two-element interferometer measures.

It was written by **Pranav Sanghavi** at this lab in 2018. Everything here can
be run yourself: the notebook is at
[`code/interferometry/`](https://github.com/WVURAIL/dspira-lessons/tree/master/code/interferometry)
and needs nothing but `numpy`, `scipy` and `matplotlib`.

<!-- TOC -->

- [Convolution](#convolution)
- [Cross-correlation and autocorrelation](#cross-correlation-and-autocorrelation)
- [Why interferometry](#why-interferometry)
- [The two-element interferometer](#the-two-element-interferometer)
- [The effect of bandwidth](#the-effect-of-bandwidth)
- [Where to go next](#where-to-go-next)
- [Credits](#credits)

<!-- /TOC -->

## Convolution

> "In mathematics (and, in particular, functional analysis) convolution is a
> mathematical operation on two functions (f and g) to produce a third
> function, that is typically viewed as a modified version of one of the
> original functions, giving the integral of the pointwise multiplication of
> the two functions as a function of the amount that one of the original
> functions is translated"
>
> — [Wikipedia](https://en.wikipedia.org/wiki/Convolution)

$$
(f * g)(x) \,=\, \int_{-\infty}^{+\infty} f(x-t)\,g(t)\,dt
$$

*for multiple dimensions*

$$
\begin{align}
(f * g)(x_1,\ldots,x_n ) \,&=\, (f * g)({\bf x})\\
\,&=\, \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} f(x_1-t_1, \ldots , x_n-t_n)\,g(t_1, \ldots, t_n) \,d^nt\\
\,&=\, \int_{-\infty}^{+\infty} f({\bf x}-{\bf t})\,g({\bf t}) \,d^nt\end{align}
$$

### Properties of convolution

$$
\begin{align}
f * g \,&=\, g * f&\qquad (\text{commutativity})\\
(f * g)* h \,&=\, f * (g * h)&\qquad (\text{associativity})\\
f * (g + h) \,&=\, (f * g) + (f * h) &\qquad (\text{distributivity})\\
(a\, g) * h \,&=\, a \, (g * h)&\qquad (\text{associativity with scalar multiplication})\\
\end{align}
$$

Convolution smooths. Convolving a rectangle with itself produces a triangle. Convolving that result with the rectangle again approaches a Gaussian. That is the central limit theorem happening in front of you — repeated
convolution drives almost anything towards a bell curve.

![A boxcar convolved with itself, twice]({{ site.baseurl }}/images/interferometry/convolution-boxcar.png)

The reason this matters for a telescope is the next picture. Point sources on
the sky are spikes. Your telescope has a beam — a response pattern roughly
15° across for a DSPIRA horn. **What you record is the sky convolved with the
beam.**

![Point sources convolved with a Gaussian beam]({{ site.baseurl }}/images/interferometry/convolution-impulses.png)

Two sources closer together than the beam merge into one bump. No amount of
integration time separates them; the information is gone at the moment of
measurement. That single fact is the whole motivation for interferometry.

[↑ Go to the Top of the Page](#)

## Cross-correlation and autocorrelation

Cross-correlation asks how much two signals resemble each other when one is
slid past the other:

$$
\begin{split}
(f\star g)(x) \,&=\, ({f_-}^*\circ g)(x)\\
&=\, \int_{-\infty}^{+\infty} f^*(t-x)\,g(t)\,dt\\
&\underset{t^\prime = t-x}{=}\, \int_{-\infty}^{+\infty} f^*(t^\prime)\,g(t^\prime+x)\,dt^\prime\\
\end{split}\qquad \text{,}
$$

$$
\begin{align}
(f\star g)(x_1,\ldots,x_n ) \,&=\, (f\star g)({\bf x})\\
&=\, ({f_-}^*\circ g)(x)\\
&=\, \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} f^*(t_1-x_1, \ldots , t_n-x_n)\,g(t_1, \ldots, t_n) \,d^nt\\
\end{align}
$$

Autocorrelation is the same operation with one signal played against itself:

$$
\begin{split}
R\{f\}(x) \,&=\, (f\star f)(x)\\
&=\, (f_-^* * f)(x)\\
&=\, \int_{-\infty}^{+\infty} f^*(t-x)\,f(t)\,dt\\
&\underset{t^\prime = t-x}{=}\, \int_{-\infty}^{+\infty} f^*(t^\prime)\,f(t^\prime+x)\,dt^\prime\\
\end{split}\qquad \text{.}
$$

Unlike convolution, cross-correlation does **not** flip a function. Thus, \\( f \star g \neq g \star f \\), while \\( f * g = g * f \\).

Autocorrelation is how a radio telescope finds signal underneath noise. Below
is a sine wave three times smaller than the noise it sits in — invisible in the
raw trace. Its autocorrelation still reveals the period. The noise is uncorrelated at nonzero lags, while the sine wave remains correlated.

![Autocorrelation recovering a period from noise]({{ site.baseurl }}/images/interferometry/autocorrelation.png)

This is not an analogy for what the spectrometer does — it is what the
spectrometer does. [`spectrometer_w_cal.grc`]({{ site.baseurl }}/spectrometer_w_cal_Instructions) displays a power spectrum. This is the Fourier transform of the horn voltage's autocorrelation. The Wiener–Khinchin theorem establishes this equivalence. It explains how the hydrogen line emerges from a much larger noise floor.

[↑ Go to the Top of the Page](#)

## Why interferometry

The resolution of a single dish is set by diffraction:

$$
\theta \,\approx\, 1.22 \frac{\lambda}{D}
$$

At 21 cm that is a brutal constraint. Rearranged for the diameter you would
need:

![Dish diameter required for a given angular resolution at 21 cm]({{ site.baseurl }}/images/interferometry/dish-diameter.png)

| You want | At 21 cm you need a dish |
|---|---|
| 1 degree | 15 m |
| 1 arcminute | 881 m |
| 1 arcsecond | 53 km |
| 15 milliarcseconds | 3,523 km |

The last row is the resolution the VLA reaches routinely. A single dish that
did the same would be a quarter of the diameter of the Earth. A dish of that size is impractical, regardless of budget.

The way out is to stop trying to fill the aperture and instead sample it at a
few points. Two horns separated by \\( b \\) resolve detail on the scale \\( \lambda / b \\). They match that large dish's resolution, but not its collecting area.

[↑ Go to the Top of the Page](#)

## The two-element interferometer

Take two antennas and combine their signals. There are two ways to do it:

* by **addition**, to form a *sum* interferometer, or \\( \sum \\)-interferometer
* by **multiplication**, to form a *product* interferometer, or \\( \prod \\)-interferometer

### The sum interferometer

$$P ={2 V_0^2(1+ \cos\Delta \Phi)} $$

### The product interferometer

$$R_c= \langle V_1 V_2 \rangle_t$$

$$R_c =\frac{V_0^2}{2}\cos{\omega \tau}=\frac{V_0^2}{2}\cos \Delta \Phi$$

where \\( \tau \\) is the time delay in the signal path. A source at angle \\( \theta \\) from the zenith reaches one antenna first. The geometric delay is \\( \tau = b\cos\theta / c \\). As the Earth turns, that
delay sweeps, and the output oscillates — the **fringe**.

This is a cosine correlator. Add a phase delay of \\( \pi/2 \\) to one signal path to make a sine correlator:

$$V_1=V_{01} \cos (\omega (t + \tau))  \quad V_2 = V_{02} \cos (\omega t + \frac{\pi}{2} )$$

$$
\begin{align}
R&=\langle V_{01} V_{02} \cos{(\omega t + \frac{\pi}{2})} \cos{[\omega (t + \tau) ]} \rangle_t\\
R&= V_0^2 \frac{\langle \cos(2 \omega t + \tau + \frac{\pi}{2})+\cos (\omega \tau - \frac{\pi}{2})\rangle_t}{2}
\end{align}
$$

$$R_s =\frac{V_0^2}{2}\sin{\omega \tau}$$

Run both at once and you have a complex correlator, whose output is the
**visibility**:

$$R = \int_{\Omega}  I_\nu(\mathbf{s}) e^{-\imath 2\pi \frac{\mathbf{b}\cdot\mathbf{s}}{\lambda}} d\Omega = V$$

That integral is a Fourier transform of the sky brightness. **An interferometer
measures the Fourier transform of the sky, one spatial frequency per baseline.**
Everything in aperture synthesis follows from it.

Here is the fringe pattern of a two-element interferometer with a baseline
three wavelengths long — the left panel. The lobes are the directions where the
two paths arrive in phase.

![Fringe pattern of a two-element interferometer]({{ site.baseurl }}/images/interferometry/fringes.png)

[↑ Go to the Top of the Page](#)

## The effect of bandwidth

The right panel above is the same interferometer observing across a wide band
rather than at one frequency. Across the band, the baseline length in wavelengths changes. Each frequency places its lobes differently, so averaging washes out the pattern. Near \\( \theta = 90^\circ \\), the geometric delay is zero and all frequencies agree.

This is **bandwidth decorrelation**. A broadband interferometer sees clearly only near the direction where its delays match. Arrays compensate with a delay that tracks the source. The zero-delay direction follows the target instead of remaining at the zenith.

DSPIRA's two-horn setup produces its sharpest fringes for sources transiting near the phase center. Narrowing the band preserves fringes across a wider region, at the cost of sensitivity.

[↑ Go to the Top of the Page](#)

## Where to go next

Two elements give you one spatial frequency at a time. Earth's rotation sweeps the baseline through the Fourier plane. More antennas fill that plane faster. This process is aperture synthesis.

See [**Fundamentals of Radio Interferometry**](https://github.com/ratt-ru/foi-course) for the standard treatment. Rhodes University and the National Astrophysics and Space Science Programme produced this course book. It is free to read and uses runnable notebooks. Chapter 4, *Visibility Space*, continues from this page. Start there.

Closer to home, and worth doing in this order:

* [Additive Interferometry Using Two DSPIRA Radio Horn Telescopes]({{ site.baseurl }}/FilesUploaded/2Horn_AddingInterferometry_LightWorkMemo31.pdf) — LightWork Memo 31. This is a measured version of the fringe pattern above. A solar transit on a 5.0 m baseline produced 0.043 rad spacing, compared with 0.042 rad predicted. This is what the theory on this page looks like when it comes out of a real horn.
* [Setting up a 2 Horn Interferometer]({{ site.baseurl }}/SettingUp2HornInterferometer) — building one and running it
* [Interferometry]({{ site.baseurl }}/Interferometry) — the rest of the interferometry material on this site
* [Fourier Analysis]({{ site.baseurl }}/dsplab-fourier1/) and [Expert Mode]({{ site.baseurl }}/dsplab-fourier2/) — the transforms this page leans on

[↑ Go to the Top of the Page](#)

## Credits

**Pranav Sanghavi** wrote this page's text, equations, and code at WVU's Radio Astronomy Instrumentation Laboratory on May 21, 2018. They are published under this site's MIT license. The notebook was ported from Python 2 to Python 3 in 2026. The autocorrelation figure was added then; the remaining material is his.

The definition of convolution is quoted from
[Wikipedia](https://en.wikipedia.org/wiki/Convolution) under CC BY-SA 4.0.

*Fundamentals of Radio Interferometry* is a separate work licensed under GPL v2. Its authors are the Rhodes University Centre for Radio Astronomy Techniques & Technologies and the NASSP community. It is linked above rather than reproduced.
