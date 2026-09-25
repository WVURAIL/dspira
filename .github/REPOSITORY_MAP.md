# Repository organization and link maintenance

## Active ownership

| Repository | Responsibility |
| --- | --- |
| dspira | Educational site, lessons, worksheets, teacher guides, small lesson-specific code |
| dspira-software | Seven classroom telescope applications and twelve DSPIRA processing blocks |
| radio-research-software | Research acquisition, event detection, and transient experiments; formerly gr-radio_astro |
| dspira-hardware | Physical designs and fabrication files; formerly os_radio_astro_hw |
| lightwork | Numbered technical memos |
| wvurail.github.io | Lab website |
| rail-preview | Archived approval preview; build tools now belong to wvurail.github.io |

DSPIRA applications and blocks have one maintained home in dspira-software.
Migration manifests there record original paths and byte hashes.
DSPIRA installs `gnuradio.dspira`; research retains `gnuradio.radio_astro`.
Existing GRC identifiers are preserved so saved flowgraphs can be reopened.
Regenerate saved flowgraphs after installing the new DSPIRA package.

## Compatibility policy

The public map is generated from `_data/repository_links.json` and available at
`/dspira/repository-map/` and `/dspira/repository-links.json`.

- GitHub redirects os_radio_astro_hw to dspira-hardware. Do not reuse the old name.
- GitHub redirects gr-radio_astro to radio-research-software. Keep that old name unused too.
- Individual GitHub file moves have no redirect. The map includes replacement
  flowgraph URLs and immutable original commit links.
- wvurail.github.io serves the old dspira-lessons, dspira-archive, cra, and gr-transient website paths.
- The retired repositories contain forwarding notices. Their recovery packages live in a DSPIRA release.
- See ARCHIVE_RETIREMENT.md for restoration, hosting ownership, and deletion limits.
- Original commit messages, tags, citations, binary documents, and frozen research
  instructions retain historical names. Their continued presence is intentional.
- Ubuntu 20.04 instructions use the preserved gr38 release line. They do not refer
  to the current application directory and must not be rewritten as current installs.

## Audit scope

The original audit reviewed text in all 24 organization repositories, plus the DSPIRA
and gr-radio_astro wikis. The approval preview has since been archived.
Active websites publish from main; their shared build tools belong to wvurail.github.io.
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

The remaining research package passes nine QA tests.
DSPIRA's moved implementations retain their original bytes and file notices.
All seven applications generate and pass syntax checks using the DSPIRA package alone.
Block checks cover exports, averaging, and single-vector calibration and CSV capture.
See dspira-software/docs/KNOWN_ISSUES.md for compatibility results and remaining hardware checks.
