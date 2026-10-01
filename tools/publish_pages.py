#!/usr/bin/env python3
"""Preserve older site addresses during the DSPIRA migration."""

import argparse
import html
import json
from pathlib import Path
import shutil
from urllib.parse import quote


def redirect(target):
    escaped = html.escape(target, quote=True)
    script_target = json.dumps(target).replace('<', '\\u003c')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>This DSPIRA page has moved</title>
<link rel="canonical" href="{escaped}">
<meta http-equiv="refresh" content="0; url={escaped}">
<script>window.location.replace({script_target} + window.location.search + window.location.hash);</script>
</head><body><main><h1>This page has moved</h1>
<p><a href="{escaped}">Continue to DSPIRA</a>.</p></main></body></html>
'''


def page_url(base, relative):
    path = relative.as_posix()
    if path == 'index.html':
        path = ''
    elif path.endswith('/index.html'):
        path = path[:-10]
    return base.rstrip('/') + '/' + quote(path, safe='/')


def make_alias(source, destination, canonical, exclude=()):
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError('Alias and source directories must be separate.')
    if destination.exists():
        raise ValueError('Alias destination must not already exist.')
    excluded = set()
    for value in exclude:
        relative = Path(value)
        if relative.is_absolute() or '..' in relative.parts or relative == Path('.'):
            raise ValueError('Excluded alias paths must be relative and stay inside the source.')
        excluded.add(relative.as_posix())

    def ignore(directory, names):
        relative = Path(directory).relative_to(source)
        return [name for name in names if (relative / name).as_posix() in excluded]

    shutil.copytree(source, destination, ignore=ignore if excluded else None)
    for path in destination.rglob('*.html'):
        path.write_text(redirect(page_url(canonical, path.relative_to(destination))), encoding='utf-8')
    for name in ('CNAME', 'sitemap.xml', 'sitemap.xml.gz', 'feed.xml'):
        (destination / name).unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', required=True, type=Path)
    parser.add_argument('--alias', type=Path)
    parser.add_argument('--canonical', default='https://rail.wvu.edu/dspira/')
    parser.add_argument('--exclude', action='append', default=[],
                        help='Relative source path to omit from an alias copy; repeat for multiple paths.')
    args = parser.parse_args()
    if args.alias:
        make_alias(args.site, args.alias, args.canonical, args.exclude)
        print('Created compatibility site:', args.alias)


if __name__ == '__main__':
    main()
