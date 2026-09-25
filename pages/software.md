---
layout: page
title: Set up telescope software
permalink: /software/
meta_description: "Prepare DSPIRA telescope software with compatibility guidance. Find installation steps, application downloads, receiver settings, and support."
lead: Check compatibility before choosing an installation route or scheduling classroom observations.
---

## Before you install

The existing telescope lessons describe Ubuntu and GNU Radio with a compatible SDR receiver.
Check your computer, receiver model, and GNU Radio version together. Installation success alone does not verify receiver operation or calibration.

**Generation checks pass on GNU Radio 3.10.9.2.** All seven applications generate Python successfully with their required block definitions installed.
Generated Python also passes syntax checks. Receiver operation and hardware calibration still need testing.
Read the [compatibility results and remaining checks](https://github.com/WVURAIL/dspira-software/blob/main/docs/KNOWN_ISSUES.md) before using these applications in class.

Email [rail@wvu.edu](mailto:rail@wvu.edu) with your operating system, GNU Radio version, and receiver model for setup guidance.

## Prepare a single-horn spectrometer

1. Review [computer requirements]({{ '/HornOperation_computerSystems' | relative_url }}).
2. Choose [an installation route]({{ '/BuildingHorn_SoftwareInfo' | relative_url }}) appropriate for your computer.
3. Install [GNU Radio]({{ '/GNURadio_Installation' | relative_url }}) and the [radio astronomy blocks]({{ '/gr_radio_astro_Installation' | relative_url }}).
4. Download the applications below and open `flowgraphs/spectrometer_w_cal.grc`.
5. Set [your receiver source block]({{ '/Spectrometer_sourceblock_settings' | relative_url }}) and follow [the running instructions]({{ '/HornOperation_runningSpectrometer' | relative_url }}).

Older instructions may target GNU Radio 3.8. Do not assume they apply unchanged to newer releases.

### Application download

[Download the application ZIP](https://github.com/WVURAIL/dspira-software/archive/refs/heads/main.zip){: .btn .btn-wvu-blue}

**Review compatibility before opening these files.** Extract the ZIP and find the `flowgraphs` folder.
The shared `radio_astro` blocks are a separate installation required by the telescope applications.
Install the receiver's GNU Radio plugin too. Osmocom and LimeSDR source blocks come from `gr-osmosdr` and `gr-limesdr`, respectively.

### Choose where observations are saved

Current spectrometer and interferometer downloads save files in your home folder by default.
To choose another folder, create it and set `DSPIRA_OUTPUT_DIR` before launching GNU Radio Companion:

```bash
mkdir -p "$HOME/dspira-data"
export DSPIRA_OUTPUT_DIR="$HOME/dspira-data"
gnuradio-companion
```

The folder must exist and be writable. Older downloaded applications may still contain someone else's output path.
Check the [recording instructions]({{ '/HornOperation_runningSpectrometer' | relative_url }}) before collecting data.

## Additional and experimental applications

The ZIP also contains two interferometers and four experimental lightning detectors.
These are not required for a first single-horn observation.

Use [DSP lesson examples]({{ '/dsp-examples/' | relative_url }}) for signal-processing exercises.
[Transient notebooks and data]({{ '/research-examples/' | relative_url }}) support advanced exploration.

## Contribute or find older files

Application changes belong in [dspira-software](https://github.com/WVURAIL/dspira-software).
Shared block changes belong in [gr-radio_astro](https://github.com/WVURAIL/gr-radio_astro).
Include software versions, receiver details, and test results.

The [repository map]({{ '/repository-map/' | relative_url }}) explains older addresses and releases.
For physical designs, use the [hardware guide]({{ '/hardware/' | relative_url }}).
