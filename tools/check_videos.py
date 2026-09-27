#!/usr/bin/env python3
"""Check embedded lesson videos and their fallback links in a built site."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse


class Videos(HTMLParser):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.links = []
        self.ids = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get('id', '').startswith('video-'):
            self.ids.append(attrs['id'])
        if tag == 'iframe' and 'youtube' in attrs.get('src', ''):
            self.frames.append(attrs)
        if tag == 'a':
            self.links.append(attrs.get('href', ''))


def selection(url):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if parsed.hostname == 'youtu.be':
        return parsed.path.lstrip('/')
    if parsed.path == '/watch':
        return query.get('v', [''])[0]
    if parsed.path in ('/playlist', '/embed/videoseries'):
        return query.get('list', [''])[0]
    return parsed.path.removeprefix('/embed/')


def check(site):
    failures = []
    count = 0
    for path in sorted(site.rglob('*.html')):
        if 'history' in path.relative_to(site).parts:
            continue
        page = Videos()
        page.feed(path.read_text(encoding='utf-8'))
        name = str(path.relative_to(site))
        if len(set(page.ids)) != len(page.ids):
            failures.append(name + ': repeated video anchor')
        seen = set()
        for frame in page.frames:
            count += 1
            src = urlparse(frame['src'])
            query = parse_qs(src.query)
            key = selection(frame['src'])
            if src.scheme != 'https' or src.hostname != 'www.youtube-nocookie.com':
                failures.append(name + ': unexpected player host')
            if not frame.get('title', '').strip() or frame.get('loading') != 'lazy':
                failures.append(name + ': missing player title or lazy loading')
            if frame.get('referrerpolicy') != 'strict-origin-when-cross-origin':
                failures.append(name + ': missing player referrer policy')
            if query.get('autoplay', ['0']) != ['0']:
                failures.append(name + ': video starts automatically')
            if key in seen:
                failures.append(name + ': repeated player for ' + key)
            seen.add(key)
            matches = [url for url in page.links
                       if urlparse(url).hostname in ('youtube.com', 'www.youtube.com', 'youtu.be')
                       and selection(url) == key]
            if not matches:
                failures.append(name + ': no watch link for ' + key)
            for url in matches:
                watch_query = parse_qs(urlparse(url).query)
                start = watch_query.get('t', watch_query.get('start', ['0']))[0].removesuffix('s')
                if start.isdigit() and int(start) and query.get('start') != [start]:
                    failures.append(name + ': start time lost for ' + key)
        for url in page.links:
            if url.startswith('#video-') and url[1:] not in page.ids:
                failures.append(name + ': missing video target ' + url)
    if not count:
        failures.append('No embedded videos found; build the site first.')
    return count, failures


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=Path('_site'))
    args = parser.parse_args()
    count, failures = check(args.site)
    for failure in failures:
        print('::error::' + failure)
    print(f'Checked {count} embedded videos; {len(failures)} problems.')
    raise SystemExit(bool(failures))
