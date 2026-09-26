# DSPIRA lesson audit — September 25–26, 2026

All 49 lessons across seven modules were reviewed after the repository reorganization.
This report separates link availability, software execution, and physical experiment verification.
Passing a software check does not establish receiver compatibility or scientific calibration.

## Coverage and results

- All 49 rendered lesson pages, local assets, section links, and previous/next module links checked. No unresolved local targets after repairs.
- 378 distinct page/resource URLs checked over HTTP. Content titles, document exports, and video metadata were used to avoid treating a generic HTTP 200 as success.
- 38 hosted lesson documents opened successfully. Eleven distinct PDF annotation links checked; exceptions are below.
- Nineteen distinct public Google Docs exported successfully; both Google Sheets downloaded as valid XLSX files.
- Fifteen Drive document downloads returned expected PDF, Office, or image signatures. Three large boot-image previews are public; images were not flashed or booted.
- All 25 linked YouTube videos returned public metadata. All 24 Mediasite recordings exposed public player data and retrievable video segments. One lecture was also played in a browser. Full recordings were not watched.
- Seven applications and all 29 teaching flowgraphs generated and passed Python syntax checks with GNU Radio 3.10.9.2.
- Eighteen software-only teaching examples ran briefly with an offscreen Qt display. The moving-average hierarchy was generated without a preexisting user cache.
- DSPIRA built and installed into an isolated prefix. Imports and all 36 generation checks passed using that installation.
- Twelve processing-block tests pass, including finite CSV/HDF5 recording and calibration batching. Thirty pointing-parser cases and two end-to-end processing tests pass.
- The velocity-curve and interferometry notebooks executed all ten code cells. Five figure scripts produced their PNGs.
- All 19 IQ example code cells executed. Numerical checks recover the expected ±20 MHz tones and increased image leakage with gain imbalance.
- A finite FM test recovered a 1 kHz input at 999.88 Hz after the corrected conversion to 48 kHz audio.
- Current-site mobile overflow and text-contrast checks pass. Search/history, math formatting, asset compatibility, and redirect tests pass. Browser checks confirm FM equations render and search handles matches, no matches, and clearing.

## Repairs

