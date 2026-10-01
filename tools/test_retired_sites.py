import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from retired_sites import extract_verified, historical_html, install_aliases, install_history, NAMES, PDF_OVERRIDES, remove_unused_export_fonts


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

    def test_removes_only_missing_notebook_overrides_from_published_copies(self):
        original = ('<html><head><style>body { color: black; }</style>'
                    '<link rel="stylesheet" href="custom.css"></head><body>Lesson</body></html>')
        exports = ('gbtdrift/index.html', 'labs/05/I_Q_quadrature_sampling.html')
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, digest = self.archive(root)
            extract_verified(package, root / 'source', digest)
            archive = root / 'source/dspira-archive'
            for relative in (*exports, 'other/index.html'):
                page = archive / relative
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text(original)
            install_history(root / 'source', root / 'active')
            published = root / 'active/history/sites/dspira-archive'
            for relative in exports:
                self.assertNotIn('href="custom.css"', (published / relative).read_text())
                self.assertIn('<style>body { color: black; }</style>', (published / relative).read_text())
                self.assertIn('<body>', (published / relative).read_text())
                self.assertIn('Lesson</body>', (published / relative).read_text())
                self.assertEqual((archive / relative).read_text(), original)
            self.assertIn('href="custom.css"', (published / 'other/index.html').read_text())
            self.assertEqual(hashlib.sha256(package.read_bytes()).hexdigest(), digest)

            (archive / 'gbtdrift/custom.css').write_text('body { color: navy; }')
            install_history(root / 'source', root / 'with-override')
            restored = root / 'with-override/history/sites/dspira-archive/gbtdrift'
            self.assertIn('href="custom.css"', (restored / 'index.html').read_text())
            self.assertEqual((restored / 'custom.css').read_text(), 'body { color: navy; }')

    def test_domain_updates_only_published_copies(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / 'sites.zip'
            old_host = 'old.example.edu'
            original_pdf = b'%PDF-original'
            revised_pdf = root / 'revised.pdf'
            revised_pdf.write_bytes(b'%PDF-updated')
            with zipfile.ZipFile(package, 'w') as archive:
                for name in NAMES:
                    archive.writestr(name + '/index.html',
                        '<html><head><link rel="canonical" href="https://' + old_host
                        + '/' + name + '/"></head><body>https://' + old_host
                        + '/dspira/ https://external.example.edu/</body></html>')
                    archive.writestr(name + '/README.md', 'https://' + old_host + '/dspira/')
                    archive.writestr(name + '/worksheet.pdf', original_pdf)
            digest = hashlib.sha256(package.read_bytes()).hexdigest()
            extract_verified(package, root / 'source', digest)
            overrides = {'cra/worksheet.pdf': (
                hashlib.sha256(original_pdf).hexdigest(), str(revised_pdf))}
            (root / 'active').mkdir()
            pinned_text = root / 'active/pinned-readme.txt'
            pinned_text.write_text('https://' + old_host + '/dspira/')
            lesson_alias = root / 'aliases/dspira-lessons/README.md'
            lesson_alias.parent.mkdir(parents=True)
            lesson_alias.write_text(pinned_text.read_text())
            with patch.dict(PDF_OVERRIDES, overrides, clear=True):
                install_history(root / 'source', root / 'active')
                install_aliases(root / 'source', root / 'aliases')
            for destination in (root / 'active/history/sites', root / 'aliases'):
                self.assertEqual((destination / 'cra/worksheet.pdf').read_bytes(), b'%PDF-updated')
                self.assertEqual((destination / 'cra/README.md').read_text(), 'https://rail.wvu.edu/dspira/')
                self.assertNotIn(old_host, (destination / 'cra/index.html').read_text())
            self.assertEqual(pinned_text.read_text(), 'https://rail.wvu.edu/dspira/')
            self.assertEqual(lesson_alias.read_text(), 'https://rail.wvu.edu/dspira/')
            self.assertIn('https://external.example.edu/',
                          (root / 'active/history/sites/cra/index.html').read_text())
            self.assertEqual((root / 'source/cra/worksheet.pdf').read_bytes(), original_pdf)
            self.assertIn(old_host, (root / 'source/cra/index.html').read_text())
            self.assertEqual(hashlib.sha256(package.read_bytes()).hexdigest(), digest)


    def test_repairs_only_known_historical_anchor_links(self):
        original = ('<html><head></head><body>'
                    '<h2 id="11-installation-guide">Installation</h2>'
                    '<a href="#11-Installation-Guide">Install</a>'
                    "<a href='../02/#14-fun-sdrgnu-radio-things'>SDR</a>"
                    '<a href="#123-a-general-waveform-generator">Waveform</a>'
                    '<a href="#unrelated">Other</a>'
                    '<p>#11-Installation-Guide</p></body></html>')
        result = historical_html(original, 'dspira-archive', Path('labs/01/index.html'))
        self.assertIn('href="#11-installation-guide"', result)
        self.assertIn("href='../02/#24-fun-sdrgnu-radio-things'", result)
        self.assertIn('href="#133-a-general-waveform-generator"', result)
        self.assertIn('href="#unrelated"', result)
        self.assertIn('<p>#11-Installation-Guide</p>', result)
        for name, relative in [('cra', 'labs/01/index.html'), ('dspira-archive', 'other/index.html')]:
            self.assertIn('href="#11-Installation-Guide"', historical_html(original, name, Path(relative)))

        fourier = historical_html('<a href="#57-spectral-leakage--polyphase-filter-bank-pfb">PFB</a>',
                                  'dspira-archive', Path('labs/05/index.html'))
        self.assertIn('href="#56-spectral-leakage--polyphase-filter-bank-pfb"', fourier)

    def test_preserved_homepage_links_reach_current_example_owners(self):
        original = ('<a href="https://github.com/WVURAIL/dspira/tree/master/code/gbt_drift">Drift</a>'
                    '<a href="https://github.com/WVURAIL/dspira/tree/master/code/observations">Observations</a>')
        result = historical_html(original, 'dspira-archive', Path('index.html'))
        self.assertIn('href="https://rail.wvu.edu/dspira/lesson-examples/gbt-drift/"', result)
        self.assertIn('href="https://github.com/WVURAIL/dspira-software/tree/main/data-processing"', result)

    def test_historical_references_use_the_same_article_and_matching_manual_version(self):
        stream_tags = historical_html('<a href="https://gnuradio.org/doc/doxygen/page_stream_tags.html">Tags</a>',
                                      'dspira-archive', Path('labs/01/index.html'))
        self.assertIn('href="https://www.gnuradio.org/doc/doxygen-3.7/page_stream_tags.html"', stream_tags)
        nrsc = historical_html('<a href="http://theori.io/research/nrsc-5-c">NRSC-5</a>',
                               'dspira-archive', Path('labs/02/index.html'))
        self.assertIn('href="https://theori.io/blog/receiving-nrsc-5"', nrsc)
        table = historical_html('<a href="http://www.ws.binghamton.edu/fowler/fowler%20personal%20page/EE301_files/FT%20Tables_rev3.pdf">Table</a>',
                                'dspira-archive', Path('labs/03/index.html'))
        self.assertIn('href="https://ws.binghamton.edu/fowler/fowler%20personal%20page/EE301_files/FT%20Tables_rev3.pdf"', table)

    def test_preserves_available_or_used_export_fonts(self):
        definition = "@font-face {font-family: 'FontAwesome'; src: url('../fonts/icons.woff?v=4.2.0');}"
        other = "@font-face {font-family: 'Lesson text'; src: url('../fonts/text.woff');}"
        original = '<html><head><style>' + definition + other + '</style></head><body>Notebook</body></html>'
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            page = root / 'notebook/index.html'
            page.parent.mkdir()
            result = remove_unused_export_fonts(original, page)
            self.assertNotIn(definition, result)
            self.assertIn(other, result)
            for markup in ['<i class="fa fa-save"></i>', '<i class="fa-save"></i>',
                           '<span style="font-family: FontAwesome">Icon</span>']:
                used = original.replace('Notebook', markup)
                self.assertIn(definition, remove_unused_export_fonts(used, page))
            (root / 'fonts').mkdir()
            (root / 'fonts/icons.woff').write_bytes(b'available-font')
            self.assertEqual(remove_unused_export_fonts(original, page), original)

    def test_historical_repairs_preserve_source_package_and_downloads(self):
        notebook = ('<html><head><style>@font-face {font-family: "Glyphicons Halflings"; '
                    'src: url("../components/bootstrap/fonts/missing.woff");}'
                    'body {color: black;}</style></head><body>Original output</body></html>')
        lesson = '<html><head></head><body><a href="#11-Installation-Guide">Install</a></body></html>'
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, _ = self.archive(root)
            with zipfile.ZipFile(package, 'a') as archive:
                archive.writestr('dspira-archive/labs/01/index.html', lesson)
                archive.writestr('dspira-archive/labs/05/I_Q_quadrature_sampling.html', notebook)
                archive.writestr('dspira-archive/other.html', notebook)
                archive.writestr('dspira-archive/labs/05/original.ipynb', b'original notebook bytes')
            digest = hashlib.sha256(package.read_bytes()).hexdigest()
            extract_verified(package, root / 'source', digest)
            before = {str(p.relative_to(root / 'source')): p.read_bytes()
                      for p in (root / 'source').rglob('*') if p.is_file()}
            install_history(root / 'source', root / 'active')
            published = root / 'active/history/sites/dspira-archive'
            self.assertIn('href="#11-installation-guide"', (published / 'labs/01/index.html').read_text())
            result = (published / 'labs/05/I_Q_quadrature_sampling.html').read_text()
            self.assertNotIn('@font-face', result)
            self.assertIn('body {color: black;}', result)
            self.assertIn('Original output', result)
            self.assertIn('@font-face', (published / 'other.html').read_text())
            self.assertEqual((published / 'labs/05/original.ipynb').read_bytes(), b'original notebook bytes')
            after = {str(p.relative_to(root / 'source')): p.read_bytes()
                     for p in (root / 'source').rglob('*') if p.is_file()}
            self.assertEqual(before, after)
            self.assertEqual(hashlib.sha256(package.read_bytes()).hexdigest(), digest)

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
        original = '<html><head><link rel="canonical" href="old"></head><body><img src="/cra/example.png"><a href="https://rail.wvu.edu/cra/guide/">Guide</a></body></html>'
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
