---
layout: page
title: Electronics Forum
permalink: /forum/electronics/
room: electronics
meta_description: "Electronics Forum: ask questions and share radio astronomy projects on GitHub Discussions. Find the community room and related DSPIRA lessons."
---
{%- comment -%}
A room of the DSPIRA forum. Its GitHub Discussions category comes from
_data/forum.yml, keyed by `room` above. No comment box may be embedded here —
see forum/index.md for why.
{%- endcomment -%}
{%- assign room = site.data.forum.rooms[page.room] %}
{%- assign url = "https://github.com/" | append: site.data.forum.repo | append: "/discussions/categories/" | append: room.slug %}

This room is for the electronics between the horn and the computer: low-noise
amplifiers, filters, the software-defined radio, cables, connectors and power,
and the noise and gain questions that come with them. It is the Electronics
category of the DSPIRA discussions on GitHub, open for anyone to read and for
anyone with a free GitHub account to post in.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
