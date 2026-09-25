# Asset directory guide

Keep each resource with the lesson or project that maintains it.
Use lowercase names with hyphens. Keep a worksheet's PDF and editable original together.

## Lesson attachments

| Folder | Contents |
| --- | --- |
| [lessons/simple-spectrometer](lessons/simple-spectrometer/) | Five GNU Radio worksheets in PDF and Word formats, plus the spectrometer guide |
| [lessons/velocity-curve](lessons/velocity-curve/) | Unit outline, background handouts, and dated observation examples |
| [lessons/electromagnetic-spectrum](lessons/electromagnetic-spectrum/) | Introduction, spectrum images, worksheet, and its existing public answer key |
| [lessons/fourier-activity](lessons/fourier-activity/) | Printable Fourier activity |
| [lessons/horn-construction](lessons/horn-construction/) | Horn, can, cradle, stand, and mini-horn construction instructions |
| [lessons/telescope-setup](lessons/telescope-setup/) | Equipment checklist |
| [lessons/two-horn-interferometer](lessons/two-horn-interferometer/) | Setup handout and wiring figures |

Add future lesson files under `assets/lessons/<lesson-slug>/`.
Link with `{{ '/assets/lessons/<lesson-slug>/filename.pdf' | relative_url }}`.
Do not move an existing resource without updating its links and preserving necessary old addresses.

## Shared resources and site files

- [teaching/astronomy-lectures](teaching/astronomy-lectures/): PDF slide decks linked from the astronomy recordings.
- [teaching/2018](teaching/2018/): editable institute slides, with the course year retained.
- [teaching](teaching/): shared teaching figures, lecture references, and source notices.
- [templates](templates/): lesson planning and Markdown templates.
- [js](js/): website behavior.
- [wvu-design-system](wvu-design-system/): the site's vendored stylesheet and its notices.
- [../images](../images/): existing lesson illustrations, module thumbnails, and site branding.

## Files maintained in other projects

- [dspira-software](https://github.com/WVURAIL/dspira-software): telescope applications and GNU Radio flowgraphs.
- [dspira-hardware](https://github.com/WVURAIL/dspira-hardware/tree/main/docs/assembly): amplifier parts guides and component locations.
- [LightWork](https://wvurail.org/lightwork/): the authoritative technical memo collection.

Link to those resources instead of committing another copy here.
Current interferometer downloads use the applications in `dspira-software/flowgraphs`.
The Fourier wave explorer lives in `dspira-software/examples/fourier-wave-explorer`.
The schematic already existed in `dspira-hardware`; its duplicate was removed here.
The memo 31 copy rendered identically to LightWork's copy, which the lessons now reference.

## Old download addresses

`FilesUploaded` is no longer a source directory. Its old public download addresses still work.
[`_data/legacy_assets.json`](../_data/legacy_assets.json) records each former path and its new source.
[`tools/publish_assets.py`](../tools/publish_assets.py) creates compatibility files after the Jekyll build.
Local aliases use the current lesson file. Downloads owned elsewhere use pinned revisions with verified checksums.
The old interferometer copies and memo retain their original bytes through immutable commits in this active repository.
No retired repository is required.

The publication workflows run this step for DSPIRA and the lab's old lesson addresses.
For a local compatibility check, run:

```sh
bundle exec jekyll build
python3 tools/test_publish_assets.py
python3 tools/publish_assets.py --site _site
```

The twelve-byte `FilesUploaded/blankfile` placeholder was removed. All substantive downloads remain available.
