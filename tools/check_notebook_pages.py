"""Check published notebook code, plots, downloads, and navigation."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
import nbformat

from publish_notebooks import MANIFEST, inside, revision_value
from version_downloads import CanonicalURL


def check(site):
    site = Path(site).resolve()
    base = urlsplit(CanonicalURL((site / 'index.html').read_text()).url).path.rstrip('/') + '/'
    entries = json.loads(MANIFEST.read_text())
    record = json.loads((site / 'assets/notebooks/source.json').read_text())
    revision_value(record['revision'])
    assert set(record['notebooks']) == {entry['id'] for entry in entries}
    catalog = BeautifulSoup((site / 'notebooks/index.html').read_text(), 'html.parser')
    plot_count = 0
    for entry in entries:
        key = entry['id']
        saved = record['notebooks'][key]
        data = inside(site, saved['download']).read_bytes()
        assert hashlib.sha256(data).hexdigest() == saved['sha256'], key + ': changed download'
        notebook = nbformat.reads(data.decode(), as_version=4)
        nbformat.validate(notebook)
        soup = BeautifulSoup(inside(site, entry['url'].strip('/') + '/index.html').read_text(), 'html.parser')
        body = soup.select_one('.notebook-example')
        assert body and body.select('.cell'), key + ': missing preview'
        assert len(soup.select('h1')) == 1, key + ': wrong page heading count'
        assert not body.select('script, iframe, object, embed, style'), key + ': active content'
        expected = [cell.source.strip('\n') for cell in notebook.cells if cell.cell_type == 'code']
        actual = [cell.get_text().strip('\n') if cell.get_text().strip() else ''
                  for cell in body.select('.input_area pre')]
        assert actual == expected, key + ': displayed code differs from the notebook'
        assert soup.find('a', download=key + '.ipynb'), key + ': missing download button'
        assert catalog.find('a', href=base + entry['url'].lstrip('/')), key + ': missing catalog link'
        for link in body.select('a[href^="#"]'):
            assert soup.find(id=unquote(link['href'][1:])), key + ': broken section link'
        images = body.select('img')
        assert len(images) == saved['images'], key + ': missing plot'
        for image in images:
            assert image.get('alt', '').strip(), key + ': missing plot description'
            assert int(image['width']) > 0 and int(image['height']) > 0
            assert image['src'].startswith(base + 'assets/notebooks/' + key + '/')
            path = inside(site, unquote(image['src'][len(base):]))
            assert hashlib.sha256(path.read_bytes()).hexdigest()[:12] in path.name, key + ': changed plot'
        plot_count += len(images)
        for link in soup.select('a[download]'):
            path = unquote(urlsplit(link['href']).path)
            assert path.startswith(base) and inside(site, path[len(base):]).is_file(), key + ': missing download'
    print(f'Checked {len(entries)} notebook pages, matching downloads, and {plot_count} plots.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    check(parser.parse_args().site)
