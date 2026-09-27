from pathlib import Path
import hashlib
from html import escape
from html.parser import HTMLParser
import re
from urllib.parse import parse_qsl, unquote, urlencode, urljoin, urlsplit, urlunsplit

FORMATS = {'.pdf', '.docx', '.pptx', '.dotx', '.potx', '.ipynb', '.csv'}
ATTRIBUTE = re.compile(r'''([^\s=<>/]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))''', re.S)


class CanonicalURL(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.url = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and 'canonical' in attrs.get('rel', '').split():
            self.url = attrs.get('href')


def version_downloads(site):
    """Refresh document links when the published file bytes change."""
    site = Path(site).resolve()
    index = site / 'index.html'
    if not index.is_file():
        return 0
    root_url = CanonicalURL(index.read_text(encoding='utf-8')).url
    if not root_url:
        return 0
    root = urlsplit(root_url)
    base = root.path.rstrip('/') + '/'
    digests = {}
    count = 0

    class DocumentLinks(HTMLParser):
        def __init__(self, source, page_url):
            super().__init__()
            self.page_url = page_url
            self.offsets = [0]
            for line in source.splitlines(keepends=True):
                self.offsets.append(self.offsets[-1] + len(line))
            self.edits = []
            self.feed(source)

        def handle_starttag(self, tag, attrs):
            attribute = {'a': 'href', 'iframe': 'src', 'embed': 'src', 'object': 'data'}.get(tag)
            if not attribute:
                return
            original = dict(attrs).get(attribute)
            if not original:
                return
            resolved = urlsplit(urljoin(self.page_url, original))
            if resolved.scheme not in {'http', 'https'} or resolved.netloc != root.netloc:
                return
            if not resolved.path.startswith(base):
                return
            relative = unquote(resolved.path[len(base):])
            target = (site / relative).resolve()
            if site not in target.parents or target.suffix.lower() not in FORMATS or not target.is_file():
                return
            if target not in digests:
                digests[target] = hashlib.sha256(target.read_bytes()).hexdigest()[:12]
            parts = urlsplit(original)
            query = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if key != 'v']
            query.append(('v', digests[target]))
            updated = urlunsplit(parts._replace(query=urlencode(query)))
            if updated == original:
                return
            raw = self.get_starttag_text()
            for match in ATTRIBUTE.finditer(raw):
                if match.group(1).lower() == attribute:
                    line, col = self.getpos()
                    start = self.offsets[line - 1] + col
                    group = next(i for i in (2, 3, 4) if match.group(i) is not None)
                    value = escape(updated, quote=True)
                    if group == 4:
                        value = '"' + value + '"'
                    self.edits.append((start + match.start(group), start + match.end(group), value))
                    break

    for path in site.rglob('*.html'):
        source = path.read_text(encoding='utf-8')
        page_url = CanonicalURL(source).url
        if not page_url:
            continue
        parser = DocumentLinks(source, page_url)
        for start, end, updated in reversed(parser.edits):
            source = source[:start] + updated + source[end:]
        if parser.edits:
            path.write_text(source, encoding='utf-8')
            count += len(parser.edits)
    return count
