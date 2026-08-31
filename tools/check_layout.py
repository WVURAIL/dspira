#!/usr/bin/env python3
"""
Does any page scroll sideways?

    python3 tools/check_layout.py                 # against _site
    python3 tools/check_layout.py --site _site --baseurl /dspira-lessons
    python3 tools/check_layout.py --fine          # sweep every width, slower

Needs playwright:  pip install playwright && playwright install chromium

WHY THIS EXISTS

Horizontal overflow is the quietest layout bug there is. The page loads, it
looks right on the machine it was written on, nothing errors, and on a phone the
whole thing slides an inch to the left when you try to scroll down. Nobody
reports it, because it reads as the site being janky rather than as a fault.

This repository has had two, and neither was found by looking:

  A lesson title containing spectrometer_w_cal.grc. A heading is set at up to
  3.1rem, and one unbreakable 25-character token is wider than a 320px phone, so
  the page leaked 54px. It had been there since 2020.

  A sixth entry in the navigation. The header fitted five, and six overflowed by
  up to 38px — but only between 721 and 756px, a band just above the point where
  the menu collapses to a hamburger. Wide enough to catch a small laptop window,
  narrow enough that nobody would think to look there.

The second one is why this sweeps continuously rather than checking a handful of
device sizes. A bug that only exists between 721 and 756px is invisible to a
check that tests 375, 768 and 1280.

WHAT COUNTS AS OVER

An element sticking out past the right edge with nothing clipping it, still there
once the page has finished arriving. Not an element that scrolls its own content —
a long equation does that on purpose and moves nothing. And not a page that is
over only while MathJax swaps its preview for the real equations: that is reported
as settling, because measuring inside that window made the same commit pass and
fail depending on how fast a CDN replied.

WHAT IT DOES NOT COVER

Only horizontal overflow. It says nothing about whether a page looks good, and
it will not catch text that overlaps, colours that fail contrast, or an image
squashed out of aspect. Those need eyes.
"""

import argparse
import functools
import http.server
import os
import re
import socketserver
import sys
import threading
import time

# Pages with a known, accepted overflow. Anything listed here is NOT checked, so
# keep the list short and say why each one is on it.
ALLOW = {
    # Two Jupyter notebooks exported by nbconvert, each carrying its own inlined
    # copy of Bootstrap 3. Bootstrap's .container uses negative margins that
    # overhang by 8px at tablet widths. Both pages are deliberately served
    # outside the site layout — their Bootstrap would otherwise rewrite the
    # header, footer and every button — so this is theirs to have, and fixing it
    # would mean editing generated output that gets regenerated.
    "/iq/index.html": "inlined Bootstrap 3 container, 8px at ~768px",
    "/code/gbt_drift/gbt_rendered_2017.html": "inlined Bootstrap 3 container, 8px at ~768px",
}

# Every page gets these. Real phones, tablets and laptops.
COARSE = (320, 360, 390, 414, 768, 1024, 1280, 1440)

# The global chrome — header, nav, footer — is on every page, so one page swept
# closely covers it. This is the sweep that would have caught the nav.
FINE_STEP = 10
FINE_RANGE = (320, 1440)


class _Threaded(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):        # a 404 for a font is not our business
        pass


def serve(root, port=0):
    handler = functools.partial(_Quiet, directory=root)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = _Threaded(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1]


def is_redirect_stub(path):
    """A meta-refresh page navigates itself the moment it loads."""
    try:
        head = open(path, encoding="utf-8", errors="replace").read(4000)
    except OSError:
        return False
    return re.search(r'http-equiv=["\']?\s*refresh', head, re.I) is not None


def settle(page, browser):
    """Return a page with nothing in flight, replacing it if need be.

    Every page is measured on one shared browser page, which is far faster than
    a reload per width. That is fine until a page navigates itself — a
    meta-refresh stub does, and so does a load that timed out while its
    navigation carried on. The next goto then dies with "interrupted by another
    navigation", and the page stays poisoned, so every goto after it dies too.
    One flake became thirty-nine failures in CI that way.

    Parking at about:blank is not enough on its own: that goto gets interrupted
    by the same in-flight navigation. So if it will not park, the page is thrown
    away and a fresh one opened. Verified by forcing every single load to fail
    on its first attempt — with this, all 79 recover on the retry.
    """
    try:
        page.goto("about:blank", wait_until="load", timeout=5000)
        return page
    except Exception:                                    # noqa: BLE001
        try:
            page.close()
        except Exception:                                # noqa: BLE001
            pass
        return browser.new_page()

