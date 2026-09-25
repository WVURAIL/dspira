---
layout: page
title: DSPIRA repository map
permalink: /repository-map/
eyebrow: Project organization
lead: Find the current home for lessons, applications, shared software, hardware, and historical material.
meta_description: "Find current DSPIRA repositories and replacement links. See where classroom software, shared GNU Radio blocks, hardware designs, and lessons are maintained."
---

Start with the DSPIRA website for lessons and downloads. Contributors can use this map to find the right source repository.

## Current projects

| Repository | What belongs there |
| --- | --- |
| [dspira](https://github.com/WVURAIL/dspira) | Lessons, worksheets, teacher guides, and the educational website |
| [dspira-software](https://github.com/WVURAIL/dspira-software) | Classroom telescope applications |
| [gr-radio_astro](https://github.com/WVURAIL/gr-radio_astro) | Shared GNU Radio blocks and other astronomy applications |
| [dspira-hardware](https://github.com/WVURAIL/dspira-hardware) | Schematics, board layouts, and fabrication files |
| [lightwork](https://github.com/WVURAIL/lightwork) | Numbered technical memos |
| [wvurail.github.io](https://github.com/WVURAIL/wvurail.github.io) | Lab people, research, publications, and contact information |

The classroom applications use the shared blocks without copying them.
The historical DSPIRA application folder now points to the new software repository.

## Older names and links

GitHub redirects the former hardware repository name. Keep that old name unused so the redirect continues working.
Moved GitHub files cannot redirect individually. Use their replacement links below or the original commit links in the downloadable map.

The archived `gr-dspira`, `gr-transient`, `cra`, and `dspira-archive` repositories retain historical material.
They are not places for new classroom contributions. `dspira-lessons` preserves older website addresses and downloads.

[Download the link map as JSON]({{ '/repository-links.json' | relative_url }}).

<div class="table-responsive">
<table class="table">
<caption>Previous addresses and their current destinations</caption>
<thead><tr><th scope="col">Previous address</th><th scope="col">Current destination</th><th scope="col">Handling</th></tr></thead>
<tbody>
{% for entry in site.data.repository_links %}
<tr><td><code class="text-break">{{ entry.old | remove: 'https://' }}</code></td><td><a href="{{ entry.new }}">{{ entry.new | remove: 'https://' }}</a></td><td>{{ entry.behavior }}</td></tr>
{% endfor %}
</tbody>
</table>
</div>

## Contribute in the right place

Use the [lesson contribution guide]({{ '/newpost/' | relative_url }}) for classroom materials.
Use the [software guide]({{ '/software/' | relative_url }}) and [hardware guide]({{ '/hardware/' | relative_url }}) for telescope resources.
