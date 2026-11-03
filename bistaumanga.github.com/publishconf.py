import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pelicanconf import *

SITEURL = CANONICAL_SITEURL
RELATIVE_URLS = True
FEED_DOMAIN = CANONICAL_SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
DELETE_OUTPUT_DIRECTORY = True
