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


def make_alias(source, destination, canonical):
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError('Alias and source directories must be separate.')
    if destination.exists():
        raise ValueError('Alias destination must not already exist.')
    shutil.copytree(source, destination)
    for path in destination.rglob('*.html'):
        path.write_text(redirect(page_url(canonical, path.relative_to(destination))), encoding='utf-8')
    for name in ('CNAME', 'sitemap.xml', 'sitemap.xml.gz', 'feed.xml'):
        (destination / name).unlink(missing_ok=True)


def add_archive_paths(site, archive, archive_url):
    site, archive = Path(site).resolve(), Path(archive).resolve()
    if site == archive or site in archive.parents or archive in site.parents:
        raise ValueError('Archive and site directories must be separate.')
    added = 0
    for source in archive.rglob('*'):
        if not source.is_file():
            continue
        relative = source.relative_to(archive)
        if relative.as_posix() in ('CNAME', 'sitemap.xml', 'sitemap.xml.gz', 'feed.xml', 'robots.txt'):
            continue
        target = site / relative
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix.lower() == '.html':
            target.write_text(redirect(page_url(archive_url, relative)), encoding='utf-8')
        else:
            shutil.copy2(source, target)
        added += 1
    return added


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', required=True, type=Path)
    parser.add_argument('--alias', type=Path)
    parser.add_argument('--canonical', default='https://wvurail.org/dspira/')
    parser.add_argument('--archive', type=Path)
    parser.add_argument('--archive-url', default='https://wvurail.org/dspira-archive/')
    args = parser.parse_args()
    if args.alias:
        make_alias(args.site, args.alias, args.canonical)
        print('Created compatibility site:', args.alias)
    if args.archive:
        print('Preserved archive paths:', add_archive_paths(args.site, args.archive, args.archive_url))


if __name__ == '__main__':
    main()
