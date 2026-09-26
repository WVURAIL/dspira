---
layout: page
title: DSPIRA teaching downloads and lecture slides
permalink: /teaching-resources/
eyebrow: For educators
lead: Print classroom materials or adapt the editable versions for your students.
meta_description: "Download DSPIRA teaching slides and classroom resources. Find astronomy presentations, DSP exercises, observation planning notes, and technical references."
---

Find lecture slides, classroom handouts, and DSP exercises here.
Each download opens directly from the site or its owning software repository.

## Plan a class

Use the [Velocity Curve unit]({{ '/Astronomy_VelocityCurve_Overview' | relative_url }}) for a complete classroom sequence.
The [astronomy recordings]({{ '/Astronomy_Lecture_Recordings/' | relative_url }}) include thirteen slide decks.
The [DSP recordings]({{ '/dsp' | relative_url }}) connect theory with laboratory exercises.

## Printable and editable materials

Every teaching download below includes a PDF and an editable companion.
Use Word for handouts and worksheets. Use PowerPoint for presentations.
Both versions share WVU DSPIRA headers, consistent fonts, and page numbers.

Some diagrams and legacy equations remain images within the editable files.
Keep author credits and check third-party permissions when adapting materials.
<p id="2018-institute-slide-decks">Dates identify source editions; older decks may differ from later recordings.</p>

{% for group in site.data.teaching_documents %}
{% case group.title %}
{% when 'Simple spectrometer' %}<details class="teaching-downloads" id="editable-gnu-radio-worksheets">
{% when 'Astronomy lecture slides' %}<details class="teaching-downloads" id="astronomy-slides">
{% when 'Digital signal processing slides' %}<details class="teaching-downloads" id="dsp-slides">
{% when 'Radio astronomy slides' %}<details class="teaching-downloads" id="radio-astronomy-lecture">
{% else %}<details class="teaching-downloads" id="{{ group.title | slugify }}">
{% endcase %}
<summary>{{ group.title }} ({{ group.documents | size }})</summary>
<table>
<caption class="visually-hidden">{{ group.title }} downloads</caption>
<thead><tr><th scope="col">Resource</th><th scope="col">Print</th><th scope="col">Edit</th></tr></thead>
<tbody>
{% for document in group.documents %}
<tr>
<th scope="row">{{ document.title }}</th>
<td><a href="{{ document.pdf | relative_url }}" aria-label="Download {{ document.title | escape }} as PDF">PDF</a></td>
<td><a href="{{ document.editable | relative_url }}" aria-label="Edit {{ document.title | escape }} in {{ document.format }}">{{ document.format }}</a></td>
</tr>
{% endfor %}
</tbody>
</table>
</details>
{% endfor %}

## Additional teaching figures

- [Frequency and radial velocity figure (PDF)]({{ '/images/astronomy/frequency-versus-radial-velocity.pdf' | relative_url }})
- [Galactic rotation figure (PDF)]({{ '/images/astronomy/galactic-rotation.pdf' | relative_url }})

## Practice with signals

[Browse 29 DSP flowgraph exercises]({{ '/dsp-examples/' | relative_url }}).
Choose examples covering signal displays, sampling, Fourier analysis, and filters.
The catalog identifies examples that still need compatibility updates.

## Prepare an observation

Bring the horn and can assembly, a stable mount, amplifier, SMA cable, receiver, USB cable, and configured computer.
Check power, connections, storage space, pointing information, and your observing plan before leaving.
Follow the [telescope setup lesson]({{ '/Telescope_Setup' | relative_url }}) and [calibration instructions]({{ '/HornOperation_Calibration' | relative_url }}).
Record the target, time, pointing, receiver settings, and calibration conditions with your observations.

Find circuit design notes in the [hardware guide]({{ '/hardware/' | relative_url }}).
Use [transient research examples]({{ '/research-examples/' | relative_url }}) for advanced simulation work.
