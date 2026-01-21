AUTHOR = 'Umanga Bista'
SITENAME = 'Umanga Bista'
SITEURL = "www.bistaumanga.com.np"
SITEDESCRIPTION = 'Personal website and blog of Umanga Bista - AI/ML researcher and engineer'

PATH = "content"

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('Twitter', 'https://www.twitter.com/bistaumanga'),
    ('GitHub', 'https://github.com/bistaumanga'),
    ('LinkedIn', 'https://au.linkedin.com/in/bistaumanga'),
    ('Email', 'mailto:mail@bistaumanga.com.np'),
)

DEFAULT_PAGINATION = 10

# Static paths
STATIC_PATHS = ['images', 'files', 'extra']

# Extra files to copy (like CNAME, robots.txt)
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/dark-mode.css': {'path': 'static/css/dark-mode.css'},
}

# Custom CSS for dark mode
CUSTOM_CSS = 'static/css/dark-mode.css'

# URL settings - Index is the profile page
INDEX_SAVE_AS = 'blog/index.html'  # Blog posts index at /blog/
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'

# Display pages in menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Menu items
MENUITEMS = [
    ('Blog', '/blog/'),
]

LOCALE = ['en_AU']


# Theme and appearance
# THEME = '../themes/blue-penguin'  # Commented out - using default theme

# Blue Penguin theme settings (not used with default theme)
# DISPLAY_HEADER = True
# DISPLAY_FOOTER = True
# DISPLAY_HOME = True
# DISPLAY_MENU = True

# Archives and categories
# ARCHIVES_URL = 'archives'
# ARCHIVES_SAVE_AS = 'archives/index.html'
# CATEGORIES_URL = 'categories'
# CATEGORIES_SAVE_AS = 'categories/index.html'
# THEME = 'themes/custom'  # We'll create this

# Plugins (install with: pip install pelican-plugins)
PLUGIN_PATHS = ['plugins']
PLUGINS = []

# Math rendering (MathJax)
MATH_JAX = {
    'align': 'center',
    'indent': '0em',
    'show_menu': False,
    'process_escapes': True,
    'latex_preview': 'TeX',
    'color': 'inherit',
    'linebreak_automatic': False
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Output path
OUTPUT_PATH = '../output/'
