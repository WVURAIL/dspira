#!/usr/bin/env python3
"""
Link checker for the dspira-lessons site.

Run it from the top of a dspira-lessons checkout:

    python3 check_links.py              # check everything
    python3 check_links.py --offline    # skip the internet, ~1 second

It writes link-report.md next to itself and prints a summary.

No installation needed - Python 3 standard library only.

Findings land in one of three buckets:

  BROKEN    Confirmed dead. Worth fixing.
  CHECK     Could not be settled automatically. Google Drive, Google Docs and
            YouTube all answer "200 OK" for files that were deleted or made
            private, and plenty of sites block scripts outright. Reporting
            these as broken would be a lie, so they are listed separately.
  OK        Responded normally.

The offline half - internal page links, heading anchors and local files - needs
no network and is the part that catches most real breakage.

Anchors are checked in both directions:

  - in-page   [1.6. Exercises](#16-exercises)  - the tables of contents at the
              head of the labs are nothing else, and they rot silently every
              time a heading is renamed or a section renumbered
  - cross-page {{ site.baseurl }}/dsplab-sdr/#21-introduction

`tools/test_check_links.py` pins the anchor rules against output from the real
kramdown gems and breaks things on purpose to prove this checker still notices.
Run it after touching anything in here.
"""

import argparse, concurrent.futures, glob, html, os, re, sys, unicodedata
import urllib.error, urllib.parse, urllib.request
from collections import defaultdict

TIMEOUT = 20
WORKERS = 12
UA = "Mozilla/5.0 (compatible; dspira-link-check/1.0)"

# Hosts whose 200 means nothing much - they serve a friendly page for content
# that has been deleted, moved private, or needs a login.
UNVERIFIABLE = (
    "drive.google.com", "docs.google.com", "forms.gle",
    "youtube.com", "youtu.be", "www.youtube.com",
    "mediasite.com", "wvu.mediasite.com",
)


# ---------------------------------------------------------------- parsing

def source_files():
    # Everything Jekyll publishes as a page. A directory missing from this list
    # is not reported as a gap by anything - it simply goes unchecked - so a new
    # top-level directory of pages needs a line here. forum/ and the
    # categories/*/index.html redirect stubs were invisible until 2026.
    #
    # README.md, CONTRIBUTING.md and the READMEs under tools/ and code/ are
    # deliberately absent: _config.yml excludes the first two and the rest carry
    # no front matter, so none of them is a page. tools/README.md would also
    # report a false positive, because it quotes '#16-exercises' as an example
    # of the kind of anchor this script catches.
    out = []
    for pat in ("_posts/*.md", "_posts/*.markdown", "pages/*.md",
                "pages/*.html", "*.md", "index.html",
                "categories/*.html", "categories/*/index.md",
                "categories/*/index.html", "forum/*.md",
                "tags/*.md", "all/index.html",
                "_includes/*.html", "_layouts/*.html"):
        out += glob.glob(pat)
    return sorted(set(p for p in out if os.path.isfile(p)))


def front_matter(path):
    """Return the YAML front-matter block as a dict of simple key -> value."""
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        km = re.match(r"^(\w+)\s*:\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip("\"'")
    return fm


def slug_for(path):
    """The URL slug Jekyll will publish this file at."""
    fm = front_matter(path)
    if fm.get("permalink"):
        return fm["permalink"].strip("/")
    # index files publish at their directory path (categories/x/, all/, ...)
    d, base = os.path.split(path)
    if os.path.splitext(base)[0] == "index" and d:
        return d.strip("/")
    if os.path.splitext(base)[0] == "index":
        return ""
    base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)      # strip the date prefix
    return os.path.splitext(base)[0]


