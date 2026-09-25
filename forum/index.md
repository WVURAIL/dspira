---
layout: page
title: DSPIRA Forum
permalink: /forum/
lead: >-
  The forum uses GitHub Discussions. Anyone can read the threads, and anyone with a free GitHub account can post.
meta_description: "DSPIRA Forum: ask questions and share radio astronomy projects on GitHub Discussions. Find the community room and related DSPIRA lessons."
---
{%- comment -%}
The rooms come from _data/forum.yml. Nothing forum-like may be served from the
University domain (SCM ruling), so neither this page nor the room pages carry a
comment box any more: they send people to the Discussions categories on
GitHub, which is where the conversations have always been kept. Links to
GitHub say so in their text and open in the same tab.
{%- endcomment -%}
{%- assign discussions = "https://github.com/" | append: site.data.forum.repo | append: "/discussions" %}

Pick the room closest to your question, or browse everything from the button at
the end. The threads go back to 2020.

## The rooms

<ul class="list-unstyled ps-0 row g-4 mb-5">
{%- for pair in site.data.forum.rooms %}
{%- assign room = pair[1] %}
   <li class="col-24 col-md-12 d-flex mb-0">
      <div class="card h-100 w-100 border-0 bg-wvu-not-quite-white">
         <div class="card-body p-4">
            <h3 class="card-title h5 helvetica-neue-bold mb-2">
               <a class="text-wvu-blue" href="{{ discussions }}/categories/{{ room.slug }}">{{ room.category }} discussions on GitHub</a>
            </h3>
            <p class="card-text mb-0">{{ room.blurb }}</p>
         </div>
      </div>
   </li>
{%- endfor %}
</ul>

<p class="mb-0">
   <a class="btn btn-wvu-blue" href="{{ discussions }}">Open the DSPIRA forum on GitHub</a>
</p>
