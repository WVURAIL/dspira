import tempfile
import unittest
from pathlib import Path

from publish_pages import make_alias, page_url, redirect


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

    def test_explicit_alias_exclusion_preserves_existing_downloads_and_redirects(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            originals = {
                'index.html': b'current homepage',
                'history/index.html': b'current history page',
                'history/experiments/index.html': b'current experiment catalog',
                'assets/history/new-recovery.zip': b'new canonical download',
                'assets/lessons/existing.pdf': b'existing download bytes',
                'assets/history-notes.txt': b'not part of excluded directory',
            }
            for relative, data in originals.items():
                path = source / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            alias = root / 'alias'
            make_alias(source, alias, '/dspira/', exclude=['assets/history'])
            self.assertFalse((alias / 'assets/history').exists())
            for relative in ('assets/lessons/existing.pdf', 'assets/history-notes.txt'):
                self.assertEqual((alias / relative).read_bytes(), originals[relative])
            self.assertIn('/dspira/history/', (alias / 'history/index.html').read_text())
            self.assertIn('/dspira/history/experiments/', (alias / 'history/experiments/index.html').read_text())
            for relative, data in originals.items():
                self.assertEqual((source / relative).read_bytes(), data)

            make_alias(source, root / 'complete-alias', '/dspira/')
            self.assertEqual((root / 'complete-alias/assets/history/new-recovery.zip').read_bytes(),
                             originals['assets/history/new-recovery.zip'])

    def test_alias_exclusions_must_stay_inside_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            source.mkdir()
            for excluded in ('.', '..', '../outside', '/absolute'):
                with self.assertRaises(ValueError):
                    make_alias(source, root / 'alias', '/dspira/', exclude=[excluded])
                self.assertFalse((root / 'alias').exists())

    def test_rejects_nested_destinations(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                make_alias(directory, Path(directory) / 'alias', '/dspira/')


if __name__ == '__main__':
    unittest.main()
