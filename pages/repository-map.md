---
layout: page
title: DSPIRA repository map
permalink: /repository-map/
eyebrow: Project organization
lead: Find the current home for lessons, applications, research software, hardware, and historical material.
meta_description: "Find current DSPIRA repositories and replacement links. See where classroom software, research software, hardware designs, and lessons are maintained."
---

Start with the DSPIRA website for lessons and downloads. Contributors can use this map to find the right source repository.

## Current projects

| Repository | What belongs there |
| --- | --- |
| [dspira](https://github.com/WVURAIL/dspira) | Lessons, worksheets, teacher guides, and the educational website |
| [dspira-software](https://github.com/WVURAIL/dspira-software) | Classroom applications and all DSPIRA processing blocks |
| [radio-research-software](https://github.com/WVURAIL/radio-research-software) | Research acquisition, event detection, and transient experiments |
| [dspira-hardware](https://github.com/WVURAIL/dspira-hardware) | Schematics, board layouts, and fabrication files |
| [lightwork](https://github.com/WVURAIL/lightwork) | Numbered technical memos |
| [wvurail.github.io](https://github.com/WVURAIL/wvurail.github.io) | Lab people, research, publications, and contact information |

Install classroom applications and their blocks together from `dspira-software`.
Research applications have a separate home in `radio-research-software`.

## Older names and links

GitHub redirects the former hardware name and `gr-radio_astro` repository name. Keep those old names unused so the redirects continue working.
Moved GitHub files cannot redirect individually. Use their replacement links below or the original commit links in the downloadable map.

The retired repositories contain forwarding notices. Their files and history are preserved through the active DSPIRA project.
The lab site handles their old website addresses. See [historical material and recovery packages]({{ '/history/' | relative_url }}).

[Download the link map as JSON]({{ '/repository-links.json' | relative_url }}).

<details>
<summary>Find replacement links for older addresses</summary>
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
</details>

## Contribute in the right place

Use the [lesson contribution guide]({{ '/newpost/' | relative_url }}) for classroom materials.
Use the [software guide]({{ '/software/' | relative_url }}) and [hardware guide]({{ '/hardware/' | relative_url }}) for telescope resources.
