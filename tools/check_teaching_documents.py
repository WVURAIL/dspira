#!/usr/bin/env python3
"""Check that every catalog entry has matching print and editable downloads."""
import argparse
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


W = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def check_word_style(package, path):
    styles = ET.fromstring(package.read('word/styles.xml'))
    normal = next(s for s in styles.findall('w:style', W)
                  if s.get(f"{{{W['w']}}}styleId") == 'Normal')
    font = normal.find('w:rPr/w:rFonts', W)
    assert font is not None and font.get(f"{{{W['w']}}}ascii") == 'Arial', f'{path}: body font must be Arial'
    for name in package.namelist():
        if not name.startswith('word/') or not name.endswith('.xml'):
            continue
        for font in ET.fromstring(package.read(name)).iter(f"{{{W['w']}}}rFonts"):
            if font.get(f"{{{W['w']}}}ascii") == 'Arial':
                assert not any('theme' in key.lower() for key in font.attrib), f'{path}: theme overrides Arial'


def check_pdf_style(path, word_document):
    import pymupdf

    with pymupdf.open(path) as pdf:
        assert len(pdf), f'{path}: empty PDF'
        for page in pdf:
            header = pymupdf.Rect(0, 0, page.rect.width, page.rect.height * 0.15)
            text = re.sub(r'\s+', ' ', page.get_text(clip=header))
            assert 'WVU DSPIRA' in text, f'{path}, page {page.number + 1}: missing header'
            # Equations and original slide diagrams retain their mathematical typefaces.
            if not word_document:
                continue
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    for span in line['spans']:
                        if any(c.isalpha() for c in span['text']):
                            family = span['font'].lower()
                            assert 'arial' in family or 'math' in family, (
                                f'{path}, page {page.number + 1}: unexpected font {span["font"]}')
        return len(pdf)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    parser.add_argument('--style', action='store_true', help='Check PDF headers and Word export fonts; requires PyMuPDF')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    groups = json.loads((root / '_data/teaching_documents.json').read_text())
    seen = set()
    count = 0
    pages = 0
    for group in groups:
        assert group['title'] and group['documents'], 'Empty teaching group'
        for document in group['documents']:
            assert document['title'], 'Missing resource title'
            pdf = Path(document['pdf'].lstrip('/'))
            editable = Path(document['editable'].lstrip('/'))
            extension, part = {'Word': ('.docx', 'word/document.xml'),
                               'PowerPoint': ('.pptx', 'ppt/presentation.xml')}[document['format']]
            assert pdf.suffix == '.pdf' and editable.suffix == extension, document
            assert pdf.with_suffix('') == editable.with_suffix(''), document
            for path in (pdf, editable):
                assert '..' not in path.parts and path.parts[0] == 'assets', path
                assert path not in seen, f'Duplicate resource: {path}'
                seen.add(path)
                source, published = root / path, args.site / path
                assert source.is_file() and published.is_file(), f'Missing download: {path}'
                assert source.read_bytes() == published.read_bytes(), f'Stale download: {path}'
            assert (root / pdf).read_bytes().startswith(b'%PDF-'), pdf
            with zipfile.ZipFile(root / editable) as package:
                assert part in package.namelist() and package.testzip() is None, editable
                if document['format'] == 'Word':
                    check_word_style(package, editable)
            if args.style:
                pages += check_pdf_style(root / pdf, document['format'] == 'Word')
            count += 1
    for folder in ('assets/lessons', 'assets/worksheets'):
        for path in (root / folder).rglob('*'):
            if path.suffix in ('.pdf', '.docx', '.pptx'):
                assert path.relative_to(root) in seen, f'Missing catalog entry: {path.relative_to(root)}'
    print(f'Checked {count} teaching resources with matching PDF and editable files.')
    if args.style:
        print(f'Checked headers on {pages} PDF pages and consistent Word export fonts.')


if __name__ == '__main__':
    main()
