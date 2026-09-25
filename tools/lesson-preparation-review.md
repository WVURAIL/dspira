# Lesson preparation review, September 25, 2026

All 49 lesson posts now have individual `equipment` and `preparation` fields.
The source for each entry is the activity text and material descriptions on that page.
This is a review of written requirements, not a classroom or hardware trial.
Linked worksheets, external documents, and videos still need review before classroom use.

The review distinguishes:

- Reading and video activities from practical construction or observing.
- Simulated GNU Radio signals from exercises requiring a receiver or audio input.
- Supplied telescope data from activities that collect new observations.
- Alternative installation routes from steps everyone must complete.
- Single-horn work from optional interferometry and community projects.

No unsupported class durations, tested hardware configurations, or test dates were added.
The calibration warm-up guidance comes from the existing procedure.
Teachers should record setup time separately from activity time when those details become available.

## Calibration software check

The `systemp_calibration` block was checked at shared-library revision
`cdbda4f577b538c0750b882241f8a36ecc2e88f8` under GNU Radio 3.10.9.2.
Synthetic 4096-channel inputs were passed through one vector at a time:

- Hot input 350 and cold input 60 produced gain 1 and system temperature 50 K.
- Calibrated input 60 returned 10 K; input 80 returned 30 K away from smoothing edges.
- Switching to cold mode preserved the hot reference.
- Switching to calibrated mode preserved both references.
- Spectrum capture wrote 4096 frequency-temperature rows to the configured prefix.

These checks support the mode-switching instructions and correct the old 20 K baseline statement.
They do not establish receiver performance, full scheduler behavior, sky calibration accuracy, or agreement with the video.
The hardware and video review remains tracked in [issue 32](https://github.com/WVURAIL/dspira/issues/32).
Lesson timing and classroom confirmation remain tracked in [issue 33](https://github.com/WVURAIL/dspira/issues/33).