The software fixes are in [dspira-software 227b1c6](https://github.com/WVURAIL/dspira-software/commit/227b1c6d1c396dfb92fb297fed076e74cea8d4a7).
Calibration now processes every spectrum in a scheduler batch. CSV recording no longer drops later spectra or overwrites captures sharing a timestamp.
Teaching flowgraphs use supported window names, FFT sizes, integer decimation, current Pluto blocks, and portable recording settings.
FM source, resampler, demodulator, and audio rates now agree.

Lesson fixes include current application names, installation paths, Pluto instructions, and public reference links.
Two broken section targets were repaired while preserving their earlier anchor names.
The FM, DFT, Fourier-series, and interferometer explanations received specific equation corrections.
The observing lesson now distinguishes calibrated CSV output from the raw HDF5 processing route.
Corrections accompany the older spectrometer PDF, and alternatives accompany unavailable slide resources.

## Lesson-by-lesson record

Every row passed the current lesson's local page/asset/anchor/navigation checks.
The resource count includes distinct destinations in the lesson's main content and navigation.
External exceptions and checks requiring equipment are stated explicitly.

### Horn Construction

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [What is Needed to Build a Horn Radio Telescope](https://wvurail.org/dspira/BuildingHornTelescope_Overview) | 14 | Parts and assembly links checked. Current software filename and version corrected. Physical construction not tested. |
| 2. [Horn Construction Information](https://wvurail.org/dspira/Horn_Construction_Information) | 14 | Construction links checked; Airspy Mini product link corrected. Dimensions and assembly require a physical build. |
| 3. [Horn and Can Assembly](https://wvurail.org/dspira/Horn_can) | 9 | Both assembly PDFs open. The mini-horn PDF contains a restricted software link; see issue 36. |
| 4. [Detailed Instructions for Assembling the CAN](https://wvurail.org/dspira/assemblingcan) | 5 | Instructions, images, and video links checked. Mechanical assembly and soldering not performed. |
| 5. [Other Horn Designs](https://wvurail.org/dspira/Other_Horn_Designs) | 11 | Mini-horn and LightWork PDFs open. Added a public installation alternative for the restricted Drive folder. |

### Receiver Electronics

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [Low Noise Amplifier (LNA) Options](https://wvurail.org/dspira/LNA) | 8 | Product and construction links checked. Receiver/amplifier operation remains a hardware check. |
| 2. [Detailed LNA Construction Instructions](https://wvurail.org/dspira/DetailedLNAInstructions) | 9 | Instructions and linked resources checked. Circuit assembly and measurements not performed. |
| 3. [SDR Options](https://wvurail.org/dspira/SDR) | 10 | Receiver links checked; corrected Airspy Mini destination. |
| 4. [PlutoSDR software Installation](https://wvurail.org/dspira/PlutoSDR_installation) | 8 | Replaced obsolete source-build instructions with GNU Radio 3.10 IIO setup. Block import/generation checked; device discovery needs a Pluto. |
| 5. [Spectrometer Source Block Settings](https://wvurail.org/dspira/Spectrometer_sourceblock_settings) | 23 | Current application names and Pluto LO settings corrected. Checked sample-rate/frequency consistency; physical reception remains untested. |

### Software Setup

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [Computer and Software Needs for the Horn Telescope Spectrometer](https://wvurail.org/dspira/HornOperation_computerSystems) | 8 | Setup links checked; clarified the single DSPIRA package. Boot-image compatibility still requires a target computer. |
| 2. [Steps for Installing Software on a Computer](https://wvurail.org/dspira/BuildingHorn_SoftwareInfo) | 9 | Installation routes and navigation checked. Current source installation tested separately. |
| 3. [The Command Line and Git](https://wvurail.org/dspira/CommandLine_and_Git/) | 9 | Commands reviewed; DSPIRA build/test/install sequence executed in an isolated prefix. No destructive or account-changing commands executed. |
| 4. [Installing Ubuntu](https://wvurail.org/dspira/Ubuntu_Installation) | 9 | Marked the older installer procedure and linked current Ubuntu guidance. An OS reinstall was not performed. |
| 5. [Installing Ubuntu 22.04 with spectrometer_w_cal.grc on Bootable Flashdrive](https://wvurail.org/dspira/Install_Ubuntu_spectrometer_onFlashdrive) | 9 | Both image previews are public. Large images were not downloaded, flashed, or booted. |
| 6. [Installing GNU Radio](https://wvurail.org/dspira/GNURadio_Installation) | 6 | Linked installation route checked; GNU Radio 3.10 available in the validation environment. |
| 7. [Installing DSPIRA Software](https://wvurail.org/dspira/install-software/) | 9 | Build, tests, installation, imports, and installed-block generation pass. Corrected a doubled repository path. |
| 8. [Historical GNU Radio 3.8 Setup on Ubuntu 20.04](https://wvurail.org/dspira/gr_radio_astro_Installation_Ubuntu20) | 6 | Historical release link and commands reviewed. GNU Radio 3.8 installation was not executed. |
| 9. [Build a Simple Spectrometer](https://wvurail.org/dspira/Simple_Spectrometer) | 15 | Five worksheets, editable versions, and guide checked. Added corrections for bias power, channel width, and averaging. Speaker/receiver work needs equipment. |
| 10. [Raspberry Pi](https://wvurail.org/dspira/RaspberryPi) | 29 | Updated official documentation and verified its section anchors in a browser. Corrected RAM/power wording. Image flashing and Pi performance remain untested. |
| 11. [Download and Install WVURAIL Radio Astronomy OS for Raspberry Pi](https://wvurail.org/dspira/RaspberryPi-OsInstall) | 8 | Historical guide and linked documents checked. Hardware, boot image, and third-party observing software not executed. |

### Observing

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [What is a Horn Telescope?](https://wvurail.org/dspira/HornTelescope_IntroVideo) | 6 | Introduction, images, and onward links checked. No executable code. |
| 2. [What Can a Horn Telescope Measure?](https://wvurail.org/dspira/HornOperation_Intro) | 9 | Current application naming corrected; linked material checked. Real sky observations not repeated. |
| 3. [Setting up the Telescope](https://wvurail.org/dspira/Telescope_Setup) | 8 | Setup video available. Physical assembly and receiver initialization remain untested. |
| 4. [Horn Telescope Spectrometer Description](https://wvurail.org/dspira/HornOperation_spectrometer_description) | 13 | Controls and video links reviewed against the current application. Current filename clarified; historical video title retained. |
| 5. [Running the Calibrated Spectrometer](https://wvurail.org/dspira/HornOperation_runningSpectrometer) | 12 | Recording filenames and frequency-column guidance corrected. Finite synthetic flowgraphs verify CSV and HDF5 recording. |
| 6. [How to Calibrate the Horn Telescope](https://wvurail.org/dspira/HornOperation_Calibration) | 8 | Synthetic calibration/reference/capture tests pass, including distinct batched spectra. Absolute calibration needs a real reference observation. |
| 7. [Observations - Mapping the Sky and Measuring the Rotation Curve](https://wvurail.org/dspira/Observations/) | 17 | All six processing CLIs pass a synthetic pipeline. Velocity notebook runs. Corrected dependencies, selected-spectrum variable, and CSV/HDF5 guidance. GBT data missing: issue 37. |
| 8. [Setting Up a 2 Horn Interferometer](https://wvurail.org/dspira/SettingUp2HornInterferometer) | 10 | Both current flowgraphs generate. Updated names and recording-folder examples. Receiver synchronization, fringes, and calibration need two horns. |

### Digital Signal Processing

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [Digital Signal Processing Lectures and Demonstrations](https://wvurail.org/dspira/dsp) | 27 | Lecture PDFs open; recording player APIs and media segments checked. See shared recording coverage below. |
| 2. [Making Waves with Fourier Series](https://wvurail.org/dspira/MakingWavesFourier) | 8 | Activity resources accessible. Relevant Fourier examples generate and run without receiver hardware. |
| 3. [Digital Signal Processing using GNU Radio - Introductory Lab](https://wvurail.org/dspira/dsplab-intro/) | 77 | Software examples run; pulse expression tested at multiple widths. Corrected FFT size, pulse units, and GLFSR name. GNU Radio reference pages verified in a browser after script checks were blocked. |
| 4. [Digital Signal Processing using GNU Radio - Software Defined Radio](https://wvurail.org/dspira/dsplab-sdr/) | 23 | Corrected FM phase equation and rates. Synthetic 1 kHz FM tone recovered at 999.88 Hz. Receiver/audio operation remains untested; retired satellite exercise labeled. |
| 5. [Digital Signal Processing using GNU Radio - Fourier Analysis](https://wvurail.org/dspira/dsplab-fourier1/) | 25 | Fourier examples generate/run. Fixed square-wave section links and summation indices; old section anchor preserved. |
| 6. [Digital Signal Processing using GNU Radio - Digital Filter](https://wvurail.org/dspira/dsplab-filters/) | 36 | Filter examples generate/run, including the hierarchy on a clean setup. Corrected filter-tool dependency and normalized-frequency description. |
| 7. [Digital Signal Processing using GNU Radio - Fourier Analysis and Radio Astronomy](https://wvurail.org/dspira/dsplab-fourier2/) | 37 | IQ example: 19 cells run with expected opposite-frequency peaks. Corrected DFT/autocorrelation equations and PFB anchor. Receiver examples generate; CASPER reference renders in a browser. |
| 8. [Correlation and the Two-Element Interferometer](https://wvurail.org/dspira/correlation-and-interferometry/) | 26 | All six notebook code cells and five figure generators run. Corrected angle definition and phase term. Physical interferometry remains untested. |

### Astronomy

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [The Milky Way Galaxy](https://wvurail.org/dspira/Astro_MWG) | 18 | Lesson and activity links checked. No executable code on this page. |
| 2. [Astronomy Activity : Understanding Celestial Coordinate Systems](https://wvurail.org/dspira/A2UnderstandingCeleCoords) | 7 | Public document resources checked. Classroom/simulation activities were not performed. |
| 3. [Tools for Observational Astronomy](https://wvurail.org/dspira/ObserveTools) | 20 | Planning-resource destinations checked. Installing or operating third-party planetarium software was not part of this audit. |
| 4. [How Fast Are We Moving?](https://wvurail.org/dspira/HowFastAreWeMoving) | 9 | Teacher/student documents accessible. Classroom measurements were not performed. |
| 5. [Measuring the Earth's Speed around the Sun](https://wvurail.org/dspira/EarthAroundSun) | 21 | Documents and class spreadsheet are publicly downloadable. Experimental measurements were not repeated. |
| 6. [Determining a Velocity Curve of the Milky Way Galaxy](https://wvurail.org/dspira/Astronomy_VelocityCurve_Overview) | 30 | Documents, model spreadsheet, and supplied-data velocity notebook checked. Proprietary classroom simulation software was not executed. |
| 7. [Interferometry](https://wvurail.org/dspira/Interferometry) | 8 | Links to the theory notebook and telescope setup resolve. Notebook executed; hardware experiment remains untested. |
| 8. [Astronomy Lecture Recordings](https://wvurail.org/dspira/Astronomy_Lecture_Recordings/) | 33 | Slides open; public video sources checked. Added alternatives for unavailable/Flash resources embedded in older slides: issue 36. |

### Community Labs

| Lesson | Resources | Verification and limits |
| --- | ---: | --- |
| 1. [Cosmic rays and radio, at the WISRD lab](https://wvurail.org/dspira/WISRDUpdate) | 11 | Linked journal and poster downloads are public. External experiment was not reproduced. |
| 2. [Is the telescope good enough for the public?](https://wvurail.org/dspira/TestingForPublicUse) | 9 | Referenced article/video destinations checked. Reported field performance was not independently reproduced. |
| 3. [A hydrogen line project at PhysicsOpenLab](https://wvurail.org/dspira/PhysicsOpenLabHydrogenLine) | 7 | Project pages render in a browser. The linked 34-page PDF is readable through the web document reader despite script blocking. |
| 4. [Somebody motorized a horn telescope](https://wvurail.org/dspira/AutomatedHornTelescope) | 7 | Project/video destinations checked. Motor hardware and third-party control software were not tested. |

## Follow-up and limitations

1. **Receiver and calibration verification:** [software issue 1](https://github.com/WVURAIL/dspira-software/issues/1). Test an actual receiver from installation through saved observations. Record OS, driver, application revision, receiver, amplifier, and calibration reference. Two-horn, lightning, audio-device, Raspberry Pi, and boot-image operation remain unverified.
2. **External references and older PDFs:** [lesson issue 36](https://github.com/WVURAIL/dspira/issues/36). Covers the private mini-horn software folder, two unavailable slide links, the Flash Rotating Sky Explorer, and spectrometer PDF corrections. Existing PDFs were preserved; the website supplies alternatives or corrections.
3. **Historical observation file:** [lesson issue 37](https://github.com/WVURAIL/dspira/issues/37). The 2017 GBT notebook's 16 code cells pass syntax checks, but its observation file is missing. Its original rendered results remain readable.

All four GNU Radio wiki destinations rendered in a browser after initially returning security-verification pages.
PhysicsOpenLab's homepage and Milky Way article rendered in a browser despite HTTP 403 responses to scripts. Its 34-page project PDF was retrieved through the web document reader.
Raspberry Pi's replacement documentation rendered in a browser; its IP, SSH, and VNC section anchors were checked directly.
The CASPER reference rendered in a browser. Script checks failed TLS validation, but no insecure bypass was needed.
Optional third-party software and activities, including classroom simulations, were not exhaustively installed or executed.

The combined lab/DSPIRA/LightWork link check found 688 internal targets and zero missing files.
The source-only checker reports eleven sibling LightWork destinations because it cannot see that separate site; the combined build resolves them.
Frozen historical HTML copies are outside the current-lesson layout gate. Their older templates retain some overflow/contrast findings; they were not rewritten.

## Repeating the core checks

In DSPIRA software, follow the installation guide, then run:

```sh
ctest --test-dir build --output-on-failure
GRC_BLOCKS_PATH="$PWD/grc" python3 scripts/check_generation.py --examples
python3 scripts/check_flowgraphs.py
python3 scripts/render_catalogs.py --check
python3 tests/data-processing/test_parse_pointing.py
MPLBACKEND=Agg python3 tests/data-processing/test_pipeline.py
```

Install the receiver block definitions before generation. Generation never opens a receiver.
The site CI builds with the GitHub Pages gem and checks navigation, search, math formatting, layout, and contrast.
HTTP availability and browser verification are dated observations, not guarantees that outside services will remain available.
