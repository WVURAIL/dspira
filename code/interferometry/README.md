# Correlation and the two-element interferometer

The notebook behind
[wvurail.org/dspira-lessons/correlation-and-interferometry](https://wvurail.org/dspira-lessons/correlation-and-interferometry/).

Convolution, autocorrelation and cross-correlation, worked through with
figures, and then applied to what a two-element interferometer measures.

```bash
pip install numpy scipy matplotlib jupyter
jupyter notebook Interferometry.ipynb
```

Nothing else is needed — no GNU Radio, no telescope, no data files. It runs on
a laptop in a few seconds.

`make_figures.py` produces the same five figures as PNGs, which is what the
lesson page uses:

```bash
python3 make_figures.py                     # writes into ../../images/interferometry
python3 make_figures.py --outdir /tmp/figs  # or somewhere else
```

## Where this came from

**Pranav Sanghavi** wrote it at this lab on 21 May 2018, as an entry in his
research diary, in Python 2. It was ported to Python 3 in 2026:

- `print` statements became functions
- `plt.style.use('seaborn-poster')` now falls back gracefully. Matplotlib 3.6
  renamed every bundled seaborn style and 3.8 removed the old names, so asking
  for that style by name raises `OSError` on any current install.
- the `ipywidgets` sliders became ordinary figures, so the notebook renders the
  same way in Jupyter, on GitHub and on the website
- the plots gained titles and axis labels
- one figure was added — autocorrelation pulling a period out of noise. The
  correlation section had the mathematics and no picture, and that picture is
  the reason a radio astronomer cares about the operation.

## What is deliberately not here

The 2018 notebook continued into the u,v plane, projected baselines and
aperture synthesis, working through
[**Fundamentals of Radio Interferometry**](https://github.com/ratt-ru/foi-course)
— the Rhodes University / NASSP course book. That material is theirs, licensed
GPL v2, and this repository is MIT, so it is linked rather than copied.

It is also simply the better place to learn it. Chapter 4, *Visibility Space*,
starts where this notebook stops.

## Licence

This directory is MIT, like the rest of the repository. The Wikipedia
definition of convolution quoted in the notebook is CC BY-SA 4.0.
