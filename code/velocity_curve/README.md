# Velocity Curve — analysis code

Code companion to the lesson
[*Determining a Velocity Curve of the Milky Way Galaxy*](https://wvurail.org/dspira/Astronomy_VelocityCurve_Overview).

| File | What it does |
|---|---|
| `galactic_plane_sine_fit.ipynb` | Fits a sine curve to HI Doppler velocity vs. galactic longitude (Part 1, Quadrants II and III) |
| `quadII_III_velocity_vs_longitude.csv` | Sample dataset — replace with your class's measurements |

## Using it with your own data

Open `quadII_III_velocity_vs_longitude.csv` and replace its rows with your measurements. Each pointing needs galactic longitude in degrees and velocity in km/s. Rerun the notebook from the top. No code changes needed.

## Running it

```bash
pip install numpy scipy matplotlib jupyterlab
jupyter lab galactic_plane_sine_fit.ipynb
```

Verified against numpy 2.x / scipy 1.17 / matplotlib 3.10.

## Provenance

Originally written for DSPIRA, this notebook lived in the now-archived `dspira-jupyter` repository. It appeared alongside unrelated JupyterLite demonstrations and had no lesson links. Moved here so it lives with the lesson it belongs
to. It now reads data from CSV instead of hard-coding values. It also supports matplotlib 3.5+ (`plt.grid(b=...)` was removed).
