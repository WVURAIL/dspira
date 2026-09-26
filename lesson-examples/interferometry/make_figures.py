#!/usr/bin/env python3
"""Figures for the "Correlation and the Two-Element Interferometer" lesson.

Written by Pranav Sanghavi in 2018 as a Python 2 notebook; ported to Python 3
and modern matplotlib, with the plots given titles and axis labels so they
stand on their own on the page.

    python3 make_figures.py [--outdir ../../images/interferometry]

Needs numpy, scipy and matplotlib. Nothing else.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import signal

C = 299792458.0                      # speed of light, m/s
HI_WAVELENGTH = 0.21                 # m, the 21 cm line


def house_style():
    """A plain, legible style that exists in every matplotlib since 3.0.

    The original notebook asked for 'seaborn-poster'. Matplotlib 3.6 renamed
    every bundled seaborn style and 3.8 removed the old names outright, so
    asking for it by name now raises OSError.
    """
    for candidate in ("seaborn-v0_8-poster", "seaborn-poster"):
        try:
            plt.style.use(candidate)
            break
        except (OSError, ValueError):
            continue
    plt.rcParams.update({
        "font.size": 13.0,
        "figure.dpi": 110,
        "savefig.dpi": 110,
        "savefig.bbox": "tight",
        "axes.grid": True,
        "grid.alpha": 0.35,
        "axes.formatter.limits": (-7, 7),
        "axes.formatter.use_mathtext": True,
        "legend.frameon": True,
    })


# --------------------------------------------------------------- the functions

def boxcar(x, a, b, amp):
    """A rectangle of height `amp` between a and b."""
    return amp * np.logical_and(x >= a, x <= b)


def gaussian(x, amp, mu, sigma):
    y = (x - mu) / sigma
    return amp * np.exp(-np.power(y, 2.0) / 2)


# ------------------------------------------------------------------- figure 1

def fig_convolution_boxcar(outdir):
    """A boxcar convolved with itself is a triangle; again, a bell."""
    a, b = -0.2, 0.2
    xrange = [-2.0, 2.0]
    xpoints = 1000
    dx = (xrange[1] - xrange[0]) / float(xpoints)
    x = np.linspace(xrange[0], xrange[1], xpoints)

    # normalise to unit area so the three panels are comparable
    y = boxcar(x, a, b, 1.0)
    amp = float(xpoints) / ((xrange[1] - xrange[0]) * y.sum())
    y = boxcar(x, a, b, amp)

    once = dx * np.convolve(y, y, "same")
    twice = dx * np.convolve(once, y, "same")

    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(7.2, 7.2))
    for ax, data, title in zip(
            axes, (y, once, twice),
            ("Boxcar",
             "Boxcar convolved with a boxcar — a triangle",
             "Triangle convolved with a boxcar — nearly a bell")):
        ax.plot(x, data, "-", color="#1f4e8c")
        ax.set_title(title, fontsize=13)
        ax.set_ylabel("amplitude")
    axes[-1].set_xlabel("x")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "convolution-boxcar.png"))
    plt.close(fig)


# ------------------------------------------------------------------- figure 2

def fig_convolution_impulses(outdir):
    """Convolving with a Gaussian is what a finite beam does to point sources."""
    xrange = [-2.0, 2.0]
    xpoints = 1000
    dx = (xrange[1] - xrange[0]) / float(xpoints)
    x = np.linspace(xrange[0], xrange[1], xpoints)
    sigma = 0.1

    def at(x0):
        return int((x0 - xrange[0]) / dx)

    spikes = (signal.unit_impulse(xpoints, [at(-1.0), at(0.0), at(1.0)])
              + 0.20 * signal.unit_impulse(xpoints, at(1.50))
              - 0.25 * signal.unit_impulse(xpoints, "mid")
              + 0.50 * signal.unit_impulse(xpoints, at(-1.00))
              + 0.50 * signal.unit_impulse(xpoints, at(-1.35)))

    kernel = gaussian(x, 1.0, 0.0, sigma)
    smoothed = dx * np.convolve(spikes, kernel, "same")

    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(7.2, 7.2))
    for ax, data, title in zip(
            axes, (spikes, kernel, smoothed),
            ("Point sources on the sky",
             "The telescope's response — a Gaussian beam",
             "What the telescope actually records")):
        ax.plot(x, data, "-", color="#1f4e8c")
        ax.set_title(title, fontsize=13)
        ax.set_ylabel("amplitude")
    axes[-1].set_xlabel("position")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "convolution-impulses.png"))
    plt.close(fig)


# ------------------------------------------------------------------- figure 3

def dish_diameter(angres_deg, wavelength=HI_WAVELENGTH):
    """Diameter needed for a given angular resolution, circular aperture."""
    return 1.22 * wavelength / np.radians(angres_deg)


def fig_dish_diameter(outdir):
    """Why one dish is not enough."""
    arcsec = np.logspace(np.log10(0.010), np.log10(3600.0), 400)   # 10 mas - 1 deg
    d = dish_diameter(arcsec / 3600.0)

    marks = [
        (3600.0, "1 degree"),
        (60.0, "1 arcmin"),
        (1.0, "1 arcsec"),
        (0.015, "15 milliarcsec\n(what the VLA does)"),
    ]

    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    ax.loglog(arcsec, d / 1e3, "-", color="#1f4e8c", lw=2)
    ax.set_xlabel("angular resolution (arcsec)")
    ax.set_ylabel("dish diameter required (km)")
    ax.set_title("A single dish at 21 cm, $D = 1.22\\,\\lambda/\\theta$", fontsize=13)
    ax.invert_xaxis()

    for a, label in marks:
        dd = dish_diameter(a / 3600.0) / 1e3
        ax.plot([a], [dd], "o", color="#c0392b", ms=7, zorder=5)
        ax.annotate("%s\n%s" % (label, _fmt_km(dd)), (a, dd),
                    textcoords="offset points", xytext=(10, -22),
                    fontsize=10, ha="left")

    ax.set_ylim(top=1e5)
    ax.axhline(12.74e3, color="#7f8c8d", ls="--", lw=1)
    ax.annotate("diameter of the Earth", (arcsec[0], 12.74e3),
                textcoords="offset points", xytext=(10, 8),
                fontsize=10, color="#7f8c8d")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "dish-diameter.png"))
    plt.close(fig)


def _fmt_km(km):
    if km < 0.001:
        return "%.2f m" % (km * 1e3)
    if km < 1:
        return "%.0f m" % (km * 1e3)
    return "%.0f km" % km


# ------------------------------------------------------------------- figure 4

def fig_fringes(outdir):
    """The fringe pattern of a two-element interferometer, and what a finite
    bandwidth does to it."""
    theta = np.linspace(0.0, 180.0, 1000)

    single = np.exp(-1j * 2 * np.pi * 3.0 * np.cos(np.radians(theta)))

    # the same baseline seen across a band, 2 to 4 wavelengths
    blambda = np.linspace(2.0, 4.0, 100)
    wide = np.zeros_like(theta, dtype=complex)
    for bl in blambda:
        wide += np.exp(-1j * 2 * np.pi * bl * np.cos(np.radians(theta)))
    # normalise each panel to its own peak: the point of the comparison is the
    # shape, not the absolute level
    single = single / np.abs(single).max()
    wide = wide / np.abs(wide).max()

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.4),
                             subplot_kw={"projection": "polar"})
    for ax, data, title in zip(
            axes, (single, wide),
            ("One frequency\nbaseline = 3 wavelengths",
             "Averaged across a wide band\nbaseline 2 to 4 wavelengths")):
        ax.plot(np.radians(theta), np.abs(np.real(data)),
                color="#1f4e8c", label="cosine correlator")
        ax.plot(np.radians(theta), np.abs(np.imag(data)),
                color="#c0392b", label="sine correlator")
        ax.set_title(title, fontsize=12, pad=18)
        ax.set_thetamin(0)
        ax.set_thetamax(180)
    axes[0].legend(loc="lower left", bbox_to_anchor=(-0.15, -0.12), fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "fringes.png"))
    plt.close(fig)


# ------------------------------------------------------------------- figure 5

def fig_autocorrelation(outdir):
    """Autocorrelation pulls a period out of noise you cannot see through.

    The one figure here that is not from the 2018 notebook: the lesson's
    correlation section had no illustration, and this is the reason a radio
    astronomer cares about the operation at all.
    """
    rng = np.random.default_rng(20180521)
    t = np.linspace(0, 10, 2000)
    period = 1.3
    clean = np.sin(2 * np.pi * t / period)
    noisy = clean + rng.normal(0, 3.0, t.size)

    ac = np.correlate(noisy, noisy, "full")[noisy.size - 1:]
    ac = ac / ac[0]
    lag = t - t[0]

    fig, axes = plt.subplots(2, 1, figsize=(7.6, 6.2))
    axes[0].plot(t, noisy, lw=0.7, color="#95a5a6", label="signal + noise")
    axes[0].plot(t, clean, lw=1.6, color="#1f4e8c", label="the sine wave, hidden in it")
    axes[0].set_xlabel("time (s)")
    axes[0].set_ylabel("amplitude")
    axes[0].set_title("A sine wave three times smaller than the noise", fontsize=13)
    axes[0].legend(fontsize=10)

    # Skip the zero-lag spike: it is always 1.0 by construction and squashes
    # everything that carries the information into the bottom of the panel.
    keep = (lag >= 0.15) & (lag <= 6.0)
    axes[1].plot(lag[keep], ac[keep], color="#1f4e8c")
    for k in range(1, 5):
        axes[1].axvline(k * period, color="#c0392b", ls="--", lw=1)
    span = np.abs(ac[keep]).max() * 1.35
    axes[1].set_ylim(-span, span)
    axes[1].annotate("peaks every %.1f s — the period" % period,
                     (period, span * 0.72), textcoords="offset points",
                     xytext=(10, 0), fontsize=11, color="#c0392b")
    axes[1].set_xlim(0, 6)
    axes[1].set_xlabel("lag (s)")
    axes[1].set_ylabel("autocorrelation")
    axes[1].set_title("Its autocorrelation, zero lag omitted — the period is there",
                      fontsize=13)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "autocorrelation.png"))
    plt.close(fig)


FIGURE_FILES = {
    "fig_convolution_boxcar": "convolution-boxcar.png",
    "fig_convolution_impulses": "convolution-impulses.png",
    "fig_autocorrelation": "autocorrelation.png",
    "fig_dish_diameter": "dish-diameter.png",
    "fig_fringes": "fringes.png",
}


def _filename(fn):
    return FIGURE_FILES[fn.__name__]


def shrink(path, colors=128):
    """Quantise to a small palette. These are line plots on white, so 128
    colours is visually lossless and cuts the files to about a third - which
    matters for teachers on slow connections. Skipped silently if Pillow is
    not installed; the figures are correct either way.
    """
    try:
        from PIL import Image
    except ImportError:
        return
    im = Image.open(path).convert("RGB")
    im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT,
                dither=Image.Dither.NONE).save(path, optimize=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--outdir", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "images", "interferometry"))
    args = ap.parse_args()
    outdir = os.path.abspath(args.outdir)
    os.makedirs(outdir, exist_ok=True)
    house_style()
    for fn in (fig_convolution_boxcar, fig_convolution_impulses,
               fig_autocorrelation, fig_dish_diameter, fig_fringes):
        fn(outdir)
        shrink(os.path.join(outdir, _filename(fn)))
        print("  %s" % fn.__name__)
    print("wrote figures to %s" % outdir)


if __name__ == "__main__":
    main()
