---
layout: page
title: DSPIRA historical material and source archives
permalink: /history/
eyebrow: Project history
lead: Find earlier course materials, experimental software, and complete recovery packages for retired repositories.
meta_description: "Explore historical DSPIRA lessons and radio astronomy experiments. Download preserved source files, Git history, and recovery instructions."
---

Start with the [current lessons]({{ '/' | relative_url }}) when planning a class.
The material below records earlier courses and research projects. Historical software may need older tools or unsupported hardware.

## Earlier websites

- [DSPIRA institute materials](https://wvurail.org/dspira/history/sites/dspira-archive/)
- [Classroom Radio Astronomy materials](https://wvurail.org/dspira/history/sites/cra/)
- [Radio transient experiments](https://wvurail.org/dspira/history/sites/gr-transient/)

Old website pages redirect to these preserved copies. Existing worksheet and data download addresses remain available.
The main lab site maintains those addresses. The retired repositories no longer publish the websites.

## Complete recovery packages

Each ZIP includes source files, Git history, branches, tags, and restoration instructions.
The institute package also includes its wiki and historical large-file objects. Public issue and review records are included where available.
Original licenses and author credits remain with the files.

{% assign release = 'https://github.com/WVURAIL/dspira/releases/download/preserved-repositories-2026-09-25/' %}
<div class="table-responsive">
<table class="table">
<caption>Repository snapshots preserved on September 25, 2026</caption>
<thead><tr><th scope="col">Repository</th><th scope="col">Source files</th><th scope="col">Recovery download</th></tr></thead>
<tbody>
{% for archive in site.data.preserved_repositories.repositories %}
<tr><td>{{ archive.repository | remove: 'WVURAIL/' }}</td><td>{{ archive.files }}</td><td><a href="{{ release }}{{ archive.package }}">Download {{ archive.repository | remove: 'WVURAIL/' }} ZIP</a></td></tr>
{% endfor %}
</tbody>
</table>
</div>

The packages preserve original file contents, including material absent from the maintained projects.
Recovery checks verified the Git bundles, source hashes, and large-file contents.
See the [release and verification records](https://github.com/WVURAIL/dspira/releases/tag/preserved-repositories-2026-09-25) for checksums and source commits.

## Finding current resources

Use the [repository map]({{ '/repository-map/' | relative_url }}) to find maintained projects.
The [software guide]({{ '/software/' | relative_url }}) covers classroom applications and shared GNU Radio blocks.
The [hardware guide]({{ '/hardware/' | relative_url }}) covers telescope construction and circuit designs.

GitHub repository links differ from website addresses. Deleting an original repository would remove its GitHub browsing and discussion URLs.
The recovery packages preserve their records, but cannot preserve those GitHub addresses.
