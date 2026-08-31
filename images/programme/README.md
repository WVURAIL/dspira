# Programme photographs

Photographs of DSPIRA classroom work, migrated from the retired `cra`
(Classroom Radio Astronomy) repository in 2026 so they stay available for use
on this site.

| File | Taken | Pixels | Size |
|---|---|---|---|
| `2018-10-16-students-horn-parking-lot.jpg` | 2018-10-16 08:07 | 5312 × 2988 | 4.5 MB |
| `2018-10-16-students-horn-parking-lot-web.jpg` | — | 1600 × 900 | 301 KB |
| `2018-10-24-students-horn-roof.jpg` | 2018-10-24 08:03 | 5312 × 2988 | 3.8 MB |
| `2018-10-24-students-horn-roof-web.jpg` | — | 1600 × 900 | 168 KB |

Both photographs show students with a horn telescope — one in a parking lot,
one on a roof. Dates and dimensions come from EXIF, which is intact in the
full-size files. Neither carries GPS coordinates.

## Which file to use

Use the `-web` version in a lesson page. The full-size file is the archival
original and is far too large to embed:

```markdown
![Students with the horn telescope]({{ site.baseurl }}/images/programme/2018-10-24-students-horn-roof-web.jpg)
```

The `-web` files were generated in 2026 from the originals at 1600 px wide,
JPEG quality 82, progressive. Regenerate at any size from the full-size file
rather than resampling a `-web` file again.

## What came across, and what did not

`cra` held five image blobs for these two photographs:

| `cra` path | Disposition |
|---|---|
| `Files_uploaded/20181024_080339.jpg` | Migrated as `2018-10-24-students-horn-roof.jpg` |
| `Files_uploaded/Students_w_Horn_roof.jpg` | Byte-identical to the above — one copy kept |
| `Files_uploaded/Students_w_Horn_parkinlot.jpg` | Migrated as `2018-10-16-students-horn-parking-lot.jpg` |
| `Students_w_Horn_roof.jpg` (repo root) | Not migrated — see below |
| `Students_w_Horn_parkinlot.jpg` (repo root) | Not migrated — see below |

The two root-level files are not smaller crops or thumbnails. They are the same
frames at the identical 5312 × 2988 resolution, re-saved at a lower JPEG quality
with the EXIF stripped. They hold no pixel, no metadata and no detail that the
originals here do not, so carrying them would add duplicate bytes and an
inferior source for anyone generating a new size later. They remain in the
archived `cra` repository if they are ever wanted.

## Rights

These are photographs of identifiable students. Copyright in the images sits
with the DSPIRA programme, but copyright is not the only right involved:
permission from the people depicted is a separate question from the licence on
this repository, and this file does not record what releases exist. Before
using either photograph in new outward-facing material, check with the DSPIRA
programme leads at WVU.
