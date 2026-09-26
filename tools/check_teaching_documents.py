#!/usr/bin/env python3
"""Check that every catalog entry has matching print and editable downloads."""
import argparse
import json
from pathlib import Path
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    groups = json.loads((root / '_data/teaching_documents.json').read_text())
    seen = set()
    count = 0
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
            count += 1
    print(f'Checked {count} teaching resources with matching PDF and editable files.')


if __name__ == '__main__':
    main()
