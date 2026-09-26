#!/usr/bin/env python3
"""Keep old download addresses working after source files move."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlparse
from urllib.request import urlopen

MANIFEST = Path(__file__).resolve().parents[1] / '_data/legacy_assets.json'


def inside(site, name):
    relative = PurePosixPath(name)
    if not name or relative.is_absolute() or '..' in relative.parts or '\\' in name:
        raise ValueError('Unsafe asset path: ' + name)
    target = (site / name).resolve()
    if site not in target.parents:
        raise ValueError('Asset path leaves the site: ' + name)
    return target


def download(url):
    with urlopen(url, timeout=60) as response:
        data = response.read(50_000_001)
    if len(data) > 50_000_000:
        raise ValueError('Compatibility asset exceeds 50 MB: ' + url)
    return data


def publish(site, manifest, fetch=download):
    site = Path(site).resolve()
    entries = manifest['files']
    seen = set()
    for entry in entries:
        old = entry['legacy']
        inside(site, old)
        if old in seen:
            raise ValueError('Repeated legacy address: ' + old)
        seen.add(old)
        if ('source' in entry) == ('url' in entry):
            raise ValueError('Each asset needs one local source or pinned URL: ' + old)
        if 'source' in entry:
            if inside(site, entry['source']) == inside(site, old):
                raise ValueError('An asset cannot alias itself: ' + old)
        else:
            url = urlparse(entry['url'])
            if (url.scheme != 'https' or url.netloc != 'raw.githubusercontent.com'
                    or not re.match(r'^/WVURAIL/[^/]+/[0-9a-f]{40}/.+', url.path)
                    or url.query or url.fragment or not re.fullmatch(r'[0-9a-f]{64}', entry.get('sha256', ''))):
                raise ValueError('External assets require a pinned GitHub revision and SHA256: ' + old)

    for entry in entries:
        target = inside(site, entry['legacy'])
        if 'source' in entry:
            source = inside(site, entry['source'])
            if not source.is_file():
                raise ValueError('Missing published asset: ' + entry['source'])
            data = source.read_bytes()
        else:
            data = fetch(entry['url'])
            if hashlib.sha256(data).hexdigest() != entry['sha256']:
                raise ValueError('Compatibility asset checksum mismatch: ' + entry['legacy'])
        if target.exists() and (not target.is_file() or target.read_bytes() != data):
            raise ValueError('An existing page or asset would be replaced: ' + entry['legacy'])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return len(entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    parser.add_argument('--manifest', type=Path, default=MANIFEST)
    args = parser.parse_args()
    count = publish(args.site, json.loads(args.manifest.read_text()))
    print(f'Preserved {count} legacy download addresses.')


if __name__ == '__main__':
    main()
