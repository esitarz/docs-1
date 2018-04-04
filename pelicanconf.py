#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


AUTHOR = 'OrderCloud.io'
SITENAME = 'OrderCloud Documentation'
SITEURL = 'localhost:8000'
SITETITLE = 'OrderCloud Docs'

SITELOGO = '/images/svg/ordercloudio_horizontal_logo.svg'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME_PATHS = ['pelican-themes']
THEME = 'themes/boots4pelican'

PLUGIN_PATHS = ['pelican-plugins','Plugins']
PLUGINS = ['assets', 'docs-subcategory']

ASSET_SOURCE_PATHS = ['scss',]

DISPLAY_CATEGORIES_ON_MENU = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'
SUBCATEGORY_URL = '{fullurl}.html'
SUBCATEGORY_SAVE_AS = os.path.join('{savepath}.html')

PATH_METADATA= '(?P<subcategory_path>.*)/.*'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_SAVE_AS = os.path.join('{subpath}', '{slug}.html')
ARTICLE_URL = '{suburl}/{slug}.html'

READERS = {'html': None}
IGNORE_FILES = ['**/pelican-plugins/*','**/pelican-themes/*','**/copies/*']

HIDE_DATE = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',

    'markdown.extensions.codehilite': {
        'noclasses' : True,
        'pygments_style':'native',
        'css_class': 'highlight',
        'linenums': True,
        'use_pygments': True
    }
}