# --------------------------------------------------------- heading anchors
#
# GitHub Pages builds this site with kramdown 2.4.0 and kramdown-parser-gfm
# 1.1.0 (see https://pages.github.com/versions/), and _config.yml sets
# `input: GFM`. That parser assigns every heading
#
#     id = generate_gfm_header_id(header.options[:raw_text])
#
# where, verbatim from kramdown-parser-gfm:
#
#     NON_WORD_RE = /[^\p{Word}\- \t]/
#     result = text.downcase
#     result.gsub!(NON_WORD_RE, '')
#     result.tr!(" \t", '-')
#     result << "-#{n}" if this id has already been generated n>0 times
#
# and raw_text is the *text* of the heading's children: link text without the
# URL, code spans without the backticks, smart quotes and dashes as the
# typographic characters kramdown substituted for them. Ruby's \p{Word} is
# letters, marks, decimal digits and underscore - so `gr-radio_astro` keeps its
# underscore, while ':' and '.' and '(' are deleted.
#
# The functions below reproduce that exactly. They were checked against the
# real gems by running kramdown 2.4.0 + kramdown-parser-gfm 1.1.0 over every
# markdown file in this repository and diffing the ids: 0 differences across
# all 49 files. If you change anything here, redo that comparison - a checker
# that agrees with itself and not with the build is worse than no checker.

def _is_word_char(ch):
    if ch == "_":
        return True
    cat = unicodedata.category(ch)
    return cat[0] in ("L", "M") or cat in ("Nd", "Pc")


def gfm_id(text):
    """kramdown-parser-gfm's id slug for one heading's raw_text."""
    r = "".join(c for c in text.lower() if _is_word_char(c) or c in "- \t")
    return r.replace(" ", "-").replace("\t", "-")


def heading_raw_text(src, baseurl):
    """Approximate kramdown's options[:raw_text] for a heading's inline text."""
    t = resolve_liquid(src, baseurl)
    t = re.sub(r"\{:[^}]*\}", "", t)                      # {: .button} etc
    t = re.sub(r"<[^>]+>", "", t)                         # html tags
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", t)       # image -> alt text
    t = re.sub(r"!\[([^\]]*)\]\[[^\]]*\]", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)        # link  -> link text
    t = re.sub(r"\[([^\]]*)\]\[[^\]]*\]", r"\1", t)
    t = re.sub(r"`+([^`]*)`+", r"\1", t)                  # code spans
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"\*(.+?)\*", r"\1", t)
    # '_' only opens emphasis at a word boundary, which is why
    # spectrometer_w_cal.grc keeps both underscores in its id.
    t = re.sub(r"(?<![A-Za-z0-9_])___(.+?)___(?![A-Za-z0-9_])", r"\1", t)
    t = re.sub(r"(?<![A-Za-z0-9_])__(.+?)__(?![A-Za-z0-9_])", r"\1", t)
    t = re.sub(r"(?<![A-Za-z0-9_])_(.+?)_(?![A-Za-z0-9_])", r"\1", t)
    t = re.sub(r"~~(.+?)~~", r"\1", t)
    # kramdown's typographic substitutions, applied left to right. Every
    # replacement is punctuation and so is deleted from the id - which is why
    # '-----> [Document]' contributes nothing but a lone ' - ' survives.
    for a, b in (("---", "—"), ("--", "–"), ("...", "…"),
                 ("<<", "«"), (">>", "»")):
        t = t.replace(a, b)
    return t.replace("\\", "").strip()


def body_lines(path):
    """(lineno, line) for real body lines: front matter and code fences out."""
    try:
        lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    except OSError:
        return
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    fence = None
    while i < len(lines):
        m = re.match(r"^\s{0,3}(```+|~~~+)", lines[i])
        if m:
            tok = m.group(1)[0]
            if fence is None:
                fence = tok
            elif tok == fence:
                fence = None
            i += 1
            continue
        if fence is None:
            yield i + 1, lines[i]
        i += 1


IAL_ID_RE = re.compile(r"\{:\s*[^}]*#([A-Za-z0-9_.:-]+)[^}]*\}")


def anchors_in(path, baseurl="/dspira-lessons"):
    """Every fragment this page will answer to."""
    lines = list(body_lines(path))
    out, counter = set(), {}
    for idx, (_ln, line) in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if not m:
            continue
        src = m.group(2)
        explicit = IAL_ID_RE.search(src)
        if not explicit and idx + 1 < len(lines):
            nxt = lines[idx + 1][1].strip()
            if nxt.startswith("{:") and nxt.endswith("}"):
                explicit = IAL_ID_RE.search(nxt)
        if explicit:
            out.add(explicit.group(1))
            continue
        base = gfm_id(heading_raw_text(src, baseurl))
        n = counter.get(base, -1) + 1
        counter[base] = n
        out.add(base if n == 0 else "%s-%d" % (base, n))
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return out
    out |= set(IAL_ID_RE.findall(text))                     # {: #custom-id}
    out |= set(re.findall(r"\{#([\w-]+)\}", text))          # older {#id} form
    out |= set(re.findall(r"""<[a-zA-Z][^>]*\sid\s*=\s*["']([^"']+)["']""",
                          text))                            # raw html anchors
    return out


