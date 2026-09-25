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

**Generation checks pass on GNU Radio 3.10.9.2.** All seven applications generate Python successfully with the DSPIRA blocks installed.
Generated Python also passes syntax checks. Receiver operation and hardware calibration still need testing.
Read the [compatibility results and remaining checks](https://github.com/WVURAIL/dspira-software/blob/main/docs/KNOWN_ISSUES.md) before using these applications in class.

Email [rail@wvu.edu](mailto:rail@wvu.edu) with your operating system, GNU Radio version, and receiver model for setup guidance.

## Prepare a single-horn spectrometer

1. Review [computer requirements]({{ '/HornOperation_computerSystems' | relative_url }}).
2. Choose [an installation route]({{ '/BuildingHorn_SoftwareInfo' | relative_url }}) appropriate for your computer.
3. [Install DSPIRA software]({{ '/install-software/' | relative_url }}), including GNU Radio dependencies, processing blocks, and applications.
4. Open `flowgraphs/spectrometer_w_cal.grc` from your `dspira-software` folder.
5. Set [your receiver source block]({{ '/Spectrometer_sourceblock_settings' | relative_url }}) and follow [the running instructions]({{ '/HornOperation_runningSpectrometer' | relative_url }}).

Older instructions may target GNU Radio 3.8. Do not assume they apply unchanged to newer releases.

### Software download

[Download DSPIRA software](https://github.com/WVURAIL/dspira-software/archive/refs/heads/main.zip){: .btn .btn-wvu-blue}

**Review compatibility before opening these files.** Extract the ZIP and find the `flowgraphs` folder.
The download includes the processing blocks and applications. Follow the [installation steps]({{ '/install-software/' | relative_url }}) before opening a flowgraph.
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

Application and DSPIRA block changes belong in [dspira-software](https://github.com/WVURAIL/dspira-software).
Include software versions, receiver details, and test results.

The [repository map]({{ '/repository-map/' | relative_url }}) explains older addresses and releases.
For physical designs, use the [hardware guide]({{ '/hardware/' | relative_url }}).
