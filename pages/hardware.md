---
layout: page
title: DSPIRA telescope hardware
permalink: /hardware/
eyebrow: Telescope resources
lead: Find the amplifier design, fabrication files, and classroom construction instructions.
meta_description: "Find DSPIRA telescope hardware designs and amplifier fabrication files. Download schematics, follow construction lessons, and locate the current repository."
---

The physical designs live in `dspira-hardware`. This repository was previously named `os_radio_astro_hw`.
GitHub redirects the former name to the current repository. The design files and their existing names remain unchanged.

## Amplifier design and fabrication

[Download the hardware files as a ZIP](https://github.com/WVURAIL/dspira-hardware/archive/refs/heads/main.zip){: .btn .btn-wvu-blue}

The ZIP includes the readable schematic, editable Altium sources, and board fabrication files.
Use the `HI_amp_v3_gerbers` folder for the existing board revision.

- [Open the amplifier schematic PDF](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/Neutral_Hydrogen_amplifier_v3.pdf).
- Read [amplifier options]({{ '/LNA' | relative_url }}) before selecting a design.
- Follow [the amplifier construction instructions]({{ '/DetailedLNAInstructions' | relative_url }}).
- Review [the parts ordering guide]({{ '/FilesUploaded/LNA_OrderingParts_Info_4.pdf' | relative_url }}).

## Build the telescope

The [Horn Construction module]({{ '/categories/horn-construction/' | relative_url }}) covers the telescope structure.
The [Receiver Electronics module]({{ '/categories/receiver-electronics/' | relative_url }}) introduces the amplifier and receiver.
[LightWork technical memos](/lightwork/) provide additional construction and measurement details.

## Propose a hardware change

Submit board and fabrication changes to [dspira-hardware](https://github.com/WVURAIL/dspira-hardware).
Include the board revision, editable design source, fabrication outputs, and any measurements performed.
Keep older revisions available for people maintaining existing telescopes.

Classroom instructions belong in the [DSPIRA lesson repository](https://github.com/WVURAIL/dspira).
Telescope applications are available through the [software guide]({{ '/software/' | relative_url }}).
The [repository map]({{ '/repository-map/' | relative_url }}) lists current names and older addresses.
