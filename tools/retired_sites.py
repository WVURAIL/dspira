#!/usr/bin/env python3
"""Publish preserved material without depending on retired repositories."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
from urllib.request import urlopen
import zipfile

from publish_pages import make_alias, page_url, redirect

NAMES = ('dspira-archive', 'cra', 'gr-transient')
BASE = 'https://wvurail.org/dspira/history/sites/'
RELEASE = 'https://github.com/WVURAIL/dspira/releases/tag/preserved-repositories-2026-09-25'
MANIFEST = Path(__file__).resolve().parents[1] / '_data/retired_sites.json'


def extract_verified(package, destination, expected_sha256):
    destination = Path(destination)
    if destination.exists():
        raise ValueError('Use a new destination for preserved sites.')
    if hashlib.sha256(Path(package).read_bytes()).hexdigest() != expected_sha256:
        raise ValueError('The preserved site checksum does not match.')
    with zipfile.ZipFile(package) as archive:
        seen = set()
        for member in archive.infolist():
            path = PurePosixPath(member.filename)
            mode = member.external_attr >> 16
            if (path.is_absolute() or not path.parts or path.parts[0] not in NAMES
                    or '..' in path.parts or '\\' in member.filename
                    or stat.S_ISLNK(mode) or member.filename in seen):
                raise ValueError('Unsafe or repeated archive member: ' + member.filename)
            seen.add(member.filename)
        for name in NAMES:
            if name + '/index.html' not in seen:
                raise ValueError('Missing historical site: ' + name)
        archive.extractall(destination)


def fetch(destination, package=None):
    manifest = json.loads(MANIFEST.read_text())
    if package:
        extract_verified(package, destination, manifest['sha256'])
        return
    with tempfile.TemporaryDirectory() as temporary:
        download = Path(temporary) / 'retired-sites.zip'
        with urlopen(manifest['url'], timeout=120) as response, download.open('wb') as output:
            shutil.copyfileobj(response, output)
        extract_verified(download, destination, manifest['sha256'])


def historical_html(text, name, relative):
    if not re.search(r'<body\b', text, flags=re.I):
        text = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                '<title>Historical DSPIRA material</title></head><body>' + text + '</body></html>')
    for old in NAMES:
        text = text.replace('https://wvurail.org/' + old + '/', BASE + old + '/')
        text = re.sub(r'(?<=[\"\x27(])/' + re.escape(old) + '/', '/dspira/history/sites/' + old + '/', text)
    # The source packages replace repository browsing and source-download links.
    text = re.sub(r'https?://github\.com/WVURAIL/(?:dspira-archive|cra|gr-transient|gr-dspira)(?:[/?#][^\s<>\"\x27]*)?',
                  RELEASE, text)
    text = re.sub(r'<link\b[^>]*rel=[\"\x27]canonical[\"\x27][^>]*>', '', text, flags=re.I)
    text = re.sub(r'<meta\b[^>]*name=[\"\x27]robots[\"\x27][^>]*>', '', text, flags=re.I)
    metadata = ('<meta name="robots" content="noindex">\n<link rel="canonical" href="'
                + page_url(BASE + name, relative) + '">\n')
    text = re.sub(r'</head>', lambda match: metadata + match[0], text, count=1, flags=re.I)
    banner = ('<aside aria-label="Historical material"><p><strong>Historical material.</strong> '
              '<a href="/dspira/">Visit current DSPIRA lessons</a> or '
              '<a href="/dspira/history/">download the preserved source and history</a>.</p></aside>')
    return re.sub(r'(<body\b[^>]*>)', lambda match: match[0] + banner, text, count=1, flags=re.I)


def install_history(source, site):
    for name in NAMES:
        target = Path(site) / 'history/sites' / name
        shutil.copytree(Path(source) / name, target)
        for path in target.rglob('*.html'):
            path.write_text(historical_html(path.read_text(), name, path.relative_to(target)), encoding='utf-8')
        for unwanted in ('CNAME', 'sitemap.xml', 'sitemap.xml.gz', 'feed.xml', 'robots.txt'):
            (target / unwanted).unlink(missing_ok=True)


def install_aliases(source, site):
    for name in NAMES:
        make_alias(Path(source) / name, Path(site) / name, BASE + name + '/')
    target = Path(site) / 'gr-dspira/index.html'
    if target.exists():
        raise ValueError('An existing gr-dspira page would be replaced.')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(redirect('https://wvurail.org/dspira/software/'), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    download = sub.add_parser('fetch')
    download.add_argument('--destination', type=Path, required=True)
    download.add_argument('--package', type=Path)
    for name in ('history', 'aliases'):
        command = sub.add_parser(name)
        command.add_argument('--source', type=Path, required=True)
        command.add_argument('--site', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'fetch':
        fetch(args.destination, args.package)
    elif args.command == 'history':
        install_history(args.source, args.site)
    else:
        install_aliases(args.source, args.site)


if __name__ == '__main__':
    main()