def baseurl_from_config(path="_config.yml"):
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return ""
    m = re.search(r'^baseurl:\s*"?([^"\n]*)"?\s*$', text, re.M)
    return (m.group(1).strip() if m else "").rstrip("/")


# Which element is actually pushing the page?
#
# The first version of this asked "is anything wider than its own box", which is
# the wrong question. An element that scrolls its own content — overflow-x on a
# long equation, a table in a scroller, a code block — is wider than its box by
# design and moves the page not at all. This blamed those, and did it while the
# real culprit sat unmentioned two elements further down the list.
#
# The right question is which boxes stick out past the right edge of the viewport
# with nothing clipping them. Ancestors of the culprit stick out too, so only the
# deepest are named, worst first.
PROBE = """() => {
  const de = document.documentElement;
  const over = de.scrollWidth - de.clientWidth;
  if (over <= 1) return null;
  const edge = de.clientWidth;
  const clipped = e => {
    for (let a = e.parentElement; a && a !== de; a = a.parentElement) {
      if (getComputedStyle(a).overflowX !== 'visible') return true;
    }
    return false;
  };
  const out = [];
  for (const e of document.querySelectorAll('body *')) {
    const r = e.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (Math.round(r.right + window.scrollX) <= edge + 1) continue;
    // Fixed elements travel with the viewport; they cannot widen the document.
    if (getComputedStyle(e).position === 'fixed') continue;
    if (clipped(e)) continue;
    out.push(e);
  }
  const leaf = out
    .filter(e => !out.some(o => o !== e && e.contains(o)))
    .map(e => ({tag: e.tagName, cls: (e.className || '').toString().slice(0, 30),
                wide: Math.round(e.getBoundingClientRect().width),
                past: Math.round(e.getBoundingClientRect().right + window.scrollX) - edge,
                text: (e.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 60)}));
  leaf.sort((a, b) => b.past - a.past);
  return {over, leaf: leaf.slice(0, 2)};
}"""


OVER = ("() => document.documentElement.scrollWidth"
        " - document.documentElement.clientWidth")


# How long to keep watching a page that looks over. The first time on a page it
# may still be arriving, so it gets the long one; after that it has arrived and
# only needs long enough to reflow.
ARRIVING = 2.0
REFLOW = 0.4


def wait_out(page, budget):
    """Watch a page that looks over, and see whether it comes back on its own.

    A page is not finished when its load event fires. MathJax paints a rough
    preview and replaces it with the real thing a few hundred milliseconds later;
    fonts land; images size themselves. Measure inside that window and the answer
    depends on how quickly a CDN replied — which is how this check came to fail in
    CI on a page that is fine at every width, and could not be reproduced at any
    latency locally. A check that gives a different answer for the same commit is
    worse than no check: it teaches people to re-run it until it goes green.

    Note what is *not* used here: waiting for the number to stop changing. It stops
    changing constantly — between the preview arriving and the equations replacing
    it, nothing moves for a comfortable fraction of a second. Holding still is not
    the same as being finished, and the first version of this went green on that
    and failed the transient case in --self-test.

    So: it either clears within the budget or it does not. Returns 0 if it clears,
    the last reading if it does not, None if the page navigated away underneath us.
    """
    deadline = time.time() + budget
    now = 0
    while True:
        try:
            now = page.evaluate(OVER)
        except Exception:                                    # noqa: BLE001
            return None                                      # navigated away
        if now <= 1:
            return 0
        if time.time() >= deadline:
            return now
        time.sleep(0.04)


CLEAN = """<!doctype html><html><head><meta name=viewport
content="width=device-width,initial-scale=1"><style>
*{box-sizing:border-box}body{margin:0;font:16px/1.5 sans-serif}
.wrap{padding:20px;overflow-wrap:break-word}</style></head>
<body><div class=wrap><h1>An ordinary heading that wraps between words</h1>
<p>Body text.</p></div></body></html>"""

# One token, no spaces, wider than a phone. This is the shape of both real bugs.
BROKEN = CLEAN.replace("overflow-wrap:break-word", "overflow-wrap:normal").replace(
    "An ordinary heading that wraps between words",
    "Running_the_spectrometer_w_calibration_program_on_a_flashdrive.grc")


# A page that navigates itself, sorted BEFORE the pages that follow it — the
# shape that took CI down: everything alphabetically after it failed to load.
STUB = ('<!doctype html><html><head>'
        '<meta http-equiv="refresh" content="0; url=/b-after/">'
        '</head><body><p>moved</p></body></html>')

