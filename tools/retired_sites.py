#!/usr/bin/env python3
"""Publish preserved material without depending on retired repositories."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
from urllib.parse import urlsplit
from urllib.request import urlopen
import zipfile

from publish_pages import make_alias, page_url, redirect

NAMES = ('dspira-archive', 'cra', 'gr-transient')
BASE = 'https://rail.wvu.edu/dspira/history/sites/'
RELEASE = 'https://github.com/WVURAIL/dspira/releases/tag/preserved-repositories-2026-09-25'
MANIFEST = Path(__file__).resolve().parents[1] / '_data/retired_sites.json'
NOTEBOOK_EXPORTS = {'gbtdrift/index.html', 'labs/05/I_Q_quadrature_sampling.html'}

PDF_OVERRIDES = {
    'cra/Files_uploaded/Hardware&Software_Needs_HornTelescope.pdf': (
        '0b6f3a4193197e66510e2c1e635872900dfcc9f4605c50fd8e0c62df44e1f257',
        'assets/retired/cra/hardware-software-needs.pdf'),
    'cra/Files_uploaded/HardwareSoftware_Needs_for_HornTelescope.pdf': (
        '18265e5ac07a1d097fecbb0d4905c559feb20b95467dc8e74ba02ba5fffe7883',
        'assets/retired/cra/hardware-software-needs-early.pdf'),
}


def original_site_host(source):
    class CanonicalLinks(HTMLParser):
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == 'link' and 'canonical' in attrs.get('rel', '').split():
                self.links.append(urlsplit(attrs.get('href', '')))

    hosts = set()
    for name in NAMES:
        parser = CanonicalLinks()
        parser.links = []
        parser.feed((Path(source) / name / 'index.html').read_text())
        hosts.update(link.hostname for link in parser.links
                     if link.scheme in ('http', 'https') and link.hostname
                     and link.path.rstrip('/') == '/' + name)
    if len(hosts) > 1:
        raise ValueError('Historical site metadata contains conflicting hostnames.')
    return next(iter(hosts), None)


def update_published_text(target, original_host):
    if original_host and original_host != urlsplit(BASE).hostname:
        old, new = original_host.encode(), urlsplit(BASE).hostname.encode()
        for path in target.rglob('*'):
            if path.is_file() and path.suffix.lower() in ('.html', '.md', '.txt', '.py'):
                data = path.read_bytes()
                if old in data:
                    path.write_bytes(data.replace(old, new))


def update_published_copy(target, name, original_host):
    update_published_text(target, original_host)
    # Keep the preserved package intact; only published copies use revised PDFs.
    for relative, (expected, replacement) in PDF_OVERRIDES.items():
        parts = PurePosixPath(relative).parts
        if parts[0] != name:
            continue
        path = target.joinpath(*parts[1:])
        if path.is_file():
            if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError('Historical PDF changed: ' + relative)
            shutil.copy2(MANIFEST.parents[1] / replacement, path)


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
        text = text.replace('https://rail.wvu.edu/' + old + '/', BASE + old + '/')
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
    original_host = original_site_host(source)
    for name in NAMES:
        target = Path(site) / 'history/sites' / name
        shutil.copytree(Path(source) / name, target)
        update_published_copy(target, name, original_host)
        for path in target.rglob('*.html'):
            relative = path.relative_to(target)
            text = path.read_text()
            if (name == 'dspira-archive' and relative.as_posix() in NOTEBOOK_EXPORTS
                    and not (path.parent / 'custom.css').exists()):
                # These exports embed their styles; custom.css was an optional override.
                text = text.replace('<!-- Custom stylesheet, it must be in the same directory as the html file -->', '')
                text = text.replace('<link rel="stylesheet" href="custom.css">', '')
            path.write_text(historical_html(text, name, relative), encoding='utf-8')
        for unwanted in ('CNAME', 'sitemap.xml', 'sitemap.xml.gz', 'feed.xml', 'robots.txt'):
            (target / unwanted).unlink(missing_ok=True)
    update_published_text(Path(site), original_host)


def install_aliases(source, site):
    original_host = original_site_host(source)
    for name in NAMES:
        make_alias(Path(source) / name, Path(site) / name, BASE + name + '/')
        update_published_copy(Path(site) / name, name, original_host)
    target = Path(site) / 'gr-dspira/index.html'
    if target.exists():
        raise ValueError('An existing gr-dspira page would be replaced.')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(redirect('https://rail.wvu.edu/dspira/software/'), encoding='utf-8')
    update_published_text(Path(site), original_host)


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
