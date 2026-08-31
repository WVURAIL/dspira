#!/usr/bin/env python3
"""
Does every piece of text meet WCAG AA contrast?

    python3 tools/check_contrast.py                 # against _site
    python3 tools/check_contrast.py --self-test     # break it on purpose

Needs a browser:  pip install playwright && playwright install chromium

WHY THIS EXISTS

Contrast is not something you can eyeball. A colour that looks fine to the
person who chose it, on the monitor they chose it on, can be unreadable to a
student with low vision or on a projector in a bright classroom — and these
lessons get projected in classrooms.

It also cannot be checked by reading the stylesheet, because what matters is
the pair of colours that actually meet: a rule sets a colour, an ancestor four
levels up supplies the background, and a translucent layer in between changes
the answer. This measures the rendered result.

The thresholds are WCAG 2.1 AA: 4.5:1 for body text, 3:1 for large text, where
large means 24px or 18.66px bold.

A WARNING FROM WRITING IT

The first version of this measured every element with a text node child, which
includes containers whose visible words live in their children. Those inherit a
colour they never paint. It reported 81 of 82 pages as broken, and every one of
those was wrong. Only elements with their own non-whitespace text are measured
now — and that is why --self-test exists.

WHAT IT DOES NOT COVER

Contrast of text against images, focus indicators, and anything that needs a
pointer or a keyboard. It is one measurable slice of accessibility, not a
substitute for the rest.
"""

import argparse
import functools
import http.server
import os
import re
import socketserver
import sys
import threading

# Pages exempted, with a reason each. Keep it short.
ALLOW = {}

WIDTHS = (390, 1280)

PROBE = r"""() => {
  const srgb = c => { c /= 255; return c <= 0.03928 ? c/12.92 : Math.pow((c+0.055)/1.055, 2.4); };
  const lum = ([r,g,b]) => 0.2126*srgb(r) + 0.7152*srgb(g) + 0.0722*srgb(b);
  const nums = s => { const m = (s||'').match(/[\d.]+/g); return m ? m.map(Number) : null; };
  const over = (fg, bg) => { const a = fg.length > 3 ? fg[3] : 1;
                             return [0,1,2].map(i => fg[i]*a + bg[i]*(1-a)); };
  // Walk up to the first opaque background, compositing translucent layers.
  const bgOf = el => {
    const stack = []; let n = el;
    while (n) {
      const c = nums(getComputedStyle(n).backgroundColor);
      if (c) { const a = c.length > 3 ? c[3] : 1;
               if (a >= 0.999) { let base = c.slice(0,3);
                                 for (let i = stack.length-1; i >= 0; i--) base = over(stack[i], base);
                                 return base; }
               if (a > 0) stack.push(c); }
      n = n.parentElement;
    }
    let base = [255,255,255];
    for (let i = stack.length-1; i >= 0; i--) base = over(stack[i], base);
    return base;
  };
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    // Only elements that paint their OWN words. A container whose text lives in
    // children inherits a colour it never renders; measuring that is what made
    // the first version of this call almost every page broken.
    const own = [...el.childNodes]
      .filter(n => n.nodeType === 3 && n.textContent.trim().length > 1)
      .map(n => n.textContent.trim()).join(' ');
    if (!own) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    const fg = nums(cs.color); if (!fg) continue;
    const bg = bgOf(el);
    const ratio = (() => { const l1 = lum(over(fg, bg)), l2 = lum(bg);
                           return (Math.max(l1,l2)+0.05) / (Math.min(l1,l2)+0.05); })();
    const px = parseFloat(cs.fontSize);
    const w = cs.fontWeight === 'bold' ? 700 : (parseInt(cs.fontWeight) || 400);
    const need = (px >= 24 || (px >= 18.66 && w >= 700)) ? 3 : 4.5;
    if (ratio < need - 0.005)
      out.push({ratio: +ratio.toFixed(2), need, px: +px.toFixed(1), weight: w,
                tag: el.tagName, cls: (el.className||'').toString().slice(0,28),
                fg: cs.color, bg: `rgb(${bg.map(Math.round).join(',')})`,
                text: own.slice(0, 44)});
  }
  return out;
}"""


