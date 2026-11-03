from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
AUTHOR = 'Umanga Bista'
SITENAME = 'Umanga Bista'
SITEURL = ''
CANONICAL_SITEURL = 'https://www.bistaumanga.com.np'
SITEDESCRIPTION = 'Umanga Bista — machine learning researcher and applied scientist in Melbourne. NLP, language models, retrieval, and practical AI systems.'
PATH = str(BASE_DIR / 'content')
OUTPUT_PATH = str(BASE_DIR.parent / 'output')
THEME = str(BASE_DIR / 'themes' / 'personal')
TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'
LOCALE = ['C']
SOCIAL = (
    ('Email', 'mailto:bistaumanga@outlook.com'),
    ('GitHub', 'https://github.com/bistaumanga'),
    ('LinkedIn', 'https://au.linkedin.com/in/bistaumanga'),
    ('Google Scholar', 'https://scholar.google.com/citations?user=zfNw5-8AAAAJ&hl=en'),
)
DEFAULT_PAGINATION = 10
STATIC_PATHS = ['files', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PLUGINS = []
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'permalink': False},
    },
    'output_format': 'html5',
}
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap', '404']
SITEMAP_SAVE_AS = 'sitemap.xml'