# Wide content inside its own scroller, plus a genuine 40px offender. This is the
# shape of every maths page: the equation is far wider than the phone and scrolls
# by itself, harming nothing. The report has to name .culprit. It named the
# equation instead once, and that sent a day of looking in the wrong place.
DECOY = """<!doctype html><html><head><meta name=viewport
content="width=device-width,initial-scale=1"><style>
*{box-sizing:border-box}body{margin:0;font:16px/1.5 sans-serif}
.scroller{overflow-x:auto;margin:20px 0}
.wide{width:1200px;height:20px;background:#ddd}
.culprit{width:360px;height:20px;background:#c00}</style></head>
<body><div class=scroller><div class=wide></div></div>
<div class=culprit></div></body></html>"""

# Over while it is still arriving, fine once it lands. MathJax does exactly this:
# a rough preview first, the real equations a few hundred milliseconds later.
# Measuring inside that window makes the answer depend on how fast a CDN replied.
TRANSIENT = """<!doctype html><html><head><meta name=viewport
content="width=device-width,initial-scale=1"><style>
*{box-sizing:border-box}body{margin:0}
#g{width:900px;height:30px;background:#ccc}</style></head>
<body><div id=g></div>
<script>setTimeout(function () {
  document.getElementById('g').style.width = '100%';
}, 500);</script></body></html>"""


def self_test():
    """Break a page on purpose and check this script notices. The sweep resizes
    the viewport rather than reloading for every width, which is eight times
    faster and would be worthless if reflow were not measured correctly."""
    import shutil
    import tempfile
    ok = True

    # A self-navigating page must not take the rest of the run with it.
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "a-stub"))
    os.makedirs(os.path.join(d, "b-after"))
    open(os.path.join(d, "a-stub", "index.html"), "w", encoding="utf-8").write(STUB)
    open(os.path.join(d, "b-after", "index.html"), "w", encoding="utf-8").write(CLEAN)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(CLEAN)
    code = run_sweep(d, "", fine=True, quiet=True)
    good = code == 0
    ok &= good
    print(f"  {'ok  ' if good else 'FAIL'} {'redirect stub does not poison the run':32} "
          f"{'caught' if code else 'quiet'}")
    shutil.rmtree(d)

    for name, html, expect_fail in (("clean page", CLEAN, False),
                                    ("unbreakable token in an h1", BROKEN, True),
                                    ("over only while it loads", TRANSIENT, False),
                                    ("real offender beside a scroller", DECOY, True)):
        d = tempfile.mkdtemp()
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
        found = []
        code = run_sweep(d, "", fine=True, quiet=True, report=found)
        good = (code == 1) if expect_fail else (code == 0)
        ok &= good
        print(f"  {'ok  ' if good else 'FAIL'} {name:32} "
              f"{'caught' if code else 'quiet'}")
        shutil.rmtree(d)

        # Catching it is half the job; saying which element it is, is the rest.
        if html is DECOY:
            named = [t["cls"] for _, _, _, leaf in found for t in leaf]
            right = bool(named) and all(c == "culprit" for c in named)
            ok &= right
            print(f"  {'ok  ' if right else 'FAIL'} {'and names the right element':32} "
                  f"{sorted(set(named)) or 'named nothing'}")
    print("self-test passed" if ok else "::error::self-test FAILED")
    return 0 if ok else 1


