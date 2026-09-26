# Contributing to DSPIRA

Teachers can send a Word document, shared document, or worksheet to rail@wvu.edu.
Start with the [submission guide](https://wvurail.org/dspira/newpost/) and its planning template.
GitHub is optional for lesson authors.

## Repository responsibilities

- `dspira`: lessons, worksheets, teacher guides, small activity code, and website templates.
- `dspira-software`: classroom telescope applications and DSPIRA processing blocks.
- `radio-research-software`: research applications, event detection, and transient experiments.
- `dspira-hardware`: board designs and fabrication files.
- `lightwork`: numbered technical memos.
- `wvurail.github.io`: the lab website.

Link to the authoritative application or hardware download instead of copying it here.
Keep editable lesson originals with the lesson's other assets. Large datasets and
system images need a separate download location, linked from the lesson page.

## Submit a lesson with GitHub

1. Start from `_includes/lesson-template.txt` or the published Markdown template download. Replace every prompt.
2. Save it under `_posts/` as `YYYY-MM-DD-short-name.md`.
3. Set `title`, `summary`, `categories`, `order`, and a permanent `permalink`.
4. Choose exactly one category from `_data/modules.yml`. Use an unused order value in that module.
5. Put worksheets under `assets/worksheets/<lesson-slug>/`, with PDFs beside their editable originals.
   Put guides under `assets/lessons/<lesson-slug>/` and illustrations under `images/<topic>/`.
   Use lowercase filenames with hyphens.
6. Use `{{ '/assets/worksheets/<lesson-slug>/worksheet.pdf' | relative_url }}` for worksheet links.
7. Start section headings at `##`. The layout supplies the page's main heading.
8. Describe images with useful alt text. Keep prose sentences at 20 words or fewer.
9. Include author credit and source information. Preserve existing licenses and quoted material.
10. Open a pull request against `main` and describe the classroom testing performed.

The `main` branch publishes the website after its checks pass.
Use a local preview when reviewing changes. The former approval preview is archived.

## Review and publication

A maintainer checks metadata, links, files, and accessibility structure. An educator
reviews the activity. The author checks a preview before the maintainer publishes it.
Record these reviews in the pull request or submission discussion.

These materials are public. Keep student records and restricted answer keys out of
the repository, issues, attachments, and preview. Teacher-only navigation does not
provide access control.

## Where files belong

Use [the asset directory guide](assets/README.md) before adding a download.
Lecture slides belong in `assets/lessons/lectures/<subject>/`, grouped by course year when known.
Worksheets belong in `assets/worksheets/<lesson-slug>/`, including complete worksheets saved as images.
Figures, screenshots, and photographs belong in `images/<topic>/`.
Guides and background handouts belong in `assets/lessons/<lesson-slug>/`.
GNU Radio applications and flowgraphs belong in `dspira-software`; board designs and amplifier assembly references belong in `dspira-hardware`.
Technical memos belong in `lightwork`. Link to their maintained files instead of uploading another copy.

The former `FilesUploaded` directory is generated during publication for old links.
Add new material to its proper source folder. Record future moves in `_data/legacy_assets.json` when existing public addresses must survive.
Keep each published lesson's `permalink` unchanged when renaming its source file.
Python files under `code/` use lowercase names with underscores; standard project files retain conventional names.

## Prepare the first contribution trial

The template and submission routes are ready. When a teacher is available, use one
real lesson to try the full process. Record where instructions caused confusion,
how much formatting help was needed, and whether the preview matched the author's intent.
No classroom trial is assumed to have happened yet.
