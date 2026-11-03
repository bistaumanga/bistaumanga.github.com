"""Check generated pages for broken local links and essential metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.h1s = 0
        self.canonicals = []
        self.description = False
        self.lang = False
        self.stylesheet = False
        self.images_without_alt = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.lang = bool(attrs.get('lang'))
        if tag == 'h1':
            self.h1s += 1
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = bool(attrs.get('content', '').strip())
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href', ''))
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.stylesheet = True
        if tag == 'img' and not attrs.get('alt'):
            self.images_without_alt += 1
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def check(root):
    root = root.resolve()
    errors = []
    pages = {}
    for file in root.rglob('*.html'):
        page = Page()
        page.feed(file.read_text())
        pages[file] = page
        if page.h1s != 1 or not page.description or not page.lang or not page.stylesheet:
            errors.append(f'{file.relative_to(root)}: missing metadata, stylesheet, language, or single h1')
        if len(page.canonicals) != 1 or not page.canonicals[0].startswith('https://www.bistaumanga.com.np/'):
            errors.append(f'{file.relative_to(root)}: invalid canonical URL')
        if page.images_without_alt:
            errors.append(f'{file.relative_to(root)}: image missing alt text')
    for file, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (root / unquote(url.path.lstrip('/')) if url.path.startswith('/')
                      else file.parent / unquote(url.path)) if url.path else file
            target = target.resolve()
            if target.is_dir():
                target /= 'index.html'
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'{file.relative_to(root)}: broken link {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{file.relative_to(root)}: missing fragment {link}')
    for required in ('index.html', 'blog/index.html', '001_visual_search.html', '404.html',
                     'CNAME', 'robots.txt', 'sitemap.xml'):
        if not (root / required).is_file():
            errors.append(f'Missing {required}')
    if (root / 'sitemap.xml').is_file():
        sitemap = ET.parse(root / 'sitemap.xml')
        for loc in sitemap.findall('.//{*}loc'):
            path = urlsplit(loc.text).path
            target = root / path.lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'Sitemap has missing page: {loc.text}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} HTML pages: local links, fragments, metadata, images, sitemap, and required files pass.')


if __name__ == '__main__':
    check(Path(sys.argv[1] if len(sys.argv) > 1 else 'output'))