def run_sweep(site, base, fine=False, quiet=False, report=None):
    """Sweep a built site. Returns 0 if nothing scrolls sideways, 1 if something does.

    Pass a list as `report` to get the findings themselves; --self-test uses that
    to check the right element is named, which an exit code cannot show.
    """
    site = os.path.abspath(site)

    # Serve the built site at its real baseurl, so absolute asset paths resolve
    # exactly as they do in production. Without this the stylesheet 404s and
    # every page passes for the wrong reason.
    root = site
    if base:
        import tempfile
        tmp = tempfile.mkdtemp()
        link = os.path.join(tmp, base.strip("/"))
        os.makedirs(os.path.dirname(link), exist_ok=True)
        os.symlink(site, link)
        root = tmp

    pages, stubs = [], []
    for dirpath, _, files in os.walk(site):
        for f in files:
            if f.endswith(".html"):
                url = os.path.join(dirpath, f)[len(site):].replace(os.sep, "/")
                if url in ALLOW:
                    continue
                if is_redirect_stub(os.path.join(dirpath, f)):
                    stubs.append(url)          # nothing to measure, and it
                    continue                   # navigates away as it loads
                pages.append(url)
    pages.sort()
    if not pages:
        sys.exit(f"::error::no HTML found under {site}")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("::error::playwright is not installed. "
                 "pip install playwright && playwright install chromium")

    httpd, port = serve(root)
    prefix = f"http://127.0.0.1:{port}{base}"
    findings, unreachable, settling, loads = [], [], [], 0

    # The global chrome is on every page, so one page swept closely covers it.
    chrome_page = "/index.html" if "/index.html" in pages else pages[0]
    fine_widths = list(range(FINE_RANGE[0], FINE_RANGE[1] + 1, FINE_STEP))

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        try:
            plan = {u: set(COARSE) for u in pages}
            for u in (pages if fine else [chrome_page]):
                plan[u] = plan.get(u, set()) | set(fine_widths)

            for url in sorted(plan):
                widths = sorted(plan[url])
                # Load once, then resize. Reflow is what is being measured, and a
                # reload per width made this eight times slower for the same
                # answer. --self-test is what keeps that shortcut honest.
                page.set_viewport_size({"width": widths[0], "height": 800})
                # Retry once. A page that fails to load is a different fault
                # from a page that overflows, and reporting one as the other
                # sends whoever reads this looking in the wrong place.
                err = None
                for attempt in (1, 2):
                    try:
                        page.goto(prefix + url, wait_until="load", timeout=20000)
                        loads += 1
                        err = None
                        break
                    except Exception as e:                       # noqa: BLE001
                        err = str(e)[:90]
                        page = settle(page, browser)   # or the next goto dies too
                if err:
                    unreachable.append((url, err))
                    continue
                arrived = False
                for w in widths:
                    page.set_viewport_size({"width": w, "height": 800})
                    try:
                        r = page.evaluate(PROBE)
                    except Exception:                            # noqa: BLE001
                        break                                    # meta-refresh stub
                    if not r:
                        continue
                    # Free on a page that is fine, which is nearly all of them.
                    held = wait_out(page, REFLOW if arrived else ARRIVING)
                    arrived = True
                    if held is None:
                        break                                    # meta-refresh stub
                    if held == 0:
                        settling.append((url, w, r["over"]))
                        continue
                    try:
                        r = page.evaluate(PROBE)
                    except Exception:                            # noqa: BLE001
                        break
                    if r:
                        findings.append((url, w, r["over"], r["leaf"]))
                page = settle(page, browser)
        finally:
            browser.close()
            httpd.shutdown()

    if not quiet:
        print(f"{len(pages)} pages, {loads} loads, baseurl {base or '(none)'}")
        for u, why in sorted(ALLOW.items()):
            print(f"  not checked: {u} — {why}")
        for u in sorted(stubs):
            print(f"  not checked: {u} — meta-refresh redirect stub")

    if unreachable and not quiet:
        for url, err in unreachable:
            print(f"::error::{url} did not load, twice — {err}")

    # Not a failure, but worth saying out loud: the page was over while it was
    # still arriving. It is what a visitor on a slow connection sees for a moment.
    if settling and not quiet:
        seen = {}
        for url, w, over in settling:
            seen[url] = max(seen.get(url, 0), over)
        for url, over in sorted(seen.items()):
            print(f"  settling: {url} was {over}px over while loading, "
                  f"then came back on its own")

    if report is not None:
        report.extend(findings)

    if not findings:
        if not quiet:
            if not unreachable:
                print("no page scrolls sideways at any width checked.")
        return 1 if unreachable else 0

    if not quiet:
        by_page = {}
        for url, w, over, leaf in findings:
            by_page.setdefault(url, []).append((w, over, leaf))
        print()
        for url, rows in sorted(by_page.items()):
            widths = [w for w, _, _ in rows]
            worst = max(rows, key=lambda row: row[1] or 0)
            print(f"::error::{url} scrolls sideways at {min(widths)}-{max(widths)}px "
                  f"(worst {worst[1]}px over, at {worst[0]}px)")
            # Named from the width it is worst at, not the narrowest one checked.
            for tag in (worst[2] or [])[:2]:
                if isinstance(tag, dict):
                    print(f"           <{tag['tag'].lower()} class=\"{tag['cls']}\"> "
                          f"is {tag['wide']}px wide and sticks out {tag['past']}px "
                          f"— {tag['text']!r}")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="_site")
    ap.add_argument("--baseurl", default=None)
    ap.add_argument("--fine", action="store_true",
                    help="sweep every page at every width, not just the chrome page")
    ap.add_argument("--self-test", action="store_true",
                    help="break a page on purpose and check this script notices")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    if not os.path.isdir(args.site):
        sys.exit(f"::error::{args.site} does not exist — build the site first")

    base = args.baseurl if args.baseurl is not None else baseurl_from_config()
    return run_sweep(args.site, base, fine=args.fine)


if __name__ == "__main__":
    sys.exit(main())
