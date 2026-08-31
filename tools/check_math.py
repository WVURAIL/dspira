#!/usr/bin/env python3
"""
Are the displayed equations actually displayed?

    python3 tools/check_math.py                 # about a tenth of a second
    python3 tools/check_math.py --self-test     # break it on purpose

Nothing to install: standard library only. Run it from the top of the repository.

WHY THIS EXISTS

kramdown only treats

    $$
    f(x) = |x|
    $$

as a displayed equation when the opening $$ begins a block — which means a blank
line above it. Write the same three lines directly underneath a sentence and
kramdown reads the whole thing as one paragraph, so the equation renders *inline*:
body size, mid-sentence, where a centred line was meant.

Nothing warns you. The build passes, the equation is correct, MathJax renders it
happily. It is just in the wrong place, and inline maths does not wrap — one
"$$" in the wrong column and the page scrolls sideways on a phone.

One did. /dsplab-fourier1/ leaked 211px at 320px because a triangle-wave
definition sat directly under "The triangular wave is defined as:". It took two
CI rounds to find, because the equation looked fine in the report and the fault
was three lines of markdown with a blank line missing.

WHAT IT DOES NOT COVER

Whether the maths is right, or whether it renders well. It checks one thing: that
every $$ fence has a blank line on its outside, so kramdown sees a block.
"""

import argparse
import os
import re
import sys

SKIP_DIRS = {"_site", ".git", "node_modules", "vendor", ".jekyll-cache", "assets"}
CODE_FENCE = re.compile(r"^\s*(```|~~~)")


def markdown_files(root="."):
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


def fences(lines):
    """Line numbers of every standalone $$, ignoring anything inside a code fence."""
    out, in_code = [], False
    for n, line in enumerate(lines, 1):
        if CODE_FENCE.match(line):
            in_code = not in_code
            continue
        if not in_code and line.strip() == "$$":
            out.append(n)
    return out


def check_file(path):
    """Faults in one file, as (line, kind, the neighbouring line)."""
    try:
        lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    except OSError:
        return []
    marks = fences(lines)
    faults = []
    if len(marks) % 2:
        faults.append((marks[-1], "unpaired", ""))
        marks = marks[:-1]
    # They alternate: the first opens, the second closes, and so on.
    for i, n in enumerate(marks):
        opening = i % 2 == 0
        neighbour = n - 2 if opening else n           # 0-based index either side
        if not 0 <= neighbour < len(lines):
            continue                                  # the edge of the file
        beside = lines[neighbour].strip()
        # Blank, or another fence — two equations back to back are two blocks.
        if not beside or beside == "$$":
            continue
        faults.append((n, "opening" if opening else "closing", beside[:64]))
    return faults


# Only the first of these is a bug today. The second is how the first gets made:
# every trapped equation in this repository sits under a line of prose that was
# itself written under a closing fence.
WHY = {
    "opening": ("renders inline instead of displayed — kramdown needs a blank "
                "line above the $$"),
    "closing": ("needs a blank line below the $$, or the next equation written "
                "here renders inline"),
    "unpaired": "this $$ has no partner",
}


def run(root=".", quiet=False):
    total, files = 0, 0
    for path in markdown_files(root):
        faults = check_file(path)
        if not faults:
            continue
        files += 1
        total += len(faults)
        rel = os.path.relpath(path, root)
        for line, kind, neighbour in faults:
            if not quiet:
                print(f"::error file={rel},line={line}::{rel}:{line} {WHY[kind]}")
                if neighbour:
                    print(f"           beside: {neighbour!r}")
    if not quiet:
        if total:
            print(f"\n{total} fence(s) in {files} file(s) are not separated from "
                  f"the text around them.")
        else:
            print("every $$ fence starts a block; the displayed equations are displayed.")
    return 1 if total else 0


GOOD = """Some prose first.

$$
f(x) = |x|
$$

And prose after.
"""

# The shape that shipped: a fence tucked straight under the sentence introducing it.
NO_BLANK_ABOVE = """The triangular wave is defined as:
$$
f(x) = |x|
$$

And prose after.
"""

NO_BLANK_BELOW = """Some prose first.

$$
f(x) = |x|
$$
for all values of x.
"""

# A fence inside a code sample is a code sample. Crying wolf here would be worse
# than saying nothing, because the answer would be to switch the check off.
IN_CODE = """Some prose first.

```
$$
f(x) = |x|
$$
```

And prose after.
"""

# Inline maths in a sentence is inline maths on purpose. Only a lone $$ is a fence.
INLINE = "A signal $$x(t)$$ is periodic if $$x(t) = x(t + T)$$ for all $$t$$.\n"


def self_test():
    import shutil
    import tempfile
    ok = True
    for name, text, expect_fail in (
            ("blank lines both sides", GOOD, False),
            ("fence under a sentence", NO_BLANK_ABOVE, True),
            ("prose under a fence", NO_BLANK_BELOW, True),
            ("$$ inside a code fence", IN_CODE, False),
            ("inline maths in a sentence", INLINE, False)):
        d = tempfile.mkdtemp()
        open(os.path.join(d, "page.md"), "w", encoding="utf-8").write(text)
        code = run(d, quiet=True)
        good = (code == 1) if expect_fail else (code == 0)
        ok &= good
        print(f"  {'ok  ' if good else 'FAIL'} {name:28} "
              f"{'caught' if code else 'quiet'}")
        shutil.rmtree(d)
    print("self-test passed" if ok else "::error::self-test FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true",
                    help="break a page on purpose and check this script notices")
    args = ap.parse_args()
    return self_test() if args.self_test else run()


if __name__ == "__main__":
    sys.exit(main())
