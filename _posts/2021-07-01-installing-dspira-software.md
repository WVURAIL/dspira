---
layout: post
date: 2021-07-01
title: Installing DSPIRA Software
summary: Install the telescope applications and their processing blocks together.
permalink: /install-software/
tags: ['School-Teachers', 'Students', 'Hobbyists']
categories: ['Software Setup']
order: 7
meta_description: "Install DSPIRA telescope applications and processing blocks together. Follow the Ubuntu setup, checks, and update steps for GNU Radio 3.10."
equipment: "An Ubuntu computer with internet access, installation permissions, and a receiver for live observations."
preparation: "Review software compatibility and identify your receiver. Preserve existing settings and customized flowgraphs before updating."
---

The `dspira-software` repository contains the telescope applications and their processing blocks.
These instructions target GNU Radio 3.10 on Ubuntu.
The [software guide]({{ '/software/' | relative_url }}) records compatibility checks and remaining hardware testing.

## Install dependencies

Open a terminal and run:

```sh
sudo apt-get update
sudo apt-get install gnuradio-dev gr-osmosdr airspy cmake g++ git python3-h5py python3-matplotlib python3-yaml
```

For LimeSDR applications, also install `gr-limesdr` and check the receiver's driver requirements.

## Install DSPIRA software

```sh
git clone https://github.com/WVURAIL/dspira-software.git
cd dspira-software
cmake -S . -B build -DPYTHON_EXECUTABLE=/usr/bin/python3
cmake --build build
ctest --test-dir build --output-on-failure
sudo cmake --install build
```

Check that Python can load the installed package:

```sh
python3 -c "from gnuradio import dspira; print(dspira.__file__)"
```

Restart GNU Radio Companion. The installed processing blocks appear in its **DSPIRA** category.
From your `dspira-software` folder, open `applications/spectrometry/calibrated-spectrometer.grc`.
Configure [receiver settings]({{ '/Spectrometer_sourceblock_settings' | relative_url }}) and [recording paths]({{ '/HornOperation_runningSpectrometer' | relative_url }}).

## Update an existing installation

Preserve local receiver settings and customized flowgraphs first.
From your `dspira-software` directory, run:

```sh
git status
git pull --ff-only
cmake -S . -B build -DPYTHON_EXECUTABLE=/usr/bin/python3
cmake --build build
ctest --test-dir build --output-on-failure
sudo cmake --install build
```

If Git reports local changes, review and preserve them before continuing.
Restart GNU Radio Companion after installing updated blocks.
Reopen saved flowgraphs to regenerate their Python code with the current package.

## Older environments

Existing images may contain the former combined `gr-radio_astro` package.
Use the current DSPIRA installation for new GNU Radio 3.10 setups.
The [GNU Radio 3.8 guide]({{ '/gr_radio_astro_Installation_Ubuntu20' | relative_url }}) describes a frozen historical release.

If an import fails, follow the [package troubleshooting notes](https://github.com/WVURAIL/dspira-software/blob/main/docs/block-reference.md).
Test receiver operation and calibration before relying on the setup in class.
