# Repository organization and link maintenance

## Active ownership

| Repository | Responsibility |
| --- | --- |
| dspira | Educational site, lessons, worksheets, teacher guides, small lesson-specific code |
| dspira-software | The seven extracted classroom telescope applications |
| gr-radio_astro | Shared GNU Radio blocks and remaining research applications |
| dspira-hardware | Physical designs and fabrication files; formerly os_radio_astro_hw |
| lightwork | Numbered technical memos |
| wvurail.github.io | Lab website |
| rail-preview | Staging assembly and automated website checks |

The library's main branch retains only a signpost at examples/DSPIRA. The
applications have one maintained home in dspira-software/flowgraphs. Their
extracted directory history and original byte hashes are retained there.
Do not rename the radio_astro Python module or GNU Radio block identifiers:
those are the shared runtime interface, not obsolete repository names.

## Compatibility policy

The public map is generated from `_data/repository_links.json` and available at
`/dspira/repository-map/` and `/dspira/repository-links.json`.

- GitHub redirects os_radio_astro_hw to dspira-hardware. Do not reuse the old name.
- Individual GitHub file moves have no redirect. The map includes replacement
  flowgraph URLs and immutable original commit links.
- dspira-lessons serves compatibility redirects and download assets for the site.
- gr-dspira, gr-transient, cra, and dspira-archive remain historical records.
- Original commit messages, tags, citations, binary documents, and frozen research
  instructions retain historical names. Their continued presence is intentional.
- Ubuntu 20.04 instructions use the preserved gr38 release line. They do not refer
  to the current application directory and must not be rewritten as current installs.

## Audit scope

Reviewed the current text in all 24 organization repositories, plus the DSPIRA
and gr-radio_astro wikis. Production and staging website branches are kept in sync.
Binary attachments were preserved. Search counts below identify repositories that
contained relevant names before the reorganization; they are not broken-link counts.

| Repository | Matching text lines before changes |
| --- | --- |
| dspira | 41 |
| wvurail.github.io | 1 |
| rail-preview | 0 |
| dspira-lessons | 0 |
| dspira-archive | 6 |
| gr-radio_astro | 59 |
| pilot-proxy | 0 |
| RFIsher | 0 |
| kotekan | 0 |
| datatrail-cli | 0 |
| Optimization-of-Radio-Array-Telescopes-to-Search-for-Fast-Radio-Bursts | 0 |
| wvu_beamer_template | 0 |
| dtv-census | 0 |
| DigitalNoiseSource | 0 |
| RadioFisher | 0 |
| Antenna_Test_Files | 0 |
| keysight_network_analyser_control | 0 |
| rawice | 0 |
| os_radio_astro_hw | 6 |
| gr-dspira | 9 |
| rflab_test | 0 |
| gr-transient | 5 |
| cra | 7 |
| lightwork | 2 |

## Teacher workflow

`/newpost/` supplies an email route and two downloadable templates. The GitHub
lesson submission form is optional. The guide covers author credit, editable
originals, tested versions, review, and permanent lesson addresses.
The first teacher trial is prepared but has not been conducted.

## Software validation boundary

The shared library passes its 18 QA tests after extraction. The application
catalog passes structural checks and matches the original seven file hashes.
GNU Radio generation exposed pre-existing compatibility errors; they are listed
in dspira-software/docs/KNOWN_ISSUES.md. No receiver operation was validated here.
