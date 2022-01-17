#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Shubhanshu Mishra'
SITENAME = u'Interpreting Models'
SITEURL = 'http://localhost:8000'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.meta': {},
        "pymdownx.magiclink": {},
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    "output_format": "html5"
}        

GITHUB_URL='https://github.com/napsternxg/blog'
PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Personal Website', 'https://shubhanshu.com/'),
        )

# Social widget
SOCIAL = (('website', 'https://shubhanshu.com'),
    ('twitter', 'https://twitter.com/TheShubhanshu'),
    ('linkedin', 'https://www.linkedin.com/in/shubhanshumishra'),
    ('github', 'https://github.com/napsternxg'),
    ('rss', '//shubhanshu.com/blog/feeds/all.atom.xml')
    )

DEFAULT_PAGINATION = 10
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup, 'extract_toc']
IGNORE_FILES = ['.ipynb_checkpoints']
JINJA_ENVIRONMENT = {
        'trim_blocks': True,
        'lstrip_blocks': True,
        'extensions': [],
}
IPYNB_SKIP_CSS=True
IPYNB_IGNORE_CSS = True
#IPYNB_COLORSCHEME='monokai'

## PATHS
OUTPUT_PATH="docs"
# put articles (posts) in blog/
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'index.html'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives/'
AUTHOR_SAVE_AS = '{slug}.html'
AUTHORS_SAVE_AS = 'authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


DISQUS_SITENAME = "shubhanshu-blog"
GOOGLE_ANALYTICS='UA-44393164-1'
TWITTER_USERNAME='TheShubhanshu'
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

# THEME SETTINGS
#THEME='../pelican-themes/pelican-bootstrap3'
#THEME='../pelican-themes/Flex'
THEME='../pelican-themes/pelican-bootswatch'
BOOTSWATCH_CDN="https://cdnjs.cloudflare.com/ajax/libs/bootswatch"
BOOTSWATCH_THEME="litera"
BOOTSWATCH_VERSION="5.1.1"
#BOOTSWATCH_INTEGRITY_SHA384="sha512-lClzayU/EqX2Du6vlZ1CDtYxqI311AxmlqlUH6oqJvSb8bcZ+04JsCnZWzh9lEOUsER0vzz2r69nRBnT1+ZJ2w=="
BOOTSWATCH_INTEGRITY_SHA384="sha512-Ze0T5yoPnXhcETAFZDb7QSgCVQa1QDkA1c+wrFiRdSqcVXOnyutqKxOzt/vE3Qo9Sqto5EdJuBxQ7LLyOd3ofg=="
BOOTSWATCH_NAV_THEME="light"

SITELOGO = '/assets/images/pic.jpg'
PYGMENTS_STYLE='monokai'
BOOTSTRAP_THEME='paper'
BOOTSTRAP_FLUID=True
COPYRIGHT_YEAR = 2016
MAIN_MENU = True
SITETITLE = 'Interpreting Models'
SITESUBTITLE = 'A journey towards model interpretability'
SITEDESCRIPTION = 'This is a collection of notes and thoughts on mathematical model interpretation via their code implementation.'
menuitems_list = [
                ("Archives", ARCHIVES_URL),
                ("Categories", CATEGORIES_URL),
                ("Tags", TAGS_URL)
                ]

def get_menuitems(siteurl, menuitems_list):
    menuitems = tuple(
            (title, "{siteurl}/{url}".format(siteurl=siteurl, url=url))
            for title, url in menuitems_list
            )
    return menuitems
MENUITEMS = get_menuitems(SITEURL, menuitems_list)
