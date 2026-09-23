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

This room is for digital signal processing in general — sampling and aliasing,
the Fourier transform, filters and windows, and how a spectrometer turns samples
into a spectrum — whether or not a telescope is involved. It is the DSP category
of the DSPIRA discussions on GitHub, open for anyone to read and for anyone with
a free GitHub account to post in.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
