---
layout: page
title: Notebook Examples
permalink: /notebooks/
eyebrow: Worked examples
lead: Read Python examples, explore their plots, and download notebooks to try yourself.
meta_description: "Read DSPIRA notebook examples for radio astronomy, I/Q sampling, interferometry, and pulsar simulations. Download notebooks and available sample data."
---

These pages show each notebook's explanations, code, and available results.
You can read them without installing Python or opening GitHub.
Each page also includes a notebook download and notes about running it.

{% assign groups = 'Teaching examples,Research examples' | split: ',' %}
{% for group in groups %}
<h2>{{ group }}</h2>
<ul>
{% for example in site.data.notebooks %}{% if example.group == group %}
<li><a href="{{ example.url | relative_url }}">{{ example.title }}</a> - {{ example.summary }}</li>
{% endif %}{% endfor %}
</ul>
{% endfor %}

Some research examples lack saved outputs or require unavailable data. Their pages explain these limits before the code.
