---
layout: page
title: DSPIRA teacher downloads and editable materials
permalink: /teaching-resources/
eyebrow: For educators
lead: Adapt existing materials or create your own with WVU DSPIRA templates.
meta_description: "Find DSPIRA classroom materials in one teacher download catalog. Print PDFs or adapt editable Word worksheets, guides, and PowerPoint slides for your class."
---

Choose a topic below to download materials for your class.
Each resource includes a printable PDF and an editable Word or PowerPoint file.
For lesson planning, visit [Teach with DSPIRA]({{ '/teach/' | relative_url }}).

## Create new materials

Start with these templates to keep new lessons consistent with the collection.
Both use the WVU DSPIRA banner, Arial text, and automatic page or slide numbers.

<table>
<caption class="visually-hidden">WVU DSPIRA templates for teachers</caption>
<thead><tr><th scope="col">Use</th><th scope="col">Template</th><th scope="col">Preview</th></tr></thead>
<tbody>
{% for template in site.data.teaching_templates %}
<tr>
<th scope="row">{{ template.title }}</th>
<td><a href="{{ template.editable | relative_url }}" download>{{ template.format }} ({{ template.extension }})</a></td>
<td><a href="{{ template.pdf | relative_url }}" aria-label="Preview the {{ template.title | downcase }} template as PDF">PDF</a></td>
</tr>
{% endfor %}
</tbody>
</table>

The Word template includes lesson sections, a data table, and space for student answers.
The PowerPoint template includes six layouts, from a lesson introduction to data and reflection slides.

1. Download the template and open it in the desktop version of Word or PowerPoint.
2. Save your working copy as a Word document (`.docx`) or PowerPoint presentation (`.pptx`).
3. Replace bracketed prompts and remove unused sections. In PowerPoint, choose **Home > New Slide** for the branded layouts.
4. Keep the heading styles and Arial font. Add image descriptions, source credits, and relevant safety instructions.
5. Check accessibility and page breaks, then export a PDF. Keep the editable file so teachers can adapt your lesson.

Word comments and PowerPoint speaker notes include additional guidance.

## Plan a class

Use the [Velocity Curve unit]({{ '/Astronomy_VelocityCurve_Overview' | relative_url }}) for a complete classroom sequence.
The [astronomy recordings]({{ '/Astronomy_Lecture_Recordings/' | relative_url }}) include thirteen slide decks.
The [DSP recordings]({{ '/dsp' | relative_url }}) connect theory with laboratory exercises.

## Printable and editable materials

Use Word for handouts and worksheets. Use PowerPoint for presentations.

Some diagrams and legacy equations remain images within the editable files.
Print measuring models at actual size; each model lists its paper and scaling instructions.
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

<details class="teaching-downloads" id="amplifier-assembly">
<summary>Amplifier assembly ({{ site.data.hardware_documents | size }})</summary>
<p>Match the guide to your board revision. Circuit drawings retain their original labels and component values.</p>
<table>
<caption class="visually-hidden">Amplifier assembly downloads</caption>
<thead><tr><th scope="col">Resource</th><th scope="col">Print</th><th scope="col">Edit</th></tr></thead>
<tbody>
{% for document in site.data.hardware_documents %}
{% assign source = 'https://raw.githubusercontent.com/WVURAIL/dspira-hardware/main/' | append: document.path %}
<tr>
<th scope="row">{{ document.title }}</th>
<td><a href="{{ source }}.pdf" aria-label="Download {{ document.title | escape }} as PDF">PDF</a></td>
<td><a href="{{ source }}.docx" aria-label="Edit {{ document.title | escape }} in Word">Word</a></td>
</tr>
{% endfor %}
</tbody>
</table>
</details>

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
