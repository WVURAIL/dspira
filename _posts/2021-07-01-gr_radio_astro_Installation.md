---
layout: post
date:  2021-07-01
title: Installing gr-radio_astro
summary:  Details for installing gr-radio_astro
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 7
meta_description: "Install the DSPIRA gr-radio_astro blocks for GNU Radio. Follow the repository setup and update steps to prepare your telescope software."
equipment: "A computer with GNU Radio, Git, build tools, and the dependencies listed in the installation steps."
preparation: "Install GNU Radio first. Check its version before choosing the shared-library branch, then obtain the separate classroom applications."
---

The shared `gr-radio_astro` library supplies GNU Radio blocks. Classroom applications now come from `dspira-software`.
Install the library first, then download the applications separately.

These instructions target GNU Radio 3.10 on Ubuntu. For an older installation, see the
[Ubuntu 20.04 and GNU Radio 3.8 guide]({{ '/gr_radio_astro_Installation_Ubuntu20' | relative_url }}).

## Install the shared library

Follow the [current library build instructions](https://github.com/WVURAIL/gr-radio_astro#installing-from-source)
to install GNU Radio, receiver drivers, and build dependencies.
Clone and build the shared library:

```sh
git clone https://github.com/WVURAIL/gr-radio_astro.git
cd gr-radio_astro
cmake -S . -B build
cmake --build build
sudo cmake --install build
```

Check the repository's Python environment instructions if GNU Radio cannot find the installed blocks.

## Get the DSPIRA applications

Use the [software download page]({{ '/software/' | relative_url }}) or clone the application repository from your home directory:

```sh
cd
git clone https://github.com/WVURAIL/dspira-software.git
```

Open `dspira-software/flowgraphs/spectrometer_w_cal.grc` in GNU Radio Companion.
The file no longer lives in `gr-radio_astro/examples/DSPIRA/`.
Review the [known compatibility findings](https://github.com/WVURAIL/dspira-software/blob/main/docs/KNOWN_ISSUES.md)
before attempting to run it. Configure your receiver, output folders, and calibration settings.

## Update the applications

Keep a separate copy of any local receiver settings or customized flowgraphs before updating.
From the application checkout, run:

```sh
git status
git pull --ff-only
```

If Git reports local changes, review and preserve them before continuing.
Application updates do not require rebuilding the shared library.

## Update the shared library

From the `gr-radio_astro` checkout, review local changes and pull the update:

```sh
git status
git pull --ff-only
cmake -S . -B build
cmake --build build
sudo cmake --install build
```

Close and reopen GNU Radio Companion after installing updated blocks.
Test the application with your equipment before relying on it in class.
