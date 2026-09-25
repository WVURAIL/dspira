import tempfile
import unittest
from pathlib import Path

from publish_pages import add_archive_paths, make_alias, page_url, redirect


class MigrationTests(unittest.TestCase):
    def test_page_paths(self):
        self.assertEqual(page_url('https://example.org/dspira/', Path('index.html')), 'https://example.org/dspira/')
        self.assertEqual(page_url('/dspira', Path('labs/01/index.html')), '/dspira/labs/01/')
        self.assertEqual(page_url('/dspira', Path('a file.html')), '/dspira/a%20file.html')

    def test_redirect_preserves_query_and_fragment(self):
        result = redirect('/dspira/a')
        self.assertIn('window.location.search + window.location.hash', result)
        self.assertIn('href="/dspira/a"', result)
        self.assertIn('content="noindex"', result)

    def test_alias_preserves_downloads(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            source.mkdir()
            (source / 'index.html').write_text('original')
            (source / 'kit.pdf').write_bytes(b'%PDF-1.7 original bytes')
            (source / 'CNAME').write_text('example.org')
            (source / 'sitemap.xml').write_text('old sitemap')
            make_alias(source, root / 'alias', '/dspira/')
            self.assertEqual((root / 'alias/kit.pdf').read_bytes(), (source / 'kit.pdf').read_bytes())
            self.assertFalse((root / 'alias/CNAME').exists())
            self.assertFalse((root / 'alias/sitemap.xml').exists())
            self.assertEqual((source / 'index.html').read_text(), 'original')
            self.assertIn('/dspira/', (root / 'alias/index.html').read_text())

    def test_archive_does_not_replace_current_content(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for folder in ('site', 'archive'):
                (root / folder).mkdir()
                (root / folder / 'index.html').write_text(folder)
            (root / 'archive/lab.html').write_text('old lab')
            (root / 'archive/test.grc').write_bytes(b'flowgraph')
            (root / 'archive/sitemap.xml').write_text('archive sitemap')
            self.assertEqual(add_archive_paths(root / 'site', root / 'archive', '/dspira-archive/'), 2)
            self.assertEqual((root / 'site/index.html').read_text(), 'site')
            self.assertIn('/dspira-archive/lab.html', (root / 'site/lab.html').read_text())
            self.assertEqual((root / 'site/test.grc').read_bytes(), b'flowgraph')
            self.assertFalse((root / 'site/sitemap.xml').exists())

    def test_rejects_nested_destinations(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                make_alias(directory, Path(directory) / 'alias', '/dspira/')


if __name__ == '__main__':
    unittest.main()
