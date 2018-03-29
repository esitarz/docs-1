#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


AUTHOR = 'OrderCloud.io'
SITENAME = 'OrderCloud Documentation Content'
SITEURL = 'localhost:8000'
SITETITLE = 'OrderCloud Docs'

SITELOGO = '/images/svg/ordercloudio_horizontal_logo.svg'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME_PATHS = ['pelican-themes']
#THEME = 'pelican-themes/flex'
# THEME = 'themes/flex-ordercloudio'
THEME = 'themes/pelican-alchemy/alchemy'

PLUGIN_PATHS = ['pelican-plugins','Plugins']
# PLUGINS = ['better_tables', 'ace_editor', 'assets']#ace_editor
PLUGINS = ['better_tables', 'assets']

DISPLAY_CATEGORIES_ON_MENU = True
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_SAVE_AS = os.path.join('{category}','{slug}.html')
ARTICLE_URL = os.path.join('{category}','{slug}.html')

READERS = {'html': None}
IGNORE_FILES = ['**/pelican-plugins/*','**/pelican-themes/*','**/copies/*']



HIDE_DATE = True

ACE_EDITOR_PLUGIN = {
'ACE_EDITOR_THEME' : 'chrome',
'ACE_EDITOR_SHOW_INVISIBLE' : True,
'ACE_EDITOR_READONLY' : False,
'ACE_EDITOR_AUTOSCROLL' : True

}


#CUSTOM_CSS_URL = 'theme/css/style.css'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',

    'markdown.extensions.codehilite': {
        'css_class': 'highlight',
        'linenums': False,
        'use_pygments': False
    }
}

