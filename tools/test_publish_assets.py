#!/usr/bin/env python3
import hashlib
from pathlib import Path
import tempfile
import unittest

from publish_assets import publish


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


if __name__ == '__main__':
    unittest.main()