def resolve_liquid(u, baseurl):
    """Turn the Liquid the site actually uses into plain paths.

    An earlier version of this checker skipped any URL containing '{{', which
    silently excluded every '{{ site.baseurl }}/...' link - 130 of them, most
    of the site's internal links. Resolve the two forms the site uses; only
    genuinely dynamic expressions are still skipped.
    """
    u = u.replace("{{ site.baseurl }}", "/" + baseurl.strip("/"))
    u = re.sub(r"\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*(?:relative_url|absolute_url)\s*\}\}",
               lambda m: "/" + baseurl.strip("/") + m.group(1), u)
    return u


def links_in(path, baseurl):
    """Yield (url, line_number) for every link and image in the file.

    Liquid is resolved on the whole line BEFORE parsing out URLs - resolving
    after extraction re-truncates '{{ site.baseurl }}/x' at its first space,
    which is exactly the failure this rewrite exists to fix.
    """
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return
    in_fence = False
    for i, raw_line in enumerate(text.split("\n"), 1):
        # Fenced code blocks hold examples, not links - the newpost template
        # shows '![alt](.../name-of-your-image-file.FORMAT)' as a pattern to
        # copy, and reporting that as a broken image helps nobody.
        if raw_line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = resolve_liquid(raw_line, baseurl)
        # One level of nested brackets in the label. Without it a table-of-
        # contents entry like
        #     [5.2.1. 8 Point Fast Fourier Transform **[OPTIONAL]**](#521-...)
        # matches nothing at all and its target is never checked - which is
        # how one of the broken anchors stayed hidden from this checker.
        for m in re.finditer(r"!?\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(\s*([^)\s]+)",
                             line):
            yield m.group(1), i
        for m in re.finditer(r'(?:href|src)\s*=\s*["\']([^"\']+)', line):
            yield m.group(1), i


# ---------------------------------------------------------------- checking

