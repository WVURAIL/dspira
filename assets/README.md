# File organization guide

Choose a folder by the resource's purpose. Use lowercase names with hyphens for teaching files and images.
Keep printable worksheets beside their editable originals. Link labels on the website should describe the resource in ordinary language.

## Lessons and lectures

The lesson web pages live in [`_posts`](../_posts/) because Jekyll requires that directory.
Their `permalink` fields preserve public addresses independently of source filenames.

[`lessons`](lessons/) holds instructional guides and background handouts:

| Folder | Contents |
| --- | --- |
| [electromagnetic-spectrum](lessons/electromagnetic-spectrum/) | Background introduction to wavelengths and radiation |
| [horn-construction](lessons/horn-construction/) | Horn, can, cradle, stand, and mini-horn construction instructions |
| [simple-spectrometer](lessons/simple-spectrometer/) | Spectrometer construction guide |
| [telescope-setup](lessons/telescope-setup/) | Equipment checklist |
| [two-horn-interferometer](lessons/two-horn-interferometer/) | Setup guide |
| [velocity-curve](lessons/velocity-curve/) | Unit outline and astronomy background handouts |

[`lessons/lectures`](lessons/lectures/) groups lecture slides by subject:

- [astronomy](lessons/lectures/astronomy/): PDF lecture decks and editable institute slides.
- [digital-signal-processing](lessons/lectures/digital-signal-processing/): institute DSP slides and the Fourier project.
- [radio-astronomy](lessons/lectures/radio-astronomy/): the Imaging and Deconvolution lecture.

Files sit directly in each subject folder. Known years go at the end of filenames, such as `dark-matter-2018.pptx`.
The [lecture index](lessons/lectures/README.md) records titles, credits, and available date information.
Do not infer a year for undated material. Original source notices remain with the lecture collection.
The two teaching figures under `images/astronomy/` retain the same original rights and credits.

## Worksheets

[`worksheets`](worksheets/) contains student exercises and their companion answers:

| Folder | Contents |
| --- | --- |
| [simple-spectrometer](worksheets/simple-spectrometer/) | Five paired PDF and Word worksheets |
| [fourier-series](worksheets/fourier-series/) | Printable Fourier activity |
| [electromagnetic-spectrum](worksheets/electromagnetic-spectrum/) | Worksheet and answer key saved as JPEGs |
| [velocity-curve](worksheets/velocity-curve/) | Observation sheets, introductory exercises, and companion answers |

A complete worksheet belongs here even when its original format is an image.
An illustration used within a page belongs in `images/` instead.
Use a matching base name for editable and printable versions, such as `01-simple-waveform.docx` and `01-simple-waveform.pdf`.
Existing public answer keys stay with their worksheets. Keep restricted classroom materials outside this public repository.

## Images and styles

[`images`](../images/) holds illustrations, screenshots, and photographs, grouped by topic.
The DSP lab folders use descriptive names such as `dsp-intro`, `fourier-series`, and `digital-filters`.
I/Q notebook figures live in `images/iq/`. Its separate stylesheet lives in `css/iq-notebook.css`.
The notebook page remains available at `/dspira/iq/`.

`images/branding/` holds logos and the social card; `images/program/` holds program photographs.
`images/modules/` contains module thumbnails, and `images/hero/` contains the homepage photographs and their originals.
Photo and diagram bytes remain unchanged when files move.

## Templates and website files

- [templates](templates/): lesson planning and Markdown templates.
- [js](js/): website behavior.
- [wvu-design-system](wvu-design-system/): the vendored stylesheet, navigation script, and notices.
- [../css](../css/): lesson and notebook styles.
- [../code](../code/): small activity scripts, notebooks, and example data, using lowercase Python naming.

## Files maintained in other projects

- [dspira-software](https://github.com/WVURAIL/dspira-software): telescope applications and GNU Radio flowgraphs.
- [dspira-hardware](https://github.com/WVURAIL/dspira-hardware/tree/main/docs/assembly): amplifier parts guides and component locations.
- [LightWork](https://wvurail.org/lightwork/): technical memos.

Link to those resources instead of committing another copy here.
Keep original author credits, licenses, and editable files with their material.

## Old download addresses

`FilesUploaded`, `assets/teaching`, and the top-level `iq` folder are no longer source directories.
Their old public download and image addresses remain available.
[`_data/legacy_assets.json`](../_data/legacy_assets.json) records former paths and their maintained sources.
[`tools/publish_assets.py`](../tools/publish_assets.py) creates compatibility files after the Jekyll build.
Local aliases follow the current resource. Downloads owned elsewhere use pinned revisions with verified checksums.
Historical software copies and the older memo retain their original bytes through immutable commits.
No retired repository is required.

The publication workflows run this step for DSPIRA and the lab's old lesson addresses.
For a local compatibility check:

```sh
bundle exec jekyll build
python3 tools/test_publish_assets.py
python3 tools/publish_assets.py --site _site
```

Update current links and the compatibility map whenever an existing resource moves.
The former twelve-byte `FilesUploaded/blankfile` placeholder was removed; substantive downloads remain available.