class _Threaded(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass


def serve(root):
    socketserver.TCPServer.allow_reuse_address = True
    httpd = _Threaded(("127.0.0.1", 0), functools.partial(_Quiet, directory=root))
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


def run(site, base, quiet=False):
    site = os.path.abspath(site)
    root = site
    if base:
        import tempfile
        tmp = tempfile.mkdtemp()
        link = os.path.join(tmp, base.strip("/"))
        os.makedirs(os.path.dirname(link), exist_ok=True)
        os.symlink(site, link)
        root = tmp

    pages = sorted(
        os.path.join(dp, f)[len(site):].replace(os.sep, "/")
        for dp, _, fs in os.walk(site) for f in fs if f.endswith(".html"))
    stubs = [p for p in pages if is_redirect_stub(site + p)]
    pages = [p for p in pages if p not in ALLOW and p not in stubs]
    if not pages:
        sys.exit(f"::error::no HTML found under {site}")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("::error::playwright is not installed. "
                 "pip install playwright && playwright install chromium")

    httpd, port = serve(root)
    prefix = f"http://127.0.0.1:{port}{base}"
    bad, unreachable = {}, []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        try:
            for url in pages:
                # Retry once, then report. Skipping a page that would not load
                # meant it passed silently, which is the opposite of the job.
                err = None
                for attempt in (1, 2):
                    try:
                        page.goto(prefix + url, wait_until="load", timeout=20000)
                        err = None
                        break
                    except Exception as e:                       # noqa: BLE001
                        err = str(e)[:90]
                        page = settle(page, browser)   # or the next goto dies too
                if err:
                    unreachable.append((url, err))
                    continue
                for w in WIDTHS:
                    page.set_viewport_size({"width": w, "height": 900})
                    try:
                        rows = page.evaluate(PROBE)
                    except Exception:                            # noqa: BLE001
                        break                                    # redirect stub
                    for r in rows:
                        bad.setdefault(url, {})[(r["tag"], r["cls"], r["ratio"])] = r
                page = settle(page, browser)
        finally:
            browser.close()
            httpd.shutdown()

    if not quiet:
        print(f"{len(pages)} pages at {' and '.join(f'{w}px' for w in WIDTHS)}, "
              f"baseurl {base or '(none)'}")
        for u, why in sorted(ALLOW.items()):
            print(f"  not checked: {u} — {why}")
        for u in sorted(stubs):
            print(f"  not checked: {u} — meta-refresh redirect stub")

    if unreachable and not quiet:
        for url, err in unreachable:
            print(f"::error::{url} did not load, twice — {err}")

    if not bad:
        if not quiet:
            if not unreachable:
                print("every element meets WCAG AA.")
        return 1 if unreachable else 0

    if not quiet:
        print()
        for url, rows in sorted(bad.items()):
            print(f"::error::{url}: {len(rows)} colour pair(s) below WCAG AA")
            for r in sorted(rows.values(), key=lambda x: x["ratio"])[:5]:
                print(f"           {r['ratio']}:1 (needs {r['need']})  "
                      f"<{r['tag'].lower()} class=\"{r['cls']}\">  "
                      f"{r['fg']} on {r['bg']}  {r['px']}px/{r['weight']}  "
                      f"{r['text']!r}")
    return 1


PASSES = """<!doctype html><html><body style="background:#fff">
<p style="color:#444;font-size:16px">Dark grey on white is about 9:1.</p>
</body></html>"""

# 3.0:1 — fine for large text, not for this. The kind of near miss that is
# invisible by eye and is most of what this catches.
FAILS = """<!doctype html><html><body style="background:#fff">
<p style="color:#949494;font-size:16px">Mid grey on white is about 3:1.</p>
</body></html>"""

# Text in a child of a coloured container. The container inherits a colour it
# never paints; an earlier version measured that and called the page broken.
NESTED_OK = """<!doctype html><html><body style="background:#04070e">
<div style="color:#04070e"><p style="color:#f2f0eb">Light text on the dark chrome.</p></div>
</body></html>"""


def self_test():
    import shutil
    import tempfile
    ok = True
    for name, html, expect_fail in (("plain dark grey on white", PASSES, False),
                                    ("mid grey on white, 3:1", FAILS, True),
                                    ("container inherits a colour it never paints",
                                     NESTED_OK, False)):
        d = tempfile.mkdtemp()
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
        code = run(d, "", quiet=True)
        good = (code == 1) if expect_fail else (code == 0)
        ok &= good
        print(f"  {'ok  ' if good else 'FAIL'} {name:44} "
              f"{'caught' if code else 'quiet'}")
        shutil.rmtree(d)
    print("self-test passed" if ok else "::error::self-test FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="_site")
    ap.add_argument("--baseurl", default=None)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not os.path.isdir(args.site):
        sys.exit(f"::error::{args.site} does not exist — build the site first")
    base = args.baseurl if args.baseurl is not None else baseurl_from_config()
    return run(args.site, base)


if __name__ == "__main__":
    sys.exit(main())
