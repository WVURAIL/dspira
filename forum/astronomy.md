---
layout: page
title: Astronomy Forum
permalink: /forum/astronomy/
room: astronomy
meta_description: "Astronomy Forum: ask questions and share radio astronomy projects on GitHub Discussions. Find the community room and related DSPIRA lessons."
---
{%- comment -%}
A room of the DSPIRA forum. Its GitHub Discussions category comes from
_data/forum.yml, keyed by `room` above. No comment box may be embedded here —
see forum/index.md for why.
{%- endcomment -%}
{%- assign room = site.data.forum.rooms[page.room] %}
{%- assign url = "https://github.com/" | append: site.data.forum.repo | append: "/discussions/categories/" | append: room.slug %}

This room is for the astronomy: the 21 cm line of neutral hydrogen, the
rotation of the Milky Way, what the bumps and shifts in a spectrum mean, and how
to plan an observation that will show them. It is the Astronomy category of the
DSPIRA discussions on GitHub, open for anyone to read and for anyone with a free
GitHub account to post in.

<p>
   <a class="btn btn-wvu-blue" href="{{ url }}">Open the {{ room.category }} discussions on GitHub</a>
</p>

[Back to the DSPIRA forum]({{ '/forum/' | relative_url }})
