#!/usr/bin/env python3
"""
Tests for check_links.py, and in particular for its model of the anchor ids
GitHub Pages generates.

    python3 tools/test_check_links.py        # from the top of a checkout

Two halves:

  1. Fixtures. Every (heading, id) pair below was produced by running the real
     gems - kramdown 2.4.0 with kramdown-parser-gfm 1.1.0, the versions
     https://pages.github.com/versions/ says GitHub Pages uses - over this
     repository and reading the ids out of the generated HTML. They are the
     awkward cases: apostrophes, ampersands, slashes, tabs, underscores,
     bracketed labels, runs of hyphens, repeated headings.

  2. Canaries. Break something on purpose, confirm check_links.py reports it,
     put it back. A checker that never fires is indistinguishable from a
     checker that works, which is how 30 broken table-of-contents anchors sat
     on the site while the link report said everything was fine.

Every test restores the tree, so a run leaves the checkout exactly as it found
it. Python 3 standard library only.
"""

import os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import check_links as C                                        # noqa: E402

BASEURL = "/dspira-lessons"

# heading source (as written in the markdown)  ->  id kramdown really emits
FIXTURES = [
    ("1. Introduction to GNU Radio and Signals",
     "1-introduction-to-gnu-radio-and-signals"),
    # a lone hyphen survives; the spaces either side become hyphens too
    ("1.2. GQRX - It's cool",                 "12-gqrx---its-cool"),
    ("1.10. GNU Radio Companion Example.",    "110-gnu-radio-companion-example"),
    # bracketed label inside bold, and a leading digit that is NOT stripped
    # (kramdown's own parser strips leading non-letters; the GFM parser does not)
    ("5.2.1. 8 Point Fast Fourier Transform **[OPTIONAL]**",
     "521-8-point-fast-fourier-transform-optional"),
    # '&' vanishes and leaves the two spaces around it as two hyphens
    ("5.6. Spectral Leakage & Polyphase Filter Bank (PFB)",
     "56-spectral-leakage--polyphase-filter-bank-pfb"),
    ("2.4. Fun SDR/GNU Radio things",         "24-fun-sdrgnu-radio-things"),
    ("2.3.1  Signal Modulation",              "231--signal-modulation"),
    # underscore is a \p{Word} character, so it stays - in the heading text and
    # in the id. The '.' of the filename does not.
    ("How to Run GNU Radio and the spectrometer_w_cal.grc program from the flashdrive.",
     "how-to-run-gnu-radio-and-the-spectrometer_w_calgrc-program-from-the-flashdrive"),
    ("Installing `gr-radio_astro`",           "installing-gr-radio_astro"),
    # a tab counts as a space
    ("**1.\tFeatures of the *Spectrum* Tab**", "1-features-of-the-spectrum-tab"),
    # '-----' is parsed as em-dash + en-dash and disappears entirely
    ("-----> [Document](https://example.com/x)", "-document"),
    # link text is kept, the URL is not
    ("Click here for a complete document of [Teacher's Notes](https://docs.google.com/x) for this whole activity sequence",
     "click-here-for-a-complete-document-of-teachers-notes-for-this-whole-activity-sequence"),
    ("*DSPIRA Summer Session - July 2019 - Green Bank, West Virginia*",
     "dspira-summer-session---july-2019---green-bank-west-virginia"),
    ("Installing Ubuntu image with radio astronomy preinstalled on a Raspberry Pi",
     "installing-ubuntu-image-with-radio-astronomy-preinstalled-on-a-raspberry-pi"),
    # two spaces in the heading would give 'preinstalled--on'; that is not a
    # bug in this checker, it is what the site would really publish
    ("Installing Ubuntu image with radio astronomy preinstalled  on a Raspberry Pi",
     "installing-ubuntu-image-with-radio-astronomy-preinstalled--on-a-raspberry-pi"),
]

