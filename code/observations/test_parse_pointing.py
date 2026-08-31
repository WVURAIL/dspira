"""Checks the pointing strings the hdf5_sink block actually produces.

Run it from this directory, no arguments:

    python3 test_parse_pointing.py

The pointing box in the GNU Radio hdf5_sink block is free text - whatever the
observer types goes into the file. The parser's contract is: read the string
if it is unambiguous, return None if it is not. A skipped file gets noticed;
a sample quietly placed at the wrong spot on a sky map does not.

Why this file exists, part 1: until 2026 the map script removed the last
character of the elevation before reading it, so 'A180E40' was read as
elevation 4. Nothing failed, nothing warned; the map was just wrong.

Why this file exists, part 2: the first replacement parser matched the
trailing 'a' of ordinary words, so 'Data 5 A180E40' was read as azimuth 5 -
and its test suite passed, because every test case had been written to
confirm the parser rather than to break it. The REJECTED section below is
the lesson learned: most of these cases are strings the parser must refuse.
"""

import sys
from map_h1_hdf5_drift import parse_pointing

ACCEPTED = [
    # (pointing string, expected (az, el), note)
    ("A180E40",        (180.0, 40.0), "the obvious way to write it"),
    ("A180E40.",       (180.0, 40.0), "trailing period - common in older files"),
    ("A180E40d",       (180.0, 40.0), "trailing letter"),
    ("Az180El40",      (180.0, 40.0), "spelled out"),
    ("AZ 180 EL 40",   (180.0, 40.0), "spaced out"),
    ("azimuth=180, elevation=40", (180.0, 40.0), "written as assignments"),
    ("180,40",         (180.0, 40.0), "bare pair, read as az then el"),
    ("180 40",         (180.0, 40.0), "bare pair, space separated"),
    ("A180E4",         (180.0, 4.0),  "genuinely 4 degrees, read as 4"),
    ("A180.5E40.25",   (180.5, 40.25), "decimals"),
    ("A180E-5",        (180.0, -5.0), "below the horizon, read as given"),
    ("El40 Az180",     (180.0, 40.0), "elevation first"),
    ("ALT 40 AZ 180",  (180.0, 40.0), "altitude/azimuth order"),
    ("elevation 40 azimuth 180", (180.0, 40.0), "elevation first, spelled out"),
    ("Data 5A180E40",  (180.0, 40.0), "label ending in a digit, then pointing"),
    ("scan_A180E40",   (180.0, 40.0), "label joined by an underscore"),
]

# Strings with a label containing its own number, where an earlier parser
# grabbed the label's number as the azimuth. The az/el markers make these
# readable despite the extra number.
LABELLED = [
    ("Data 5 A180E40",       (180.0, 40.0), "was read as azimuth 5"),
    ("Path 3 AZ180 EL40",    (180.0, 40.0), "was read as azimuth 3"),
    ("Antenna 2 AZ180 EL40", (180.0, 40.0), "was read as azimuth 2"),
    ("Alpha 3 A180E40",      (180.0, 40.0), "label word starts with A"),
]

REJECTED = [
    # (pointing string, note) - all of these must return None.
    ("AZ,EL",            "the block's placeholder"),
    ("",                 "empty"),
    ("south",            "words, no numbers"),
    ("A180",             "azimuth only"),
    ("scan 3: 180,40",   "three bare numbers - is azimuth 3 or 180?"),
    ("2024-05-01 180,40","a date supplies extra numbers"),
    ("A400E40",          "azimuth out of range"),
    ("A180E140",         "elevation out of range"),
    ("500,40",           "bare pair, azimuth out of range"),
    ("180,95",           "bare pair, elevation out of range"),
]


def main():
    failures = []
    print("-- must parse --")
    for s, expected, note in ACCEPTED + LABELLED:
        got = parse_pointing(s)
        ok = got == expected
        print("%-4s %-30r -> %-16s  %s" % ("ok" if ok else "FAIL", s, got, note))
        if not ok:
            failures.append((s, expected, got))

    print("-- must be rejected --")
    for s, note in REJECTED:
        got = parse_pointing(s)
        ok = got is None
        print("%-4s %-30r -> %-16s  %s" % ("ok" if ok else "FAIL", s, got, note))
        if not ok:
            failures.append((s, None, got))

    total = len(ACCEPTED) + len(LABELLED) + len(REJECTED)
    print()
    if failures:
        print("%d of %d failed:" % (len(failures), total))
        for s, expected, got in failures:
            print("  %r  expected %s, got %s" % (s, expected, got))
        return 1
    print("all %d cases pass" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
