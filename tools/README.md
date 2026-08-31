# tools

## check_links.py

Finds broken links in the lessons before students do.

```bash
python3 tools/check_links.py              # everything, a few minutes
python3 tools/check_links.py --offline    # skip the internet, about a second
```

Run it from the top of the repository. It needs nothing installed — Python 3
standard library only. Results go to `link-report.md`, which is gitignored.

The offline half checks links between lesson pages, heading anchors, and
whether referenced images and PDFs actually exist. That half is where most real
breakage shows up, and it is worth running before any push that touches links.

### Heading anchors

The tables of contents at the head of the labs are nothing but in-page anchors,
and they are the quietest thing on the site: rename a section and every link to
it stops working, while the page still loads and the build still passes. Thirty
of them were dead this way.

The checker now resolves both `[1.6. Exercises](#16-exercises)` and
`{{ site.baseurl }}/dsplab-sdr/#21-introduction` against the ids GitHub Pages
really generates — lowercase, punctuation stripped, `-1`/`-2` on repeats. Those
rules are not a guess: they are kramdown-parser-gfm's, and
`test_check_links.py` pins them against output from the real gems.

```bash
python3 tools/test_check_links.py                          # fixtures + canaries
python3 tools/check_links.py --offline --fail-on anchors    # what CI runs
```

`--fail-on anchors` exits non-zero only for anchors. CI uses it so a build is
never failed by a PDF somebody still owes us, while a broken table of contents
stops the build the moment it is pushed.

If you write a table of contents by hand, or regenerate one with an editor
extension, check the anchors are **lowercase**. Several editor plugins emit
GitHub-style `#11-Installation-Guide`, which looks right and matches nothing —
that is where most of the thirty came from.

Findings are split three ways:

- **Broken** — confirmed dead, worth fixing.
- **Needs a human** — could not be settled automatically. Google Drive, Google
  Docs, YouTube and Mediasite all return "200 OK" for content that has been
  deleted or made private, and some sites refuse automated requests outright.
  These are listed separately rather than guessed at.
- **OK** — responded normally.

Hosts known to sit in that bucket permanently, so nobody re-investigates them:

- `physicsopenlab.org` answers every automated request with 403 regardless of
  user agent. The pages are fine in a browser.
- `home.ifa.hawaii.edu` serves an expired certificate, so the check cannot
  verify it. That one is also flagged on `/labs/`, because a reader clicking it
  gets a browser warning and should know it is expected.
- `indico.phys.vt.edu` and `wiki.analog.com` refuse HEAD, with 400 and 500
  respectively. The checker falls through to GET for any HEAD error, so these
  come back OK; they are listed here only so the next 4xx-on-HEAD host is
  recognised rather than treated as dead.

A link in the middle bucket is not evidence of a problem. If the run cannot
reach the internet at all it says so and falls back to offline mode, rather
than reporting every link as broken.

## check_layout.py

Finds pages that scroll sideways.

```bash
bundle exec jekyll build                    # it reads _site
python3 tools/check_layout.py               # about 15 seconds
python3 tools/check_layout.py --fine        # every page at every width, slower
python3 tools/check_layout.py --self-test   # break a page, check this notices
```

Needs a browser, which is the one thing in `tools/` that is not standard
library:

```bash
pip install playwright && playwright install chromium
```

Horizontal overflow is the quietest layout bug there is. Nothing errors, the
page looks right on the machine it was written on, and on a phone the whole
thing slides an inch to the left when you try to scroll down. It reads as the
site being janky rather than as a fault, so nobody reports it.

Two shipped here, and neither was found by looking at the site:

- A lesson title containing `spectrometer_w_cal.grc`. A heading is set at up to
  3.1rem, and one unbreakable 25-character token is wider than a 320px phone.
  The page leaked 54px, and had since 2020.
- A sixth entry in the navigation. Five fitted; six overflowed by up to 38px —
  but only between **721 and 756px**, in the band just above where the menu
  collapses to a hamburger.

That second one is why the sweep is continuous rather than a handful of device
sizes. A bug that lives between 721 and 756px is invisible to a check that tests
375, 768 and 1280.

Every page is checked at eight common widths; the front page, which carries the
header and footer that appear everywhere, is also swept every 10px from 320 to
1440. `--fine` does that to every page.

For speed it loads each page once and resizes rather than reloading — eight
times faster for the same answer. `--self-test` is what keeps that shortcut
honest: it builds a clean page and a deliberately broken one and checks the
sweep stays quiet for the first and fails on the second. CI runs it before the
real check, the same way `test_check_links.py` runs before the link check.

**What "over" means, and what it does not.** The first version asked whether any
element was wider than its own box. That is the wrong question. An element that
scrolls its own content — a long equation, a wide table in a scroller, a code
block — is wider than its box on purpose and moves the page not at all. The
question is which boxes stick out past the right edge with nothing clipping them,
and that is what is measured and named now: the deepest such element, at the width
it is worst at, with how far past it reaches.

