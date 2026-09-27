"""Publish hardware documents from one revision of their source repository."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path, PurePosixPath
import re
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from zipfile import BadZipFile, ZipFile

REPOSITORY = 'WVURAIL/dspira-hardware'
MANIFEST = Path(__file__).resolve().parents[1] / '_data/hardware_publication.json'


def download(url):
    headers = {'User-Agent': 'WVU-DSPIRA-publication'}
    if urlsplit(url).netloc == 'api.github.com' and os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        data = response.read(50_000_001)
    if len(data) > 50_000_000:
        raise ValueError('Hardware document exceeds 50 MB: ' + url)
    return data


def validate_revision(revision):
    if not isinstance(revision, str) or not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Hardware publication requires a full commit SHA')
    return revision


def current_revision(fetch=download):
    record = json.loads(fetch(f'https://api.github.com/repos/{REPOSITORY}/commits/main'))
    return validate_revision(record.get('sha'))


def document_names(manifest):
    names = manifest['files']
    if not names or len(names) != len(set(names)):
        raise ValueError('Hardware document list must be nonempty and unique')
    for name in names:
        if (not re.fullmatch(r'[a-z0-9][a-z0-9/-]*\.(pdf|docx)', name)
                or PurePosixPath(name).as_posix() != name):
            raise ValueError('Invalid hardware document path: ' + name)
    return names


def needs_update(manifest, revision, published_url, fetch=download):
    validate_revision(revision)
    names = document_names(manifest)
    try:
        published = json.loads(fetch(published_url))
    except HTTPError as error:
        if error.code == 404:
            return True
        raise
    if not isinstance(published, dict):
        return True
    return (published.get('repository') != REPOSITORY
            or published.get('revision') != revision
            or set(published.get('files', {})) != set(names))


def publish_hardware(site, manifest, revision=None, fetch=download):
    site = Path(site).resolve()
    root = (site / 'assets/hardware').resolve()
    if site not in root.parents:
        raise ValueError('Hardware destination leaves the built site')
    names = document_names(manifest)
    targets = {name: (root / name).resolve() for name in names}
    if any(root not in target.parents for target in targets.values()):
        raise ValueError('Hardware document leaves its publication directory')
    marker = root / 'source.json'
    if marker.is_symlink():
        raise ValueError('Hardware source record cannot be a symbolic link')
    revision = current_revision(fetch) if revision is None else validate_revision(revision)

    def load(name):
        data = fetch(f'https://raw.githubusercontent.com/{REPOSITORY}/{revision}/{name}')
        if name.endswith('.pdf'):
            if not data.startswith(b'%PDF-'):
                raise ValueError('Invalid hardware PDF: ' + name)
        else:
            try:
                with ZipFile(BytesIO(data)) as package:
                    if 'word/document.xml' not in package.namelist() or package.testzip() is not None:
                        raise ValueError('Invalid hardware Word document: ' + name)
            except BadZipFile as error:
                raise ValueError('Invalid hardware Word document: ' + name) from error
        return name, data

    with ThreadPoolExecutor(max_workers=4) as pool:
        documents = dict(pool.map(load, names))
    record = {'repository': REPOSITORY, 'revision': revision, 'files': {}}
    for name, data in documents.items():
        target = targets[name]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        record['files'][name] = hashlib.sha256(data).hexdigest()
    marker.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=MANIFEST)
    parser.add_argument('--published-url', help='Compare the current revision with the published source record')
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    revision = current_revision()
    publish = not args.published_url or needs_update(manifest, revision, args.published_url)
    print('revision=' + revision)
    print('publish=' + str(publish).lower())


if __name__ == '__main__':
    main()
