# NOTICE

`dspira` is an archived repository: the working repository of the DSPIRA summer
institute, an NSF-funded Research Experiences for Teachers programme at the
Lane Department of Computer Science and Electrical Engineering, West Virginia
University, run with the Green Bank Observatory.

The maintained material is at <https://wvurail.org/dspira-lessons/>. See
[`README.md`](README.md) for the redirect table and for what deliberately
stayed here.

## Authorship

Commits run from June 2017 to August 2026: 443 by Pranav Sanghavi, 72 by Kevin
Bandura, and the archival commit by Dylan Gormley.

Commit authorship covers the labs, the flowgraphs and the analysis code. It
does **not** cover the lecture material, which was contributed by its speakers
and committed on their behalf.

## Lecture slides — third-party rights

The decks under `lectures/astronomy/` were presented to the RET cohort. They
are not works of the DSPIRA project, and the MIT licence below does not grant
rights in them. Authorship as recorded in the files themselves:

| File | Author named in the document |
|---|---|
| `DJP_Lectures/RET_0706.pdf` … `RET_0714.pdf` (seven decks) | D.J. Pisano |
| `LDA_Lectures/RET_DSP_MotionOfSky1.pdf` | Loren Anderson |
| `LDA_Lectures/RET_SCP_Time_Planning_Observations.pdf` | Loren Anderson |
| `LDA_Lectures/RET_DSP_Intro.pdf` | Markus Boettcher |
| `LDA_Lectures/RET_DSP_Dark_Matter.pdf` | Mark Voit |
| `LDA_Lectures/RET_DSP_Gravity.pdf` | none recorded |
| `LDA_Lectures/RET_DSP_Rotation_Curves.pdf` | none recorded |

Two of these name authors outside the project, and the two with no author
recorded carry titles matching standard introductory-astronomy chapter
sequences. Treat the `LDA_Lectures` set as compiled teaching material that may
incorporate publisher or third-party figures.

This is the same question the README describes: five decks were held back over
textbook figures and released only once their authors confirmed the figures had
been used with permission. That confirmation concerned the original
presentations. It is not a licence, and it does not transfer to anyone
redistributing or adapting these files. Ask the named author before reusing a
deck.

`labs/06/DSPIRA_Horn_Assembly.pdf`, `labs/06/DSPIRA_memo2_LNA.pdf` and
`archive/DSPIRA_LNA_assembly.pdf` are by Kevin Bandura and are project work.

## Git LFS

Every PDF and slide deck here — `lectures/astronomy/`, parts of
`lectures/2018/`, `labs/06/`, `archive/` — is stored with Git LFS: 28 objects,
about 196 MB. A plain `git clone` gives pointer files a few dozen bytes long.
Run `git lfs pull` to fetch the real ones.

The DSP decks in `lectures/2018/DSP/` are the exception. They were renamed at
some point from `lecture 1.pptx` to `lecture1.pptx`, which stopped them
matching the LFS pattern in `lectures/.gitattributes`, so they are ordinary git
blobs. `linux/cheatsheet.pdf` is an ordinary blob for the reason recorded in
`.gitattributes`.

## Licence

[`LICENSE`](LICENSE) is the MIT License, covering the project's own code, lab
text and flowgraphs. It does not cover the lecture slides described above, nor
third-party figures reproduced inside any document.

Until 2026 the `LICENSE` file held only a two-line fragment ending in an
ellipsis — a licence header rather than a licence. The full MIT text was
restored before archiving. `CITATION.cff` declared MIT throughout, so this
records the intent that was always stated rather than changing it.