def check_url(url):
    """Return (bucket, detail). Tries HEAD, falls back to GET."""
    host = urllib.parse.urlparse(url).netloc.lower()
    if any(host.endswith(u) or host == u for u in UNVERIFIABLE):
        return "CHECK", "host answers 200 even for deleted/private content"
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method,
                                         headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                final = r.geturl()
                if final.rstrip("/") != url.rstrip("/"):
                    return "OK", f"{r.status} (redirects to {final})"
                return "OK", str(r.status)
        except urllib.error.HTTPError as e:
            # HEAD is an optimisation, and a server that will not answer it has
            # not answered the question. The status it refuses with says nothing
            # about whether the page is there: indico.phys.vt.edu says 400,
            # wiki.analog.com says 500, plenty of others say 405, and all three
            # serve the page perfectly well over GET. So any HEAD error falls
            # through and the GET decides.
            if method == "HEAD":
                continue
            if e.code in (403, 406, 429, 999):
                return "CHECK", f"HTTP {e.code} - blocked or rate-limited"
            if 400 <= e.code < 600:
                return "BROKEN", f"HTTP {e.code}"
            return "CHECK", f"HTTP {e.code}"
        except urllib.error.URLError as e:
            # A connection-level failure is NOT evidence that the link is dead.
            # No internet, a corporate proxy, DNS trouble or a TLS problem all
            # land here, and calling those "broken" would send you chasing
            # links that are perfectly fine. Only an HTTP status says broken.
            return "CHECK", f"could not connect ({e.reason}) - not necessarily dead"
        except Exception as e:                    # noqa: BLE001
            return "CHECK", f"{type(e).__name__}: {e}"
    return "CHECK", "no response"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true",
                    help="skip external URLs (internal checks only)")
    ap.add_argument("--baseurl", default="/dspira-lessons")
    ap.add_argument("--fail-on", choices=("all", "anchors", "none"),
                    default="all",
                    help="what makes the exit code non-zero. 'anchors' is for "
                         "CI: it gates the one class of breakage that is "
                         "entirely inside this repository's control, without "
                         "failing every build over a PDF somebody still owes "
                         "us. Default 'all'.")
    args = ap.parse_args()

    if not os.path.isdir("_posts"):
        sys.exit("No _posts/ directory here. Run this from the top of a "
                 "dspira-lessons checkout.")

    files = source_files()
    slugs, anchors, own = {}, {}, {}
    for f in files:
        s = slug_for(f)
        slugs[s] = f
        a = anchors_in(f, args.baseurl)
        anchors[s] = a
        own[f] = a

    # _includes and _layouts are fragments: they are composed into one rendered
    # page, so an anchor in the header pointing at an id in the layout is fine.
    # Pool their ids and let any of them satisfy any of them.
    shell = set()
    for f in files:
        if f.startswith(("_includes/", "_layouts/")):
            shell |= own[f]
    for f in list(own):
        if f.startswith(("_includes/", "_layouts/")):
            own[f] = own[f] | shell

    internal, external, assets = [], defaultdict(list), []
    anchor_problems = []
    base = args.baseurl.strip("/")

    for f in files:
        for raw, line in links_in(f, args.baseurl):
            u = html.unescape(raw.strip())

            # In-page anchors. '#' on its own is the site's "back to the top"
            # link and always works. Anything else has to name a heading that
            # this page actually generates - the table of contents at the head
            # of each lab is nothing but these, and they rot silently when a
            # heading is renamed or renumbered.
            if u.startswith("#"):
                frag = urllib.parse.unquote(u[1:])
                if frag and frag not in own.get(f, set()):
                    anchor_problems.append((u, f, line,
                                            "anchor not found on this page - "
                                            "no heading generates id '%s'"
                                            % frag))
                continue

            if u.startswith(("mailto:", "tel:", "javascript:", "data:")):
                continue
            if "{{" in u or "{%" in u:            # Liquid template expression
                continue

            parsed = urllib.parse.urlparse(u)
            # Only URLs under this site's baseurl are ours to verify.
            # wvurail.org also hosts sibling projects (/lightwork/,
            # /dspira-2019/ and so on) that live in other repositories, so
            # those are external as far as this checker is concerned.
            norm_path = re.sub(r"/{2,}", "/", parsed.path)
            is_site = (not parsed.netloc) or (
                "wvurail.org" in parsed.netloc.lower()
                and re.match(rf"^/?{re.escape(args.baseurl.strip('/'))}(/|$)",
                             norm_path)
            )

            if not is_site:
                external[u].append((f, line))
                continue

            path = urllib.parse.unquote(parsed.path)
            frag = parsed.fragment
            # Collapse duplicate slashes first: links in the wild are written
            # as wvurail.org//dspira-lessons/... fairly often, and the server
            # serves those fine, so they must not be reported as broken.
            path = re.sub(r"/{2,}", "/", path)
            path = re.sub(rf"^/?{re.escape(base)}/?", "", path).strip("/")
            if not path:
                continue

            if re.search(r"\.\w{2,5}$", path):     # looks like a file
                # Jekyll compiles css/style.scss to css/style.css at build
                # time, so the .css the pages link is real even though only
                # the .scss is in the repo.
                scss_twin = path.endswith(".css") and os.path.exists(path[:-4] + ".scss")
                if not os.path.exists(path) and not scss_twin:
                    assets.append((u, f, line, "file not found"))
            elif path.startswith(".."):
                internal.append((u, f, line, "relative path escapes the site root"))
            else:
                key = path.split("/")[0] if "/" in path else path
                if path not in slugs and key not in slugs:
                    if not os.path.isdir(path):
                        internal.append((u, f, line, "no page publishes this URL"))
                elif frag:
                    # A cross-page fragment: /dsplab-sdr/#21-introduction. The
                    # page exists (checked above), so an unknown fragment is a
                    # real problem, not an unknown one.
                    tgt = path if path in slugs else key
                    known = anchors.get(tgt)
                    frag = urllib.parse.unquote(frag)
                    if known is not None and frag not in known:
                        anchor_problems.append((u, f, line,
                                                "page exists but has no "
                                                "heading with id '%s'" % frag))

    results = {}
    if not args.offline and external:
        # Pre-flight: if we cannot reach a known-good host, say so rather than
        # producing a report full of imaginary breakage.
        probe, _ = check_url("https://example.com")
        if probe != "OK":
            print("No internet reachable from here (proxy, VPN or offline).")
            print("Falling back to --offline; internal checks still run.\n")
            args.offline = True

    if not args.offline and external:
        print(f"checking {len(external)} external links "
              f"({WORKERS} at a time, be patient)...", flush=True)
        with concurrent.futures.ThreadPoolExecutor(WORKERS) as ex:
            futs = {ex.submit(check_url, u): u for u in external}
            done = 0
            for fut in concurrent.futures.as_completed(futs):
                results[futs[fut]] = fut.result()
                done += 1
                if done % 25 == 0:
                    print(f"  {done}/{len(external)}", flush=True)

    # ------------------------------------------------------------ report
    L = ["# Link report", ""]
    L.append(f"- source files scanned: **{len(files)}**")
    L.append(f"- internal links: **{sum(1 for _ in internal)} problems**")
    L.append(f"- heading anchors: **{len(anchor_problems)} problems**")
    L.append(f"- local file references: **{len(assets)} missing**")
    L.append(f"- external links: **{len(external)}**"
             + ("" if not args.offline else " *(not checked, --offline)*"))
    L.append("")

    def block(title, rows, note=""):
        L.append(f"## {title} ({len(rows)})")
        if note:
            L.append("")
            L.append(note)
        L.append("")
        if not rows:
            L.append("Nothing found.")
        for r in rows:
            L.append(f"- `{r[0]}`")
            L.append(f"  - {r[-1]}")
            L.append(f"  - in `{r[1]}` line {r[2]}")
        L.append("")

    block("Broken heading anchors", anchor_problems,
          "Links to a heading that does not exist. Most of these are tables of "
          "contents that were left behind when a section was renamed or "
          "renumbered: the page still loads, the link just does nothing, so "
          "nobody reports it. The ids are the ones kramdown really generates - "
          "lowercase, punctuation removed - see the notes in this script.")
    block("Broken internal links", internal,
          "Links to pages on this site that nothing publishes. These are the "
          "ones that show a 404 to a student following the lessons.")
    block("Missing local files", assets,
          "Images and PDFs referenced by a lesson that are not in the repo.")

    if not args.offline:
        for bucket, title, note in (
            ("BROKEN", "Broken external links",
             "Confirmed dead."),
            ("CHECK", "External links needing a human",
             "Could not be settled automatically - either the host blocks "
             "scripts, or it answers 200 even when the content is gone. "
             "Google Drive, Google Docs, YouTube and Mediasite are all in "
             "this category, so a 'CHECK' here is not evidence of a problem."),
        ):
            rows = []
            for u, (b, detail) in sorted(results.items()):
                if b != bucket:
                    continue
                f, line = external[u][0]
                extra = (f" (+{len(external[u]) - 1} more places)"
                         if len(external[u]) > 1 else "")
                rows.append((u, f + extra, line, detail))
            block(title, rows, note)

    open("link-report.md", "w", encoding="utf-8").write("\n".join(L))

    n_broken = len(internal) + len(assets) + len(anchor_problems) + \
        sum(1 for v in results.values() if v[0] == "BROKEN")
    n_check = sum(1 for v in results.values() if v[0] == "CHECK")
    print()
    print(f"  broken anchors:  {len(anchor_problems)}")
    print(f"  broken:          {n_broken}")
    print(f"  needs a human:   {n_check}")
    print(f"  wrote link-report.md")
    for u, f, line, why in anchor_problems:
        print(f"    {f}:{line}  {u}")
    if args.fail_on == "none":
        return 0
    if args.fail_on == "anchors":
        return 1 if anchor_problems else 0
    return 1 if n_broken else 0


if __name__ == "__main__":
    sys.exit(main())
