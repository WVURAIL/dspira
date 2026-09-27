"""Check notebook publication, source integrity, and static-only rendering."""
import base64
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from urllib.error import HTTPError

import nbformat
from bs4 import BeautifulSoup
from publish_notebooks import REPOSITORY, needs_update, publish_notebooks, render_notebook

REVISION = 'a' * 40
PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII=')


def notebook_bytes():
    output = nbformat.v4.new_output('display_data', data={'image/png': base64.b64encode(PNG).decode()},
                                   metadata={'dspira_alt': 'A test plot with one pixel.'})
    notebook = nbformat.v4.new_notebook(cells=[
        nbformat.v4.new_markdown_cell('# Example\n\nA measured result.'),
        nbformat.v4.new_code_cell('raise RuntimeError("This code must never execute")', outputs=[output]),
    ])
    return nbformat.writes(notebook).encode()


class NotebookPublication(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.site = self.root / 'site'
        self.site.mkdir()
        (self.site / 'index.html').write_text('<link rel="canonical" href="https://example.edu/preview/dspira/">')
        self.entries = [{'id': 'example', 'url': '/notebooks/example/', 'source': 'examples/example.ipynb', 'repository': REPOSITORY}]
        self.page = self.site / 'notebooks/example/index.html'
        self.page.parent.mkdir(parents=True)
        self.page.write_text('<h1>Example</h1><!-- notebook:example:start -->pending<!-- notebook:example:end -->')
        self.data = notebook_bytes()
        self.calls = []

    def tearDown(self):
        self.temp.cleanup()

    def fetch(self, url):
        self.calls.append(url)
        if url.endswith('/commits/main'):
            return json.dumps({'sha': REVISION}).encode()
        self.assertIn('/' + REVISION + '/', url)
        return self.data

    def test_source_bytes_outputs_base_path_and_repeat_publication(self):
        record = publish_notebooks(self.site, self.entries, fetch=self.fetch)
        data = self.site / record['notebooks']['example']['download']
        self.assertEqual(data.read_bytes(), self.data)
        self.assertEqual(record['notebooks']['example']['sha256'], hashlib.sha256(self.data).hexdigest())
        soup = BeautifulSoup(self.page.read_text(), 'html.parser')
        self.assertEqual(len(soup.select('h1')), 1)
        self.assertEqual(soup.h2.get_text(), 'Example')
        self.assertIn('A measured result.', [p.get_text() for p in soup.select('p')])
        self.assertNotIn('<h1', soup.get_text())
        self.assertEqual(soup.select_one('.notebook-sections a')['href'], '#' + soup.h2['id'])
        self.assertIn('raise RuntimeError', soup.get_text())
        image = soup.find('img')
        self.assertTrue(image['src'].startswith('/preview/dspira/assets/notebooks/'))
        self.assertEqual(image['alt'], 'A test plot with one pixel.')
        self.assertEqual((image['width'], image['height']), ('1', '1'))
        original = self.page.read_bytes()
        publish_notebooks(self.site, self.entries, REVISION, fetch=self.fetch)
        self.assertEqual(self.page.read_bytes(), original)
        self.assertEqual(sum(url.endswith('/commits/main') for url in self.calls), 1)

    def test_missing_outputs_are_labeled_and_active_content_is_removed(self):
        notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_markdown_cell(
            '<script>alert(1)</script><a href="javascript:alert(1)" onclick="alert(2)">Unsafe link</a>'),
                                                 nbformat.v4.new_code_cell('print(42)')])
        html, images, outputs = render_notebook(nbformat.writes(notebook).encode(), self.entries[0], '/dspira/')
        self.assertIn('no saved outputs', html)
        soup = BeautifulSoup(html, 'html.parser')
        self.assertFalse(soup.find('script'))
        self.assertFalse(soup.find('a').get('href'))
        self.assertFalse(soup.find('a').get('onclick'))
        self.assertEqual((images, outputs), ({}, 0))

    def test_invalid_download_preserves_existing_page_and_assets(self):
        publish_notebooks(self.site, self.entries, REVISION, fetch=self.fetch)
        before = {p: p.read_bytes() for p in self.site.rglob('*') if p.is_file()}
        self.data = b'not a notebook'
        with self.assertRaises(Exception):
            publish_notebooks(self.site, self.entries, REVISION, fetch=self.fetch)
        self.assertEqual(before, {p: p.read_bytes() for p in self.site.rglob('*') if p.is_file()})

    def test_static_plots_survive_legacy_widget_html(self):
        output = nbformat.v4.new_output('display_data', data={
            'text/html': '<div><script>alert(1)</script><img src="data:image/png;base64,'
                         + base64.b64encode(PNG).decode() + '"></div>'})
        notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell('plot(samples)', outputs=[output])])
        html, images, outputs = render_notebook(nbformat.writes(notebook).encode(), self.entries[0], '/dspira/')
        soup = BeautifulSoup(html, 'html.parser')
        self.assertFalse(soup.find('script'))
        self.assertEqual((len(images), outputs), (1, 1))
        self.assertIn('cell 1', soup.img['alt'])
        self.assertEqual(next(iter(images.values())), PNG)

    def test_unsafe_source_and_publication_symlinks_are_rejected(self):
        entries = deepcopy(self.entries)
        entries[0]['source'] = '../example.ipynb'
        with self.assertRaises(ValueError):
            publish_notebooks(self.site, entries, REVISION, fetch=self.fetch)
        (self.site / 'assets').symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            publish_notebooks(self.site, self.entries, REVISION, fetch=self.fetch)

    def test_local_source_and_daily_change_detection(self):
        path = self.root / 'examples/example.ipynb'
        path.parent.mkdir()
        path.write_bytes(self.data)
        entries = deepcopy(self.entries)
        entries[0].pop('repository')
        record = publish_notebooks(self.site, entries, REVISION, fetch=self.fetch, source_root=self.root)
        self.assertFalse(self.calls)
        fetch = lambda url: json.dumps(record).encode()
        self.assertFalse(needs_update(entries, REVISION, 'https://example.edu/source.json', fetch))
        self.assertTrue(needs_update(entries, 'b' * 40, 'https://example.edu/source.json', fetch))
        def missing(url):
            raise HTTPError(url, 404, 'Not found', {}, None)
        self.assertTrue(needs_update(entries, REVISION, 'https://example.edu/source.json', missing))


if __name__ == '__main__':
    unittest.main()
