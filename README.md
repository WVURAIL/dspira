# DSPIRA lessons

Lessons and classroom resources for Digital Signal Processing in Radio Astronomy.
Visit the [DSPIRA website](https://wvurail.org/dspira/) for teaching materials and downloads.
Start with [CONTRIBUTING.md](CONTRIBUTING.md) to suggest changes or submit a lesson.

The approved site publishes from `main`. The former approval preview is archived.
A future move to `rail.wvu.edu` follows the [lab's cutover checklist](https://github.com/WVURAIL/wvurail.github.io/blob/main/.github/CUTOVER.md).

## Find the right files

| Path | Purpose |
| --- | --- |
| [_posts](_posts/) | Individual lesson pages |
| [assets/lessons](assets/lessons/) | Worksheets, editable originals, construction guides, and lesson attachments |
| [assets/teaching](assets/teaching/) | Shared lecture slides and teaching references |
| [assets/templates](assets/templates/) | Lesson contribution templates |
| [images](images/) | Existing lesson figures, module thumbnails, and site illustrations |
| [code](code/) | Small activity scripts and observation analysis examples |
| [pages](pages/) | Teaching, installation, hardware, history, and contribution guides |
| [categories](categories/) | Module introduction pages |
| [_data](_data/) | Navigation, module definitions, resource catalogs, and compatibility maps |
| [_layouts](_layouts/), [_includes](_includes/) | Shared page templates and common elements |
| [css](css/), [assets/js](assets/js/) | Site styles and behavior |
| [tools](tools/) | Build helpers and link, layout, math, and contrast checks |
| [.github](.github/) | Publishing workflows, issue templates, and migration records |

The [asset directory guide](assets/README.md) lists the attachment folders and explains old download addresses.
`FilesUploaded` has been replaced by folders grouped by lesson or topic.

## Keep each resource in one project

- Lesson pages, worksheets, and teacher materials belong here.
- Telescope applications and GNU Radio flowgraphs belong in [dspira-software](https://github.com/WVURAIL/dspira-software).
- Board designs and amplifier assembly references belong in [dspira-hardware](https://github.com/WVURAIL/dspira-hardware).
- Technical memos belong in [LightWork](https://github.com/WVURAIL/lightwork).

Link to the maintained resource instead of uploading another copy.
Keep original author credits, licenses, and editable files with the material.

## Add or update a lesson

Teachers can use the [submission guide](https://wvurail.org/dspira/newpost/) without using GitHub.
For repository contributions, follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [lesson template](_includes/lesson-template.txt).

Each lesson needs one module, a position within that module, and a stable public address.
Store its attachments together under `assets/lessons/<lesson-slug>/`.
Keep printable PDFs beside their editable originals, and give new files lowercase names with hyphens.
Start body headings at `##`; the layout supplies the page title.

All published material is public. Keep student records and restricted answer keys in your school's classroom system.

## Preview and validation

The site uses the GitHub Pages gem and Jekyll. For a local preview:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/dspira/`.
For old download addresses, also follow the [compatibility build instructions](assets/README.md#old-download-addresses).
See [the tools guide](tools/README.md) for checks run by CI.

The WVU Design System stylesheet is vendored under `assets/wvu-design-system`.
Page layouts use the common masthead, footer, and contact settings from `_config.yml`.
Site publishing trims unused stylesheet rules and checks the resulting pages.

## Historical material

The [history page](https://wvurail.org/dspira/history/) links preserved material and recovery ZIPs.
Retired repository snapshots remain separate from current lesson assets.
The [repository map](https://wvurail.org/dspira/repository-map/) explains old names and current ownership.
