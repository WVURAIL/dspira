"""Publish readable notebook pages and downloads without executing their code."""
import argparse
import base64
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import hashlib
from html import escape
import json
from pathlib import Path, PurePosixPath
import re
import struct
from urllib.error import HTTPError
from urllib.parse import quote, urlsplit

from publish_hardware import download
from version_downloads import CanonicalURL

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / '_data/notebooks.json'
REPOSITORY = 'WVURAIL/radio-research-software'


def revision_value(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-f0-9]{40}', value):
        raise ValueError('Notebook sources require a full commit SHA')
    return value


def current_revision(fetch=download):
    return revision_value(json.loads(fetch(f'https://api.github.com/repos/{REPOSITORY}/commits/main'))['sha'])


def inside(root, name):
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '\\' in name or not name:
        raise ValueError('Unsafe notebook path: ' + name)
    target = (root / name).resolve()
    if root.resolve() not in target.parents:
        raise ValueError('Notebook path leaves its directory: ' + name)
    return target


def validate_manifest(entries):
    ids, urls = set(), set()
    for entry in entries:
        key = entry['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', key) or key in ids:
            raise ValueError('Notebook IDs must be unique slugs')
        if not re.fullmatch(r'/[a-z0-9/-]+/', entry['url']) or entry['url'] in urls:
            raise ValueError('Notebook page addresses must be unique local paths')
        if entry.get('repository') not in (None, REPOSITORY):
            raise ValueError('Unrecognized notebook source repository')
        inside(ROOT, entry['source'])
        if not entry['source'].endswith('.ipynb'):
            raise ValueError('Expected an .ipynb source')
        ids.add(key)
        urls.add(entry['url'])
    if not ids:
        raise ValueError('Notebook catalog is empty')


def needs_update(entries, revision, published_url, fetch=download):
    validate_manifest(entries)
    revision_value(revision)
    try:
        published = json.loads(fetch(published_url))
    except HTTPError as error:
        if error.code == 404:
            return True
        raise
    return (published.get('repository') != REPOSITORY or published.get('revision') != revision
            or set(published.get('notebooks', {})) != {entry['id'] for entry in entries})


def render_notebook(data, entry, base):
    import nbformat
    import bleach
    from nbconvert import HTMLExporter
    from bs4 import BeautifulSoup

    notebook = nbformat.reads(data.decode('utf-8'), as_version=4)
    nbformat.validate(notebook)
    preview = deepcopy(notebook)
    descriptions = []
    for number, cell in enumerate(preview.cells, 1):
        outputs = []
        for output in cell.get('outputs', []):
            data = output.get('data', {})
            embedded = BeautifulSoup(data.get('text/html', ''), 'html.parser').select('img[src^="data:image/png;base64,"]')
            if embedded:
                # Older Matplotlib widgets also saved static plots in their HTML.
                outputs.extend(nbformat.v4.new_output(
                    'display_data', data={'image/png': img['src'].split(',', 1)[1]},
                    metadata=output.get('metadata', {})) for img in embedded)
            elif 'application/javascript' not in data:
                outputs.append(output)
        if cell.cell_type == 'code':
            cell.outputs = outputs
        for output in outputs:
            if 'image/png' in output.get('data', {}):
                descriptions.append(output.get('metadata', {}).get('dspira_alt')
                                    or f'Plot from notebook cell {number}. The code above gives its variables and plotting parameters.')
    if entry.get('plot_descriptions'):
        if len(entry['plot_descriptions']) != len(descriptions):
            raise ValueError('Notebook plot descriptions need to match the saved plots')
        descriptions = entry['plot_descriptions']
    exporter = HTMLExporter(template_name='basic', sanitize_html=False,
                            exclude_input_prompt=True, exclude_output_prompt=True)
    html, _ = exporter.from_notebook_node(preview)
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.select('script, style, iframe, object, embed, form, .anchor-link'):
        tag.decompose()
    for heading in soup.find_all(re.compile(r'^h[1-6]$')):
        heading.name = 'h' + str(min(6, int(heading.name[1]) + 1))
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.lower().startswith('on'):
                del tag[attr]
    images, image_number = {}, 0
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.startswith('data:image/png;base64,'):
            raw = base64.b64decode(src.split(',', 1)[1], validate=True)
            if not raw.startswith(b'\x89PNG\r\n\x1a\n'):
                raise ValueError('Invalid notebook PNG')
            image_number += 1
            path = f"assets/notebooks/{entry['id']}/figure-{image_number:02d}-{hashlib.sha256(raw).hexdigest()[:12]}.png"
            images[path] = raw
            img['src'] = base + path
            img['alt'] = descriptions[image_number - 1]
            width, height = struct.unpack('>II', raw[16:24])
            img['width'], img['height'] = str(width), str(height)
        elif not img.get('alt'):
            raise ValueError('Notebook image needs a description: ' + src)
        img['loading'], img['decoding'] = 'lazy', 'async'
    if image_number != len(descriptions):
        raise ValueError('Notebook image output changed unexpectedly')
    # Sanitize after extracting plots so ordinary notebook headings remain HTML.
    safe_html = bleach.clean(
        str(soup),
        tags={'a', 'abbr', 'b', 'blockquote', 'br', 'caption', 'code', 'dd', 'del',
              'div', 'dl', 'dt', 'em', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i',
              'img', 'li', 'ol', 'p', 'pre', 's', 'small', 'span', 'strong', 'sub',
              'sup', 'table', 'tbody', 'td', 'th', 'thead', 'tr', 'ul'},
        attributes={'*': ['class', 'id', 'title'], 'a': ['href'],
                    'img': ['src', 'alt', 'width', 'height', 'loading', 'decoding'],
                    'ol': ['start'], 'td': ['colspan', 'rowspan'],
                    'th': ['colspan', 'rowspan', 'scope']},
        protocols={'http', 'https', 'mailto'}, strip=True,
    )
    sections = [(h.get('id'), h.get_text(' ', strip=True)) for h in soup.select('h2[id], h3[id]')]
    toc = ''
    if sections:
        toc = '<details class="notebook-sections"><summary>Sections in this example</summary><ul>'
        toc += ''.join(f'<li><a href="#{quote(key, safe="")}">{escape(title)}</a></li>' for key, title in sections)
        toc += '</ul></details>'
    saved_outputs = sum(len(cell.get('outputs', [])) for cell in preview.cells)
    status = ('Saved outputs are shown below.' if saved_outputs else
              'This notebook has no saved outputs. The preview shows its explanations and code.')
    return toc + f'<p class="notebook-status">{status}</p>\n' + safe_html, images, saved_outputs


