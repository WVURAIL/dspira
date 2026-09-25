---
layout: page
title: Build and maintain telescope hardware
permalink: /hardware/
meta_description: "Build or maintain a DSPIRA radio telescope. Compare amplifier options, follow construction guides, and download schematics and fabrication files."
lead: Choose your parts, follow the construction guides, or find the design files for your board.
---

## Build your first telescope

Start with [the complete parts overview]({{ '/BuildingHornTelescope_Overview' | relative_url }}).
The [Horn Construction module]({{ '/categories/horn-construction/' | relative_url }}) covers the antenna and stand.
[Receiver Electronics]({{ '/categories/receiver-electronics/' | relative_url }}) connects the amplifier, receiver, and computer.

## Choose an amplifier

Compare [amplifier options]({{ '/LNA' | relative_url }}) before ordering parts.
You can build the DSPIRA amplifier or choose a listed ready-made option.

- [Build the DSPIRA amplifier]({{ '/DetailedLNAInstructions' | relative_url }}).
- [Review the parts ordering guide (PDF)]({{ '/FilesUploaded/LNA_OrderingParts_Info_4.pdf' | relative_url }}).
- [Ask about a starter kit]({{ '/kits/' | relative_url }}).

## Maintain or fabricate a board

Match the schematic and fabrication files to your board revision before making changes.
The download includes a readable schematic, editable Altium sources, and fabrication files.
Use `HI_amp_v3_gerbers` for the existing version 3 board.

[Open the version 3 schematic (PDF)](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/Neutral_Hydrogen_amplifier_v3.pdf)

[Download hardware design files (ZIP)](https://github.com/WVURAIL/dspira-hardware/archive/refs/heads/main.zip){: .btn .btn-wvu-blue}

[LightWork technical guides](/lightwork/) provide additional construction and measurement references.

<details markdown="1">
<summary>Earlier amplifier design notes</summary>

These institute documents explain earlier choices. Component values, bias settings, and prices may differ from your board.

- [Amplifier assembly notes (PDF)](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/docs/institute/lna-assembly.pdf)
- [June 2018 assembly guide (PDF)](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/docs/institute/lna-assembly-2018-06-22.pdf)
- [2017 design and measurements (PDF)](https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/docs/institute/lna-design-memo-2017.pdf)

Use the current construction lesson for classroom assembly.
</details>

## Propose a change

Submit board changes to [dspira-hardware](https://github.com/WVURAIL/dspira-hardware).
Include the board revision, editable sources, fabrication outputs, and measurements.
Use the [contribution guide]({{ '/newpost/' | relative_url }}) for classroom instructions.

The [repository map]({{ '/repository-map/' | relative_url }}) explains previous names.
The [software guide]({{ '/software/' | relative_url }}) covers telescope applications.
