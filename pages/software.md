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

**Compatibility review is still needed.** Current checks found errors in the classroom applications on newer GNU Radio versions.
Receiver operation and calibration have not been verified for the migrated collection.
Read the [known compatibility issues](https://github.com/WVURAIL/dspira-software/blob/main/docs/KNOWN_ISSUES.md) before using these applications in class.

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