def publish_notebooks(site, entries, revision=None, fetch=download, source_root=ROOT):
    site, source_root = Path(site).resolve(), Path(source_root).resolve()
    validate_manifest(entries)
    revision = current_revision(fetch) if revision is None else revision_value(revision)
    canonical = CanonicalURL((site / 'index.html').read_text(encoding='utf-8')).url
    if not canonical:
        raise ValueError('The built site needs a canonical address')
    base = urlsplit(canonical).path.rstrip('/') + '/'

    def load(entry):
        if entry.get('repository'):
            return fetch(f"https://raw.githubusercontent.com/{REPOSITORY}/{revision}/{entry['source']}")
        return inside(source_root, entry['source']).read_bytes()

    with ThreadPoolExecutor(max_workers=4) as pool:
        notebooks = list(pool.map(load, entries))
    writes = {}
    record = {'repository': REPOSITORY, 'revision': revision, 'notebooks': {}}
    for entry, data in zip(entries, notebooks):
        page = inside(site, entry['url'].strip('/') + '/index.html')
        template = page.read_text(encoding='utf-8')
        start, end = f"<!-- notebook:{entry['id']}:start -->", f"<!-- notebook:{entry['id']}:end -->"
        if template.count(start) != 1 or template.count(end) != 1:
            raise ValueError('Missing notebook placeholder: ' + entry['id'])
        content, images, outputs = render_notebook(data, entry, base)
        download_path = f"assets/notebooks/{entry['id']}/{entry['id']}.ipynb"
        writes[inside(site, download_path)] = data
        for name, raw in images.items():
            writes[inside(site, name)] = raw
        before, rest = template.split(start)
        _, after = rest.split(end)
        # Keep delimiters so rerunning publication refreshes the same page.
        writes[page] = (before + start + content + end + after).encode()
        record['notebooks'][entry['id']] = {
            'source': entry['source'], 'sha256': hashlib.sha256(data).hexdigest(),
            'download': download_path, 'images': len(images), 'saved_outputs': outputs,
        }
    marker = inside(site, 'assets/notebooks/source.json')
    writes[marker] = (json.dumps(record, indent=2) + '\n').encode()
    # Validate every source before replacing any published page.
    for path, data in writes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path)
    parser.add_argument('--revision')
    parser.add_argument('--published-url')
    args = parser.parse_args()
    entries = json.loads(MANIFEST.read_text())
    revision = args.revision or current_revision()
    if args.site:
        result = publish_notebooks(args.site, entries, revision)
        print(f"Published {len(result['notebooks'])} notebook examples.")
    else:
        publish = not args.published_url or needs_update(entries, revision, args.published_url)
        print('revision=' + revision)
        print('publish=' + str(publish).lower())


if __name__ == '__main__':
    main()
