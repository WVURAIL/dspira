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
| [assets/lessons](assets/lessons/) | Lesson guides, background handouts, and construction instructions |
| [assets/lessons/lectures](assets/lessons/lectures/) | Lecture slides grouped by subject, with known years in filenames |
| [assets/worksheets](assets/worksheets/) | Student exercises, answer keys, and editable originals |
| [assets/templates](assets/templates/) | Lesson contribution templates |
| [images](images/) | Figures, screenshots, photographs, and branding, grouped by topic |
| [lesson-examples](lesson-examples/) | Lesson notebooks, sample data, and figure generators |
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
- Telescope applications, GNU Radio flowgraphs, and reusable observation-processing scripts belong in [dspira-software](https://github.com/WVURAIL/dspira-software).
- Board designs and amplifier assembly references belong in [dspira-hardware](https://github.com/WVURAIL/dspira-hardware).
- Technical memos belong in [LightWork](https://github.com/WVURAIL/lightwork).

Link to the maintained resource instead of uploading another copy.
Keep original author credits, licenses, and editable files with the material.

## Add or update a lesson

Teachers can use the [submission guide](https://wvurail.org/dspira/newpost/) without using GitHub.
For repository contributions, follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [lesson template](_includes/lesson-template.txt).

Each lesson needs one module, a position within that module, and a stable public address.
Store worksheets under `assets/worksheets/<lesson-slug>/`, keeping printable PDFs beside their editable originals.
Put instructional guides under `assets/lessons/<lesson-slug>/` and illustrations under `images/<topic>/`.
Use lowercase filenames with hyphens, such as `2026-09-25-horn-calibration.md` or `receiver-settings.png`.
Published lesson addresses are set by `permalink`, independently of source filenames.
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

## Naming conventions

Use lowercase, hyphenated names for lesson sources, web pages, images, and teaching downloads.
Lesson sources retain Jekyll's required `YYYY-MM-DD-` prefix.
Python scripts, notebooks, and their data use lowercase names with underscores under `lesson-examples/`.
Jekyll directories and data keys retain their required underscores.
Standard project files such as `README.md`, `LICENSE`, `CITATION.cff`, and `Gemfile` keep their conventional names.
Preserved source notices and vendored libraries retain their original naming.

## Historical material

The [history page](https://wvurail.org/dspira/history/) links preserved material and recovery ZIPs.
Retired repository snapshots remain separate from current lesson assets.
The [repository map](https://wvurail.org/dspira/repository-map/) explains old names and current ownership.