That matters because the old report was confidently wrong. A maths lesson came
back blaming two equations that were scrolling exactly as intended, while the real
offender went unnamed. `--self-test` now includes that shape — wide content in a
scroller next to a genuine 40px offender — and checks the report names the
offender.

**Pages are not finished when they load.** MathJax paints a rough preview and
replaces it with the real equations a few hundred milliseconds later. Measure in
that window and the answer depends on how fast a CDN replied: the same commit
passed and failed, and the failing page is fine at every width once it lands. A
check that answers differently for the same commit is worse than no check, because
it teaches people to re-run it until it goes green.

So a page that looks over is watched for up to two seconds to see whether it comes
back on its own. If it does, that is reported as `settling:` — worth knowing,
since a visitor on a slow connection sees it — but it does not fail the build.
Only overflow that is still there when the page has arrived does.

Waiting for the number to *stop changing* does not work, and `--self-test` has a
case that proves it: between the preview arriving and the equations replacing it,
nothing moves for a comfortable fraction of a second. Holding still is not the
same as being finished.

**A failure worth knowing about.** Both browser checks measure every page on one
shared browser page — far faster than a reload per width. A page that navigates
itself breaks that: a meta-refresh stub does, and so does a load that timed out
while its navigation carried on. The next `goto` then dies with "interrupted by
another navigation", the page stays poisoned, and every page after it fails too.
One flake became thirty-nine failures in CI that way, and the report blamed
thirty-nine innocent pages.

Two guards now. Meta-refresh stubs are detected by reading the file and skipped —
there is no layout on them to measure — and reported rather than dropped
silently. And after any failed load the page is parked at `about:blank`, or
replaced outright if it will not park. Verified by forcing *every* load to fail
on its first attempt: all 79 pages recover on the retry. `--self-test` includes a
redirect stub sorted ahead of other pages, which is the exact shape that failed.

Pages with an accepted overflow are listed in `ALLOW` at the top of the script,
each with a reason. There are two, both exported Jupyter notebooks carrying
their own inlined Bootstrap. Adding to that list is how you silence something —
deliberately, in a place somebody will read.

It only looks for horizontal overflow. It will not tell you whether a page looks
good, and it cannot see overlapping text, poor contrast, or a squashed image.

## check_math.py

Checks that the displayed equations are actually displayed.

```bash
python3 tools/check_math.py               # about a tenth of a second
python3 tools/check_math.py --self-test   # break it on purpose
```

Standard library only, like the link checker.

kramdown treats

```markdown
$$
f(x) = |x|
$$
```

as a displayed equation only when the opening `$$` starts a block — which means a
blank line above it. Write the same three lines directly under the sentence that
introduces them and kramdown reads it all as one paragraph, so the equation
renders **inline**: body size, mid-sentence, where a centred line was meant.

Nothing warns you. The build passes, MathJax renders it happily, the maths is
correct. It is just in the wrong place — and inline maths does not wrap, so on a
phone it takes the page with it. `/dsplab-fourier1/` leaked 211px at 320px
because a triangle-wave definition sat under "The triangular wave is defined as:".
Three equations were like that, and the other two were merely wrong rather than
wide, which is why the layout check alone was not enough to find them.

It also flags a fence with prose immediately *below* it. That one is not a bug
today — the paragraph after a closing fence parses fine. It is how the bug gets
made: every trapped equation here sat under a line of prose that had itself been
written under a closing fence.

Two things it deliberately ignores: `$$` inside a code fence, which is a code
sample, and `$$x(t)$$` inside a sentence, which is inline maths on purpose. Only
a `$$` alone on its line is a fence. Both cases are in `--self-test`, because a
check that cries wolf gets switched off.

## check_contrast.py

Checks that every piece of text meets WCAG AA contrast.

```bash
bundle exec jekyll build
python3 tools/check_contrast.py               # about 13 seconds
python3 tools/check_contrast.py --self-test   # break it on purpose
```

Same browser as `check_layout.py`, so in CI it costs nothing extra.

Contrast cannot be read off the stylesheet. What matters is the pair of colours
that actually meet — a rule sets one, an ancestor four levels up supplies the
background, and a translucent layer in between changes the answer. This measures
the rendered result at 390px and 1280px. Thresholds are WCAG 2.1 AA: 4.5:1 for
body text, 3:1 for large (24px, or 18.66px bold).

It matters here more than on most sites: teachers project these lessons in
classrooms, where a colour that is merely acceptable on a laptop stops being
readable.

**A warning worth keeping.** The first version measured every element with a
text-node child, which includes containers whose visible words are in their
children — those inherit a colour they never paint. It reported 81 of 82 pages
broken, and every one was wrong. Only elements with their own non-whitespace
text are measured now, and `--self-test` includes that exact case so the mistake
cannot come back quietly.

What it found on a correct first run: five colour pairs, all inside the two
exported Jupyter notebooks, all near misses from the default Pygments palette —
comments at 4.25:1, string interpolation at 3.65:1. They are corrected by an
override block near the top of each of those two files, which explains itself.

It does not cover text over images, focus indicators, or anything needing a
pointer or keyboard. One measurable slice, not the whole of accessibility.
