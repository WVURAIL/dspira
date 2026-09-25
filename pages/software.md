---
layout: page
title: DSPIRA telescope software
permalink: /software/
eyebrow: Telescope resources
lead: Find classroom applications, the shared GNU Radio blocks, and the instructions for using them together.
meta_description: "Get DSPIRA classroom telescope applications and shared GNU Radio blocks. Find downloads, installation guidance, compatibility notes, and software support."
---

DSPIRA applications are GNU Radio flowgraphs. They describe how signal-processing blocks connect to form a spectrometer or another telescope instrument.
The applications live in `dspira-software`. Their reusable `radio_astro` blocks are installed from `gr-radio_astro`.

## Download the classroom applications

[Download the application files as a ZIP](https://github.com/WVURAIL/dspira-software/archive/refs/heads/main.zip){: .btn .btn-wvu-blue}

Extract the ZIP and open its `flowgraphs` folder. The collection includes a calibrated spectrometer, two interferometers, and four experimental lightning detectors.

The repository move preserved these files unchanged. Current GNU Radio checks found existing compatibility errors.
Review the [compatibility findings](https://github.com/WVURAIL/dspira-software/blob/main/docs/KNOWN_ISSUES.md) before using them in class.
Receiver operation and calibration have not been verified for this migration.

## Install the shared blocks

Follow [the installation lesson]({{ '/gr_radio_astro_Installation' | relative_url }}) to prepare GNU Radio and the shared library.
Then open the desired application from the downloaded `flowgraphs` folder.
Choose the receiver, output folders, and calibration settings for your equipment.

The shared library remains in `gr-radio_astro`. It also supports astronomy applications outside DSPIRA.
Install it once; the classroom repository does not contain another copy.

## Update or contribute

Application changes belong in [dspira-software](https://github.com/WVURAIL/dspira-software).
Reusable block changes belong in [gr-radio_astro](https://github.com/WVURAIL/gr-radio_astro).
Include the GNU Radio version, receiver model, and test results with a software contribution.

For a lesson or worksheet, use the [teacher contribution guide]({{ '/newpost/' | relative_url }}).
For schematics and fabrication files, use the [hardware guide]({{ '/hardware/' | relative_url }}).

## Find an older download

The [repository map]({{ '/repository-map/' | relative_url }}) lists replacement addresses for files moved from the shared library.
Historical releases and commit links retain their original files. Older GNU Radio 3.8 instructions refer to the separate `gr38` release line.

## More examples

Browse [DSP lesson flowgraphs]({{ '/dsp-examples/' | relative_url }}) for signal-processing exercises.
Explore [transient research notebooks and data]({{ '/research-examples/' | relative_url }}) for advanced experiments.
