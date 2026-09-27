#!/usr/bin/env python3
"""Check that every catalog entry has matching print and editable downloads."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile


W = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}


def check_template(package, path, part, word_document):
    content_types = ET.fromstring(package.read('[Content_Types].xml'))
    expected = ('application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml'
                if word_document else 'application/vnd.openxmlformats-officedocument.presentationml.template.main+xml')
    assert any(node.get('PartName') == '/' + part and node.get('ContentType') == expected
               for node in content_types), f'{path}: not an Office template'
    assert not any('vbaproject' in name.lower() for name in package.namelist()), f'{path}: unexpected macro'
    if word_document:
        footers = [package.read(name).decode('utf-8') for name in package.namelist()
                   if re.fullmatch(r'word/footer\d+\.xml', name)]
        assert any('PAGE' in footer and 'NUMPAGES' in footer for footer in footers), f'{path}: missing page fields'
    else:
        p = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
             'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
        layouts = [ET.fromstring(package.read(name)) for name in package.namelist()
                   if re.fullmatch(r'ppt/slideLayouts/slideLayout\d+\.xml', name)]
        assert layouts, f'{path}: no reusable layouts'
        for layout in layouts:
            placeholders = layout.findall('.//p:ph', p)
            assert len(placeholders) >= 2 and any(ph.get('type') == 'title' for ph in placeholders), (
                f'{path}: layout lacks editable title and content placeholders')
        masters = [ET.fromstring(package.read(name)) for name in package.namelist()
                   if re.fullmatch(r'ppt/slideMasters/slideMaster\d+\.xml', name)]
        assert len(masters) == 1, f'{path}: unexpected extra slide master'
        assert 'WVU DSPIRA' in ''.join(masters[0].itertext()), f'{path}: master lacks branding'
        assert masters[0].find('.//a:fld[@type="slidenum"]', p) is not None, f'{path}: missing slide number field'


def check_word_style(package, path):
    styles = ET.fromstring(package.read('word/styles.xml'))
    by_id = {style.get(f"{{{W['w']}}}styleId"): style for style in styles.findall('w:style', W)}

    def inherited(style_id, element, attribute):
        visited = set()
        while style_id and style_id not in visited:
            visited.add(style_id)
            style = by_id.get(style_id)
            assert style is not None, f'{path}: unknown style {style_id}'
            node = style.find(f'w:rPr/w:{element}', W)
            if node is not None and node.get(f"{{{W['w']}}}{attribute}") is not None:
                return node.get(f"{{{W['w']}}}{attribute}")
            parent = style.find('w:basedOn', W)
            style_id = parent.get(f"{{{W['w']}}}val") if parent is not None else None
        node = styles.find(f'w:docDefaults/w:rPrDefault/w:rPr/w:{element}', W)
        return node.get(f"{{{W['w']}}}{attribute}") if node is not None else None

    assert inherited('Normal', 'rFonts', 'ascii') == 'Arial', f'{path}: body font must be Arial'
    for style_id, size in (('Normal', 22), ('Title', 48), ('Heading1', 30), ('Heading2', 24)):
        assert inherited(style_id, 'sz', 'val') == str(size), (
            f'{path}: {style_id} must use the lesson template size')
    for name in package.namelist():
        if not name.startswith('word/') or not name.endswith('.xml'):
            continue
        for font in ET.fromstring(package.read(name)).iter(f"{{{W['w']}}}rFonts"):
            if font.get(f"{{{W['w']}}}ascii") == 'Arial':
                assert not any('theme' in key.lower() for key in font.attrib), f'{path}: theme overrides Arial'


def check_slide_style(package, path):
    ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
          'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
    presentation = ET.fromstring(package.read('ppt/presentation.xml'))
    size = presentation.find('p:sldSz', ns)
    assert size is not None and (size.get('cx'), size.get('cy')) == ('12192000', '6858000'), (
        f'{path}: slides must use the widescreen teaching template')
    masters = [ET.fromstring(package.read(name)) for name in package.namelist()
               if re.fullmatch(r'ppt/slideMasters/slideMaster\d+\.xml', name)]
    assert len(masters) == 1, f'{path}: unexpected extra slide master'
    assert 'WVU DSPIRA' in ''.join(masters[0].itertext()), f'{path}: missing branded master'
    assert masters[0].find('.//a:fld[@type="slidenum"]', ns) is not None, f'{path}: missing slide number'
    layouts = {ET.fromstring(package.read(name)).find('p:cSld', ns).get('name')
               for name in package.namelist()
               if re.fullmatch(r'ppt/slideLayouts/slideLayout\d+\.xml', name)}
    expected = {'Lesson title', 'Question and goals', 'Explanation and figure',
                'Activity steps', 'Data or visual', 'Discussion and reflection'}
    assert expected <= layouts, f'{path}: missing reusable teacher layouts'


def check_pdf_style(path, word_document):
    import pymupdf

    with pymupdf.open(path) as pdf:
        assert len(pdf), f'{path}: empty PDF'
        for page in pdf:
            header = pymupdf.Rect(0, 0, page.rect.width, min(80, page.rect.height * 0.15))
            text = re.sub(r'\s+', ' ', page.get_text(clip=header))
            assert 'WVU DSPIRA' in text, f'{path}, page {page.number + 1}: missing header'
            spans = [span for block in page.get_text('dict', clip=header)['blocks']
                     for line in block.get('lines', []) for span in line['spans']]
            brand = [span for span in spans if ' '.join(span['text'].split()) == 'WVU DSPIRA']
            assert len(brand) == 1 and brand[0]['size'] >= 15.5 and brand[0]['color'] == 0xffffff, (
                f'{path}, page {page.number + 1}: header must use prominent white lettering')
            assert 'WEST VIRGINIA UNIVERSITY' in text, f'{path}, page {page.number + 1}: missing university name'
            shapes = [shape for shape in page.get_drawings()
                      if shape.get('fill') and shape['rect'].y1 <= header.y1]

            def matches_color(shape, color):
                return all(abs(actual - expected / 255) < .01
                           for actual, expected in zip(shape['fill'], color))

            assert any(matches_color(shape, (0, 40, 85))
                       and shape['rect'].width >= page.rect.width * .75
                       and shape['rect'].contains(pymupdf.Rect(brand[0]['bbox'])) for shape in shapes), (
                f'{path}, page {page.number + 1}: missing navy header band')
            assert any(matches_color(shape, (238, 170, 0))
                       and shape['rect'].width >= page.rect.width * .75 for shape in shapes), (
                f'{path}, page {page.number + 1}: missing gold header rule')
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


def check_restored_figures(package, path, expected):
    """Keep recovered diagram labels intact when Office rewrites image parts."""
    import pymupdf

    found = set()
    for name in package.namelist():
        if not name.startswith(('word/media/', 'ppt/media/')):
            continue
        try:
            image = pymupdf.Pixmap(package.read(name))
        except (RuntimeError, ValueError):
            continue
        if image.alpha:
            found.add((image.width, image.height, hashlib.sha256(image.samples).hexdigest()))
    for figure in expected:
        key = (figure['width'], figure['height'], figure['sha256'])
        assert key in found, (
            f'{path}: restored figure changed or lost transparency '
            f'({figure["width"]} x {figure["height"]}); compare with the original before updating its reference')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    parser.add_argument('--style', action='store_true', help='Check PDF headers and Word export fonts; requires PyMuPDF')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    figure_checks = {item['editable']: item['figures'] for item in
                     json.loads((root / 'tools/teaching_figure_checks.json').read_text())}
    groups = json.loads((root / '_data/teaching_documents.json').read_text())
    templates = json.loads((root / '_data/teaching_templates.json').read_text())
    groups.append({'title': 'Teacher templates', 'documents': templates})
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
                               'PowerPoint': ('.pptx', 'ppt/presentation.xml'),
                               'Word template': ('.dotx', 'word/document.xml'),
                               'PowerPoint template': ('.potx', 'ppt/presentation.xml')}[document['format']]
            word_document = document['format'].startswith('Word')
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
                if word_document:
                    check_word_style(package, editable)
                else:
                    check_slide_style(package, editable)
                if extension in ('.dotx', '.potx'):
                    check_template(package, editable, part, word_document)
                if args.style and editable.as_posix() in figure_checks:
                    check_restored_figures(package, editable, figure_checks[editable.as_posix()])
            if args.style:
                pages += check_pdf_style(root / pdf, word_document)
            count += 1
    for folder in ('assets/lessons', 'assets/worksheets', 'assets/templates'):
        for path in (root / folder).rglob('*'):
            if path.suffix in ('.pdf', '.docx', '.pptx', '.dotx', '.potx'):
                assert path.relative_to(root) in seen, f'Missing catalog entry: {path.relative_to(root)}'
    print(f'Checked {count} teaching resources with matching PDF and editable files.')
    if args.style:
        print(f'Checked headers on {pages} PDF pages and consistent Word export fonts.')


if __name__ == '__main__':
    main()
