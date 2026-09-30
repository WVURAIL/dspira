#!/usr/bin/env python3
import hashlib
from pathlib import Path
import tempfile
import unittest

from publish_assets import publish
from version_downloads import version_downloads


class AssetPublishingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.site = Path(self.temporary.name)
        (self.site / 'assets/lesson').mkdir(parents=True)
        (self.site / 'assets/lesson/worksheet.pdf').write_bytes(b'%PDF original\x00bytes')
        self.local = {'legacy': 'FilesUploaded/Old Worksheet.pdf',
                      'source': 'assets/lesson/worksheet.pdf'}

    def test_binary_download_survives_a_move_and_repeated_publication(self):
        for _ in range(2):
            self.assertEqual(publish(self.site, {'files': [self.local]}), 1)
        self.assertEqual((self.site / self.local['legacy']).read_bytes(), b'%PDF original\x00bytes')

    def test_local_alias_follows_an_updated_worksheet(self):
        (self.site / self.local['source']).write_bytes(b'new worksheet')
        publish(self.site, {'files': [self.local]})
        self.assertEqual((self.site / self.local['legacy']).read_bytes(), b'new worksheet')

    def test_existing_content_is_not_overwritten(self):
        (self.site / 'FilesUploaded').mkdir()
        (self.site / self.local['legacy']).write_bytes(b'another document')
        with self.assertRaisesRegex(ValueError, 'would be replaced'):
            publish(self.site, {'files': [self.local]})
        self.assertEqual((self.site / self.local['legacy']).read_bytes(), b'another document')

    def test_missing_source_fails_the_build(self):
        with self.assertRaisesRegex(ValueError, 'Missing published asset'):
            publish(self.site, {'files': [dict(self.local, source='assets/missing.pdf')]})

    def test_paths_cannot_escape_the_site(self):
        for key in ('legacy', 'source'):
            for bad in ('../outside.pdf', '/outside.pdf', r'..\outside.pdf'):
                with self.subTest(key=key, path=bad), self.assertRaises(ValueError):
                    publish(self.site, {'files': [dict(self.local, **{key: bad})]})

    def test_repeated_addresses_fail_before_writing(self):
        with self.assertRaisesRegex(ValueError, 'Repeated legacy address'):
            publish(self.site, {'files': [self.local, self.local]})
        self.assertFalse((self.site / 'FilesUploaded').exists())

    def test_remote_download_requires_the_pinned_bytes(self):
        data = b'original flowgraph'
        entry = {'legacy': 'FilesUploaded/old.grc',
                 'url': 'https://raw.githubusercontent.com/WVURAIL/dspira/' + 'a' * 40 + '/old.grc',
                 'sha256': hashlib.sha256(data).hexdigest()}
        publish(self.site, {'files': [entry]}, fetch=lambda url: data)
        self.assertEqual((self.site / entry['legacy']).read_bytes(), data)
        with self.assertRaisesRegex(ValueError, 'checksum mismatch'):
            publish(self.site, {'files': [entry]}, fetch=lambda url: b'changed')
        with self.assertRaisesRegex(ValueError, 'pinned GitHub revision'):
            publish(self.site, {'files': [dict(entry, url=entry['url'].replace('a' * 40, 'main'))]})


class DownloadVersionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.site = Path(self.temporary.name)
        (self.site / 'assets').mkdir()
        self.pdf = self.site / 'assets/Lesson sheet.pdf'
        self.pdf.write_bytes(b'%PDF current lesson')
        self.index = self.site / 'index.html'
        self.index.write_text('<link rel="canonical" href="https://rail.wvu.edu/dspira/">')
        (self.site / 'lesson').mkdir()
        self.page = self.site / 'lesson/index.html'
        self.head = '<link href="https://rail.wvu.edu/dspira/lesson/" rel="canonical">'

    def test_changed_files_get_new_versions_without_losing_queries_or_fragments(self):
        self.page.write_text(self.head + '<a href="../assets/Lesson%20sheet.pdf?download=1&amp;v=old#page=2">PDF</a>')
        self.assertEqual(version_downloads(self.site), 1)
        first = hashlib.sha256(self.pdf.read_bytes()).hexdigest()[:12]
        self.assertIn('?download=1&amp;v=' + first + '#page=2', self.page.read_text())
        self.assertEqual(version_downloads(self.site), 0)
        self.pdf.write_bytes(b'%PDF revised lesson')
        self.assertEqual(version_downloads(self.site), 1)
        self.assertNotIn(first, self.page.read_text())

    def test_external_sibling_missing_and_non_document_links_stay_unchanged(self):
        body = ''.join('<a href="' + url + '">link</a>' for url in (
            'https://example.org/dspira/assets/Lesson%20sheet.pdf',
            '/lightwork/paper.pdf', '/dspira/assets/missing.pdf',
            '/dspira/assets/picture.png', 'mailto:rail@wvu.edu', '#page=2'))
        self.page.write_text(self.head + body)
        self.assertEqual(version_downloads(self.site), 0)
        self.assertEqual(self.page.read_text(), self.head + body)

    def test_root_absolute_and_embedded_downloads_use_same_file_version(self):
        self.page.write_text(self.head +
            '<a href="/dspira/assets/Lesson%20sheet.pdf">PDF</a>' +
            "<iframe src='https://rail.wvu.edu/dspira/assets/Lesson%20sheet.pdf#page=3'></iframe>")
        self.assertEqual(version_downloads(self.site), 2)
        digest = hashlib.sha256(self.pdf.read_bytes()).hexdigest()[:12]
        self.assertEqual(self.page.read_text().count('v=' + digest), 2)
        self.assertIn('#page=3', self.page.read_text())

    def test_only_the_actual_link_attribute_changes(self):
        self.page.write_text(self.head +
            '<a data-href="keep.pdf" title="href=keep.pdf" href=/dspira/assets/Lesson%20sheet.pdf>PDF</a>')
        self.assertEqual(version_downloads(self.site), 1)
        digest = hashlib.sha256(self.pdf.read_bytes()).hexdigest()[:12]
        self.assertIn('data-href="keep.pdf" title="href=keep.pdf"', self.page.read_text())
        self.assertIn('href="/dspira/assets/Lesson%20sheet.pdf?v=' + digest + '">', self.page.read_text())

    def test_encoded_traversal_cannot_read_files_outside_the_published_site(self):
        self.page.write_text(self.head + '<a href="/dspira/%2e%2e/outside.pdf">PDF</a>')
        self.assertEqual(version_downloads(self.site), 0)


if __name__ == '__main__':
    unittest.main()
