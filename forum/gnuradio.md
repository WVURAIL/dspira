---
layout: page
title: GNU Radio Forum
permalink: /forum/gnuradio/
room: gnuradio
meta_description: "GNU Radio Forum: ask questions and share radio astronomy projects on GitHub Discussions. Find the community room and related DSPIRA lessons."
---
{%- comment -%}
A room of the DSPIRA forum. Its GitHub Discussions category comes from
_data/forum.yml, keyed by `room` above. No comment box may be embedded here —
see forum/index.md for why.
{%- endcomment -%}
{%- assign room = site.data.forum.rooms[page.room] %}
{%- assign url = "https://github.com/" | append: site.data.forum.repo | append: "/discussions/categories/" | append: room.slug %}

This room is for GNU Radio and the software around it: installing it, the
flowgraphs used in the lessons, the gr-radio_astro blocks, and getting a
spectrometer to run on a particular computer or a Raspberry Pi. It is the GNU
Radio category of the DSPIRA discussions on GitHub, open for anyone to read and
for anyone with a free GitHub account to post in.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
