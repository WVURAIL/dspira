# DSP in Radio Astronomy — archived

**This material has moved to [wvurail.org/dspira-lessons](https://wvurail.org/dspira-lessons/).**

This was the DSPIRA summer institute's working repository — the labs, the
lectures and the analysis code. It was migrated in 2026 and is now read-only,
kept so existing links and citations keep resolving.

| You wanted | It is now at |
|---|---|
| Labs 1–5, the DSP sequence | [Digital Signal Processing](https://wvurail.org/dspira-lessons/categories/digital-signal-processing/) |
| Lab 7, Observations | [Observations](https://wvurail.org/dspira-lessons/Observations/) |
| The `python/` analysis scripts | [`code/observations/`](https://github.com/WVURAIL/dspira-lessons/tree/master/code/observations) |
| The GBT drift scan notebook | [`code/gbt_drift/`](https://github.com/WVURAIL/dspira-lessons/tree/master/code/gbt_drift) |
| Astronomy lecture recordings | [Astronomy Lecture Recordings](https://wvurail.org/dspira-lessons/Astronomy_Lecture_Recordings/) |
| DSP lecture recordings | [DSP Lectures](https://wvurail.org/dspira-lessons/dsp) |
| The Linux and git notes | [The Command Line and Git](https://wvurail.org/dspira-lessons/CommandLine_and_Git/) |
| Building the telescope | [All lessons](https://wvurail.org/dspira-lessons/all/) |

## What stayed here

Some things were deliberately not migrated, and this is where they remain:

* **The GNU Radio flowgraphs** in `grc-flowgraphs/`. All of them are GNU Radio
  **3.7** XML. GNU Radio 3.8 moved to a YAML format and will not open them, so
  they are kept as a record rather than as something to hand a class. If you
  are on 3.7, they work.

  The maintained spectrometer is
  [`spectrometer_w_cal.grc`](https://github.com/WVURAIL/gr-radio_astro/tree/master/examples/DSPIRA)
  in `gr-radio_astro` — one flowgraph for every radio, with the per-radio
  settings on the [source block settings
  page](https://wvurail.org/dspira-lessons/Spectrometer_sourceblock_settings).
  **Check that page before copying any tuning out of the files here.** The
  Pluto and Lime flowgraphs use a `freq` or `samp_rate` that differs from the
  documented per-radio procedure, and changing `samp_rate` without also moving
  `freq` can put the hydrogen line outside the recorded band. The analysis
  scripts in `dspira-lessons` follow the page, not these files.
* **The 2018 lecture slide decks** in `lectures/2018/`, superseded by the
  recordings linked above.
* **The LNA design memo** (`labs/06/DSPIRA_memo2_LNA.pdf`) — the measured
  design and performance of the 21 cm amplifier. A candidate for the lessons
  site once fetched out of Git LFS.
* **Lab 6**, whose build instructions were written for GNU Radio 3.7 and whose
  links point at the retired `cra` site. The current installation lessons are
  [here](https://wvurail.org/dspira-lessons/categories/telescope-software-setup/).

The astronomy lecture decks in `lectures/astronomy/` are **not** in that list
any more. All thirteen are on the lessons site: the five held back over
textbook figures — Motion of the Sky, Light and Telescopes, the Doppler
Effect, Stars, Stellar Evolution — were released once their authors confirmed
the figures had been used with permission. The copies here are the originals
and stay for the record.

Almost every PDF and slide deck in this repository — `lectures/astronomy/`,
parts of `lectures/2018/`, `labs/06/`, `archive/` — is stored with **Git LFS**.
`git clone` alone gives you tiny pointer files a few dozen bytes long; run
`git lfs pull` to fetch the real ones. The exceptions come down with an
ordinary clone: the DSP decks in `lectures/2018/DSP/` and `linux/cheatsheet.pdf`.
`NOTICE.md` records why.

---

**DSPIRA** was an NSF-funded Research Experiences for Teachers programme at the
Lane Department of Computer Science and Electrical Engineering, West Virginia
University, run with the Green Bank Observatory.
