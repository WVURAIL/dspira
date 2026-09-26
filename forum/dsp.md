---
layout: page
title: Digital Signal Processing Forum
permalink: /forum/dsp/
room: dsp
meta_description: "Digital Signal Processing Forum: ask questions and share radio astronomy projects on GitHub Discussions. Find the community room and related DSPIRA lessons."
---
{%- comment -%}
A room of the DSPIRA forum. Its GitHub Discussions category comes from
_data/forum.yml, keyed by `room` above. No comment box may be embedded here —
see forum/index.md for why.
{%- endcomment -%}
{%- assign room = site.data.forum.rooms[page.room] %}
{%- assign url = "https://github.com/" | append: site.data.forum.repo | append: "/discussions/categories/" | append: room.slug %}

Discuss sampling, aliasing, Fourier transforms, filters, windows, and spectrometer processing here. These signal-processing topics apply beyond telescopes. This links to the DSP category in DSPIRA's GitHub discussions. Anyone can read it. Posting requires a free GitHub account.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
