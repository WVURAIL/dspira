---
layout: page
title: DSPIRA historical material
permalink: /history/
eyebrow: Project history
lead: Browse earlier radio astronomy experiments, original files, and lab images.
meta_description: "Explore earlier DSPIRA radio astronomy experiments and lab images. Download original experiment files with source records and author credits."
---

Useful course materials now have active homes. Browse [teaching downloads]({{ '/teaching-resources/' | relative_url }}) and [research examples]({{ '/research-examples/' | relative_url }}).

Start with the [current lessons]({{ '/' | relative_url }}) when planning a class.
The material below records earlier courses and research projects. Historical software may need older tools or unsupported hardware.

## Earlier experiments

Browse the [historical experiment catalog]({{ '/history/experiments/' | relative_url }}) for older receiver configurations, audio demonstrations, pulsar notebooks, and diagnostic figures. Each entry offers a direct download from this website; one ZIP also contains all 53 distinct files and their provenance. Current applications remain linked separately.

## Earlier lab images

These photographs, diagrams, and project graphics appeared on earlier versions of the lab website. For current projects, see [research and telescopes](https://rail.wvu.edu/where-we-work/).

<ul>
{% for image in site.data.historical_lab_images %}
<li><a href="{{ image.download_path | relative_url }}">{{ image.title | escape }}</a> &middot; <a href="{{ image.source_url }}">Source record</a></li>
{% endfor %}
</ul>

## Finding current resources

Use the [repository map]({{ '/repository-map/' | relative_url }}) to find maintained projects.
The [software guide]({{ '/software/' | relative_url }}) covers classroom applications and DSPIRA processing blocks.
The [hardware guide]({{ '/hardware/' | relative_url }}) covers telescope construction and circuit designs.
