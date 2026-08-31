# Velocity Curve — analysis code

Code companion to the lesson
[*Determining a Velocity Curve of the Milky Way Galaxy*](https://wvurail.org/dspira-lessons/Astronomy_VelocityCurve_Overview).

| File | What it does |
|---|---|
| `galactic_plane_sine_fit.ipynb` | Fits a sine curve to HI Doppler velocity vs. galactic longitude (Part 1, Quadrants II & III) |
| `quadII_III_velocity_vs_longitude.csv` | Sample dataset — replace with your class's measurements |

## Using it with your own data

Open `quadII_III_velocity_vs_longitude.csv`, replace the rows with your measurements
(one row per pointing: galactic longitude in degrees, velocity in km/s), and re-run the
notebook from the top. No code changes needed.

## Running it

```bash
pip install numpy scipy matplotlib jupyterlab
jupyter lab galactic_plane_sine_fit.ipynb
```

Verified against numpy 2.x / scipy 1.17 / matplotlib 3.10.

## Provenance

Originally written for the DSPIRA programme and previously kept in the (now archived)
`dspira-jupyter` repository, where it sat alongside unrelated JupyterLite demo content
and was not linked from any lesson. Moved here so it lives with the lesson it belongs
to. Rewritten to read its data from CSV rather than hard-coding it, and fixed for
matplotlib 3.5+ (`plt.grid(b=...)` was removed).