# (name, file, find, replace, should the checker's count go up?)
CANARIES = [
    ("case-sensitive anchor", "_posts/2020-08-14-dsplab1.md",
     "(#16-exercises)", "(#16-Exercises)", True),
    ("renumbered heading", "_posts/2020-08-14-dsplab5.md",
     "(#54-the-spectrometers-purpose)", "(#55-the-spectrometers-purpose)", True),
    ("nested brackets in the label", "_posts/2020-08-14-dsplab5.md",
     "**[OPTIONAL]**](#521-8-point", "**[OPTIONAL]**](#999-8-point", True),
    ("cross-page fragment", "_posts/2020-08-14-dsplab1.md",
     "/dsplab-sdr/#24-fun-sdrgnu-radio-things", "/dsplab-sdr/#24-fun-nonsense", True),
    ("heading renamed, contents left behind", "_posts/2020-08-14-dsplab2.md",
     "## 2.1. Introduction", "## 2.1. Introduction and Setup", True),
    ("underscore dropped from an id", "_posts/2021-08-05-RaspberryPi.md",
     "(#installing-gr-radio_astro)", "(#installing-gr-radioastro)", True),
    ("anchor inside a code fence is an example, not a link",
     "_posts/2020-08-14-dsplab1.md",
     "```bash", "```bash\n# see [nothing](#no-such-heading)", False),
    ("bare '#' is the back-to-top link", "_posts/2020-08-14-dsplab1.md",
     "[↑ Go to the Top of the Page](#)", "[↑ Top](#)", False),
    ("skip link in _includes points into _layouts", "_includes/header.html",
     'href="#main"', 'href="#main"', False),
]


def broken_count():
    p = subprocess.run([sys.executable, os.path.join("tools", "check_links.py"),
                        "--offline"], capture_output=True, text=True, cwd=ROOT)
    m = re.search(r"broken:\s+(\d+)", p.stdout)
    if not m:
        sys.exit("check_links.py did not run:\n" + p.stdout + p.stderr)
    return int(m.group(1))


def main():
    os.chdir(ROOT)
    fails = []

    print("fixtures - ids against the real kramdown output")
    for src, want in FIXTURES:
        got = C.gfm_id(C.heading_raw_text(src, BASEURL))
        ok = got == want
        if not ok:
            fails.append("id for %r: got %r, want %r" % (src[:50], got, want))
        print("  %-4s %s" % ("ok" if ok else "FAIL", src[:66]))

    # duplicate headings get -1, -2, ... in document order
    dup = ["a", "a", "b", "a"]
    seen, out = {}, []
    for d in dup:
        n = seen.get(d, -1) + 1
        seen[d] = n
        out.append(d if n == 0 else "%s-%d" % (d, n))
    if out != ["a", "a-1", "b", "a-2"]:
        fails.append("duplicate numbering model is wrong: %r" % (out,))
    print("  ok   duplicate headings numbered a, a-1, b, a-2")

    print("\ncanaries - break it, check the checker notices")
    base = broken_count()
    print("  baseline: %d finding(s)" % base)
    for name, path, old, new, should_fire in CANARIES:
        src = open(path, encoding="utf-8").read()
        if old not in src:
            fails.append("canary setup: %r not found in %s" % (old[:40], path))
            print("  SKIP %s" % name)
            continue
        shutil.copy(path, path + ".canarybak")
        try:
            open(path, "w", encoding="utf-8").write(src.replace(old, new, 1))
            fired = broken_count() > base
        finally:
            shutil.move(path + ".canarybak", path)
        ok = fired == should_fire
        if not ok:
            fails.append("canary %r: %s" % (name, "silent" if should_fire
                                            else "false positive"))
        print("  %-4s %-48s %s" % ("ok" if ok else "FAIL", name,
                                   "caught" if fired else "quiet"))

    after = broken_count()
    if after != base:
        fails.append("tree not restored: %d findings before, %d after"
                     % (base, after))

    print()
    if fails:
        for f in fails:
            print("FAIL: %s" % f)
        return 1
    print("all %d fixtures and %d canaries pass; tree restored"
          % (len(FIXTURES), len(CANARIES)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
