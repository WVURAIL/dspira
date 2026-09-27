#!/usr/bin/env python3
"""Check that webpage exports retain assembly text, dimensions, and artwork."""

from html import unescape
from pathlib import Path
import os
import re
import tempfile
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import check_links
from export_assembly_guides import GUIDES, NS, ROOT, WEB_TEXT, export_guide, text_of


class AssemblyGuides(unittest.TestCase):
    def test_all_instruction_text_and_original_images_survive(self):
        for name, images in GUIDES.items():
            with self.subTest(guide=name):
                result = export_guide(ROOT, name, images)
                markup = result[Path("_includes/assembly") / (name + ".html")].decode()
                visible = unescape(re.sub(r"<[^>]+>", "", markup))
                with ZipFile(ROOT / "assets/lessons/horn-construction" / (name + ".docx")) as package:
                    doc = ET.fromstring(package.read("word/document.xml"))
                    for p in doc.findall(".//w:body//w:p", NS):
                        style = p.find("w:pPr/w:pStyle", NS)
                        if style is not None and style.attrib.get(f"{{{NS['w']}}}val") in ("Title", "Subtitle"):
                            continue
                        expected = re.sub(r"^\d+\.\s+", "", text_of(p))
                        for old, new in WEB_TEXT.items():
                            expected = expected.replace(old, new)
                        self.assertIn(expected, visible)
                    original_images = [package.read(p) for p in package.namelist() if p.startswith("word/media/")]
                    exported_images = [data for path, data in result.items() if path.parts[0] == "images"]
                    self.assertEqual(len(exported_images), len(images))
                    for data in exported_images:
                        self.assertIn(data, original_images)
                self.assertNotIn('alt=""', markup)
                self.assertEqual(len(re.findall(r'width="\d+" height="\d+"', markup)), len(images))
                ids = re.findall(r'id="([^"]+)"', markup)
                self.assertEqual(len(ids), len(set(ids)))
                self.assertIn('<th scope="col">', markup)

    def test_checked_in_exports_are_current(self):
        for name, images in GUIDES.items():
            for path, data in export_guide(ROOT, name, images).items():
                # Git may check out HTML with CRLF on Windows.
                actual = (ROOT / path).read_bytes()
                if path.suffix == ".html":
                    actual = actual.replace(b"\r\n", b"\n")
                self.assertEqual(actual, data, str(path))

    def test_static_include_anchors_are_scoped_and_cycles_stop(self):
        previous = Path.cwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                Path("_includes/assembly").mkdir(parents=True)
                Path("_includes/assembly/one.html").write_text('<h2 id="dimensions">Dimensions</h2>\n{% include assembly/two.html %}')
                Path("_includes/assembly/two.html").write_text('<h3 id="cuts">Cuts</h3>\n{% include assembly/one.html %}')
                Path("used.md").write_text("# Start\n{% include assembly/one.html %}")
                Path("other.md").write_text("# Other")
                self.assertEqual(check_links.anchors_in("used.md"), {"start", "dimensions", "cuts"})
                self.assertEqual(check_links.anchors_in("other.md"), {"other"})
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
