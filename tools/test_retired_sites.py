import hashlib
from pathlib import Path
import tempfile
import unittest
import zipfile

from retired_sites import extract_verified, historical_html, install_aliases, install_history, NAMES


class PreservationTests(unittest.TestCase):
    def archive(self, root, extra=None):
        package = root / 'sites.zip'
        with zipfile.ZipFile(package, 'w') as archive:
            for name in NAMES:
                archive.writestr(name + '/index.html', '<html><head></head><body>Old material</body></html>')
                archive.writestr(name + '/worksheet.pdf', b'%PDF-original')
            if extra:
                archive.writestr(*extra)
        return package, hashlib.sha256(package.read_bytes()).hexdigest()

    def test_verified_history_and_redirects_keep_download_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, digest = self.archive(root)
            extract_verified(package, root / 'source', digest)
            install_history(root / 'source', root / 'active')
            install_aliases(root / 'source', root / 'lab')
            for name in NAMES:
                historical = root / 'active/history/sites' / name
                alias = root / 'lab' / name
                self.assertIn('Historical material.', (historical / 'index.html').read_text())
                self.assertIn('/dspira/history/sites/' + name + '/', (alias / 'index.html').read_text())
                self.assertIn('window.location.search + window.location.hash', (alias / 'index.html').read_text())
                self.assertNotIn('Old material', (alias / 'index.html').read_text())
                self.assertEqual((alias / 'worksheet.pdf').read_bytes(), b'%PDF-original')
                self.assertEqual((historical / 'worksheet.pdf').read_bytes(), b'%PDF-original')

    def test_rejects_wrong_checksum_and_traversal(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, digest = self.archive(root, ('cra/../../escape', 'bad'))
            with self.assertRaises(ValueError):
                extract_verified(package, root / 'wrong', '0' * 64)
            with self.assertRaises(ValueError):
                extract_verified(package, root / 'unsafe', digest)
            self.assertFalse((root / 'unsafe').exists())

    def test_rewrites_legacy_assets_and_canonical(self):
        original = '<html><head><link rel="canonical" href="old"></head><body><img src="/cra/example.png"><a href="https://wvurail.org/cra/guide/">Guide</a></body></html>'
        result = historical_html(original, 'cra', Path('guide/index.html'))
        self.assertIn('src="/dspira/history/sites/cra/example.png"', result)
        self.assertNotIn('href="old"', result)
        self.assertEqual(result.count('rel="canonical"'), 1)
        self.assertIn('content="noindex"', result)

    def test_adds_context_to_bare_historical_fragments(self):
        result = historical_html('<p>Original text.</p>', 'cra', Path('index.html'))
        self.assertIn('<title>Historical DSPIRA material</title>', result)
        self.assertIn('Historical material.', result)
        self.assertIn('<p>Original text.</p>', result)


if __name__ == '__main__':
    unittest.main()
