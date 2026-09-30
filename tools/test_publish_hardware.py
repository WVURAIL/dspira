from io import BytesIO
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from urllib.error import HTTPError
from zipfile import ZipFile

from check_links import published_hardware_exists
from publish_hardware import document_names, needs_update, publish_hardware
from version_downloads import version_downloads


class HardwarePublicationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.site = Path(temporary.name) / 'site'
        self.site.mkdir()
        self.pdf = b'%PDF-1.7\noriginal hardware guide'
        stream = BytesIO()
        with ZipFile(stream, 'w') as package:
            package.writestr('word/document.xml', '<document/>')
        self.word = stream.getvalue()
        self.manifest = {'files': ['assembly/guide.pdf', 'assembly/guide.docx']}
        self.revision = 'a' * 40

    def fetch(self, url):
        if url.endswith('/commits/main'):
            return json.dumps({'sha': self.revision}).encode()
        self.assertIn('/' + self.revision + '/', url)
        return self.pdf if url.endswith('.pdf') else self.word

    def test_original_bytes_and_revision_are_published(self):
        record = publish_hardware(self.site, self.manifest, fetch=self.fetch)
        root = self.site / 'assets/hardware'
        self.assertEqual((root / 'assembly/guide.pdf').read_bytes(), self.pdf)
        self.assertEqual((root / 'assembly/guide.docx').read_bytes(), self.word)
        self.assertEqual(json.loads((root / 'source.json').read_text()), record)
        self.assertEqual(record['revision'], self.revision)
        self.assertEqual(record['files']['assembly/guide.pdf'], hashlib.sha256(self.pdf).hexdigest())

    def test_new_revision_refreshes_documents_and_browser_versions(self):
        page = self.site / 'index.html'
        page.write_text('<link rel="canonical" href="https://rail.wvu.edu/dspira/">'
                        '<a href="/dspira/assets/hardware/assembly/guide.pdf#page=2">View PDF</a>')
        publish_hardware(self.site, self.manifest, fetch=self.fetch)
        version_downloads(self.site)
        old_hash = hashlib.sha256(self.pdf).hexdigest()[:12]
        self.assertIn('v=' + old_hash, page.read_text())
        self.revision = 'b' * 40
        self.pdf = b'%PDF-1.7\nrevised hardware guide'
        record = publish_hardware(self.site, self.manifest, fetch=self.fetch)
        version_downloads(self.site)
        self.assertEqual(record['revision'], self.revision)
        self.assertNotIn(old_hash, page.read_text())
        self.assertIn('#page=2', page.read_text())

    def test_failed_or_invalid_downloads_leave_published_documents_unchanged(self):
        publish_hardware(self.site, self.manifest, fetch=self.fetch)
        before = {p: p.read_bytes() for p in self.site.rglob('*') if p.is_file()}
        for invalid in (b'<html>error</html>', b'version https://git-lfs.github.com/spec/v1'):
            def fetch(url):
                return invalid if url.endswith('.pdf') else self.word
            with self.assertRaisesRegex(ValueError, 'Invalid hardware PDF'):
                publish_hardware(self.site, self.manifest, self.revision, fetch)
        with self.assertRaisesRegex(ValueError, 'Invalid hardware Word'):
            publish_hardware(self.site, self.manifest, self.revision, lambda url: self.pdf)
        def missing(url):
            raise HTTPError(url, 404, 'Missing', {}, None)
        with self.assertRaises(HTTPError):
            publish_hardware(self.site, self.manifest, self.revision, missing)
        self.assertEqual({p: p.read_bytes() for p in self.site.rglob('*') if p.is_file()}, before)

    def test_paths_and_revisions_are_validated(self):
        for name in ('../escape.pdf', '/escape.pdf', r'..\escape.pdf', 'a//b.pdf', 'a/../b.pdf', 'guide.exe'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                document_names({'files': [name]})
        for names in ([], ['a.pdf', 'a.pdf']):
            with self.assertRaises(ValueError): document_names({'files': names})
        for revision in ('main', 'abc123', '../main'):
            with self.assertRaises(ValueError):
                publish_hardware(self.site, self.manifest, revision, self.fetch)

    def test_symlinks_cannot_write_outside_the_build(self):
        outside = self.site.parent / 'outside'
        outside.mkdir()
        (self.site / 'assets').mkdir()
        (self.site / 'assets/hardware').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'leaves the built site'):
            publish_hardware(self.site, self.manifest, self.revision, self.fetch)
        self.assertEqual(list(outside.iterdir()), [])

    def test_schedule_skips_unchanged_sources_and_detects_new_documents(self):
        record = publish_hardware(self.site, self.manifest, fetch=self.fetch)
        fetch = lambda url: json.dumps(record).encode()
        url = 'https://rail.wvu.edu/dspira/assets/hardware/source.json'
        self.assertFalse(needs_update(self.manifest, self.revision, url, fetch))
        self.assertTrue(needs_update(self.manifest, 'b' * 40, url, fetch))
        self.assertTrue(needs_update({'files': ['new-guide.pdf']}, self.revision, url, fetch))

    def test_first_publication_is_detected_but_server_errors_remain_errors(self):
        url = 'https://rail.wvu.edu/dspira/assets/hardware/source.json'
        def missing(url): raise HTTPError(url, 404, 'Missing', {}, None)
        self.assertTrue(needs_update(self.manifest, self.revision, url, missing))
        def unavailable(url): raise HTTPError(url, 503, 'Unavailable', {}, None)
        with self.assertRaises(HTTPError): needs_update(self.manifest, self.revision, url, unavailable)

    def test_all_files_use_one_resolved_commit(self):
        calls = []
        def fetch(url):
            calls.append(url)
            return self.fetch(url)
        publish_hardware(self.site, self.manifest, fetch=fetch)
        self.assertEqual(sum(url.endswith('/commits/main') for url in calls), 1)
        self.assertEqual(sum('/' + self.revision + '/' in url for url in calls), 2)

    def test_catalog_downloads_are_in_the_publication_manifest(self):
        data = Path(__file__).resolve().parents[1] / '_data'
        names = document_names(json.loads((data / 'hardware_publication.json').read_text()))
        for document in json.loads((data / 'hardware_documents.json').read_text()):
            for extension in ('.pdf', '.docx'):
                self.assertIn(document['path'] + extension, names)

    def test_link_checker_requires_the_actual_generated_file(self):
        path = 'assets/hardware/assembly/guide.pdf'
        self.assertFalse(published_hardware_exists(path, self.site))
        publish_hardware(self.site, self.manifest, fetch=self.fetch)
        self.assertTrue(published_hardware_exists(path, self.site))
        self.assertFalse(published_hardware_exists('assets/hardware/missing.pdf', self.site))
        self.assertFalse(published_hardware_exists('assets/hardware/../../outside.pdf', self.site))


if __name__ == '__main__':
    unittest.main()
