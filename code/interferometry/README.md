# Correlation and the two-element interferometer

The notebook behind
[wvurail.org/dspira/correlation-and-interferometry](https://wvurail.org/dspira/correlation-and-interferometry/).

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

**Pranav Sanghavi** wrote it here in Python 2 on May 21, 2018. It was an entry in his research diary. It was ported to Python 3 in 2026:

- `print` statements became functions
- `plt.style.use('seaborn-poster')` now falls back gracefully. Matplotlib 3.6 renamed the bundled seaborn styles, and 3.8 removed their old names. Requesting the old style raises `OSError` on current installations.
- the `ipywidgets` sliders became ordinary figures. The notebook now renders consistently in Jupyter, on GitHub, and on the website
- the plots gained titles and axis labels
- one figure was added — autocorrelation pulling a period out of noise. The correlation section had equations but no illustration. The illustration explains why this operation matters in radio astronomy.

## What is deliberately not here

The 2018 notebook continued into the u,v plane, projected baselines, and aperture synthesis. It followed [**Fundamentals of Radio Interferometry**](https://github.com/ratt-ru/foi-course), the Rhodes University / NASSP course book. That material is theirs, licensed
GPL v2, and this repository is MIT, so it is linked rather than copied.

It is also simply the better place to learn it. Chapter 4, *Visibility Space*,
starts where this notebook stops.

## Licence

This directory is MIT, like the rest of the repository. The Wikipedia
definition of convolution quoted in the notebook is CC BY-SA 4.0.
