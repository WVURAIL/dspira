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

Discuss amplifiers, filters, SDRs, cables, connectors, and power here. This room covers receiver electronics and their noise and gain requirements. This links to the Electronics category in DSPIRA's GitHub discussions. Anyone can read it. Posting requires a free GitHub account.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
