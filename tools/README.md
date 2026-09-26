# tools

## check_links.py

Finds broken links in the lessons before students do.

```bash
python3 tools/check_links.py              # everything, a few minutes
python3 tools/check_links.py --offline    # skip the internet, about a second
```

Run it from the top of the repository. It needs nothing installed — Python 3
standard library only. Results go to `link-report.md`, which is gitignored.

Full URLs pointing to this site's `/dspira/` pages are checked locally instead of fetched. The script defines its own host name. Update it during the rail.wvu.edu migration, as described in the lab repository's `.github/CUTOVER.md`.

The offline half checks links between lesson pages, heading anchors, and
whether referenced images and PDFs actually exist. That half is where most real
breakage shows up, and it is worth running before any push that touches links.

### Heading anchors

Lab tables of contents use page anchors. Renaming a section can break those links even when the page loads and its build succeeds. Thirty
of them were dead this way.

The checker resolves anchors such as `[1.6. Exercises](#16-exercises)` and `{{ site.baseurl }}/dsplab-sdr/#21-introduction`.
GitHub Pages generates lowercase IDs with punctuation removed and `-1`/`-2` suffixes for duplicates. These rules come from kramdown-parser-gfm. `test_check_links.py` verifies them against output from the actual gems.

```bash
python3 tools/test_check_links.py                          # fixtures + canaries
python3 tools/check_links.py --offline --fail-on anchors    # what CI runs
```

`--fail-on anchors` exits non-zero only for anchors. CI uses it to tolerate missing external PDFs. Broken table-of-contents links still fail the build immediately.

When writing or regenerating a table of contents, make its anchors **lowercase**. Some editor plugins produce anchors such as `#11-Installation-Guide`. They look plausible but match nothing here. Most of the thirty failures came from these anchors.

Findings are split three ways:

- **Broken** — confirmed dead, worth fixing.
- **Needs a human** — could not be settled automatically. Google Drive, Google Docs, YouTube, and Mediasite may return "200 OK" for deleted or private content. Other sites reject automated requests.
  These are listed separately rather than guessed at.
- **OK** — responded normally.

Hosts known to sit in that bucket permanently, so nobody re-investigates them:

- `physicsopenlab.org` answers every automated request with 403 regardless of
  user agent. The pages are fine in a browser.
- `home.ifa.hawaii.edu` serves an expired certificate, so the check cannot
  verify it. The `/labs/` page also flags that link. Readers receive a browser warning, so the page explains that behavior.
- `indico.phys.vt.edu` and `wiki.analog.com` refuse HEAD, with 400 and 500
  respectively. The checker retries HEAD errors with GET, so these links pass. This list helps identify similar hosts that reject HEAD requests.

A link in the middle bucket is not evidence of a problem. If internet access fails entirely, the checker reports that limitation and switches to offline mode. It avoids marking every external link broken.

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

Internet access is required for fonts from use.typekit.net. Design System CSS
is served locally. Both this check and `check_contrast.py` need the fonts loaded
to measure the rendered page correctly.

Horizontal overflow is the quietest layout bug there is. The author's computer shows no error. On a phone, however, scrolling down moves the whole page sideways. It reads as the
site being janky rather than as a fault, so nobody reports it.

Two shipped here, and neither was found by looking at the site:

- A lesson title containing `spectrometer_w_cal.grc`. Headings can reach 3.1rem. One unbreakable 25-character word can exceed a 320px phone's width.
  The page leaked 54px, and had since 2020.
- A sixth entry in the navigation. Five navigation items fit; six overflowed by up to 38px. This happened only between **721 and 756px**, just above the mobile-menu breakpoint.

That second one is why the sweep is continuous rather than a handful of device
sizes. A bug that lives between 721 and 756px is invisible to a check that tests
375, 768 and 1280.

Every page is checked at eight common widths. The front page also tests the shared header and footer every 10px from 320 to
1440. `--fine` does that to every page.

Loading each page once and resizing is eight times faster than reloading. `--self-test` verifies this shortcut using clean and deliberately broken pages. The clean page must pass, and the broken page must fail. CI runs it before the
real check, the same way `test_check_links.py` runs before the link check.

**What "over" means, and what it does not.** The first version asked whether any
element was wider than its own box. That is the wrong question. Some elements intentionally scroll their own content, such as equations, wide tables, and code blocks. They can exceed their containers without moving the page. The checker identifies unclipped boxes extending beyond the page's right edge. It reports the deepest offending element, its worst viewport width, and the overflow distance.

That matters because the old report was confidently wrong. An earlier report blamed two correctly scrolling equations and missed the actual cause. `--self-test` now includes scrolling content beside a genuine 40px overflow. It verifies that the report identifies the real problem.

**Pages are not finished when they load.** MathJax paints a rough preview and
replaces it with the real equations a few hundred milliseconds later. Measuring during that interval made results depend on CDN response time. The same commit passed and failed. Once loading finished, the page fit every tested width. Inconsistent results encourage repeated runs until a check passes. Such a check provides little protection.

