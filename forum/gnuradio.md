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

Discuss GNU Radio installation, lesson flowgraphs, and DSPIRA processing blocks here. Get help running a spectrometer on your computer or Raspberry Pi. This links to the GNU Radio category in DSPIRA's GitHub discussions. Anyone can read it. Posting requires a free GitHub account.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