The checker watches apparent overflow for up to two seconds to see whether it resolves itself. Resolved overflow is reported as `settling:` without failing the build. Visitors on slow connections may still see that temporary state.
Only overflow that is still there when the page has arrived does.

Waiting for a stable measurement is insufficient. Preview content can remain still briefly before equations replace it. `--self-test` covers this case. Holding still is not the
same as being finished.

**A failure worth knowing about.** Both browser checks measure every page on one
shared browser page — far faster than a reload per width. Automatic navigation breaks that approach. Examples include meta-refresh redirects and page loads whose navigation continues after a timeout. The next `goto` fails with "interrupted by another navigation". The browser page remains unusable, causing subsequent checks to fail.
One flake became thirty-nine failures in CI that way, and the report blamed
thirty-nine innocent pages.

Two guards now. The checker detects meta-refresh stubs from their files and reports them as skipped. These stubs have no layout to measure. And after any failed load the page is parked at `about:blank`, or
replaced outright if it will not park. Forcing every first load to fail verified retry recovery on all 79 pages. `--self-test` includes a redirect stub before other pages, reproducing the original failure.

Pages with an accepted overflow are listed in `ALLOW` at the top of the script,
each with a reason. There are two, both exported Jupyter notebooks carrying
their own inlined Bootstrap. Adding to that list is how you silence something —
deliberately, in a place somebody will read.

It only looks for horizontal overflow. It cannot assess appearance or detect overlapping text, poor contrast, and distorted images.

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
blank line above it. Without a blank line after the introduction, kramdown treats those three lines as part of the paragraph. The equation renders **inline** at body size instead of centered on its own line.

Nothing warns you. The build passes, MathJax renders it happily, the maths is
correct. Inline math does not wrap and can cause overflow. At 320px, `/dsplab-fourier1/` overflowed by 211px. Its triangle-wave definition immediately followed "The triangular wave is defined as:".
Three equations had this problem. Only one caused overflow, so layout checks alone missed the other two.

It also flags a fence with prose immediately *below* it. That one is not a bug
today — the paragraph after a closing fence parses fine. Every affected equation followed prose placed directly after a closing fence. This spacing pattern caused the bug.

The checker ignores `$$` inside code fences. It also ignores deliberate inline math such as `$$x(t)$$`. Only
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

Contrast cannot be read off the stylesheet. Contrast depends on the colors actually displayed together. Ancestor backgrounds and translucent layers can change the result of a text-color rule. This measures
the rendered result at 390px and 1280px. WCAG 2.1 AA requires 4.5:1 for body text and 3:1 for large text. Large text means 24px, or 18.66px bold).

Teachers project these lessons in classrooms. Marginal contrast on a laptop can become unreadable on a projector.

**A warning worth keeping.** The first version measured every element with a text-node child. This included containers inheriting colors used only by their descendants. It reported 81 of 82 pages
broken, and every one was wrong. The checker now measures only elements with their own non-whitespace text. `--self-test` covers the earlier mistake.

The corrected first run found five failing color pairs in two exported Jupyter notebooks. All came from the default Pygments palette. Comments measured 4.25:1; string interpolation measured 3.65:1. They are corrected by an
override block near the top of each of those two files, which explains itself.

Since the move to the Design System the colours are its own. New failures are more likely to involve utility classes on unsuitable backgrounds, such as `text-wvu-gold` on white. Fix these in the page rather than `css/lessons.scss`.

It does not cover text over images, focus indicators, or anything needing a
pointer or keyboard. One measurable slice, not the whole of accessibility.

## I/Q notebook export

The published I/Q notebook is a static export. Its Bootstrap stylesheet and
13 unchanged plot images live in `images/iq/`, with their stylesheet at `css/iq-notebook.css`.
The HTML keeps its text, code samples,
plot descriptions, MathJax, and accessibility overrides. The unused Jupyter
widget scripts are omitted.

When updating the export, preserve its metadata, skip link, heading IDs, image
descriptions, and preview `noindex`. Keep plot files separate so they can load
on demand. Compare all plots and rerun the layout and contrast checks.

## Historical notebook styles

`retired_sites.py history` repairs two optional stylesheet references in the published archive:
`dspira-archive/gbtdrift/index.html` and `dspira-archive/labs/05/I_Q_quadrature_sampling.html`.
Both notebook exports embed their styles but also request an absent `custom.css` override.
The publication step removes that reference only when the stylesheet is missing.
If a future source package includes the override, it is copied and retained.

The preserved source and ZIP remain unchanged. Run `python3 tools/test_retired_sites.py` to check this behavior.
## Preserve moved download addresses

`publish_assets.py` rebuilds old file addresses from `_data/legacy_assets.json` after Jekyll runs.
It copies local lesson assets and verifies pinned downloads from active repositories.
It rejects missing sources, conflicting destinations, unsafe paths, and checksum mismatches.
Run `python3 tools/test_publish_assets.py`, then `python3 tools/publish_assets.py --site _site`.
See [the asset guide](../assets/README.md) before moving an existing download.
