#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Shubhanshu Mishra'
SITENAME = u'Interpreting Models'
SITEURL = 'http://shubhanshu.com/blog'

GITHUB_URL='https://github.com/napsternxg/blog'
PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Homepage', 'http://shubhanshu.com/'),
        ('Projects', 'http://shubhanshu.com/playground.html'),
        ('Blog Repo', GITHUB_URL),
        )

# Social widget
SOCIAL = (('website', 'http://shubhanshu.com'),
    ('twitter', 'http://twitter.com/TheShubhanshu'),
    ('linkedin', 'http://www.linkedin.com/in/shubhanshumishra'),
    ('github', 'http://github.com/napsternxg'),
    ('rss', '//shubhanshu.com/blog/feeds/all.atom.xml')
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']

## PATHS
OUTPUT_PATH="docs"
# put articles (posts) in blog/
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'index.html'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'    
TAG_SAVE_AS = 'blog/tag/{slug}.html'    
TAGS_URL = 'blog/tag/'  
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


DISQUS_SITENAME = "shubhanshu-blog"
IPYNB_IGNORE_CSS = True
GOOGLE_ANALYTICS='UA-44393164-1'
TWITTER_USERNAME='TheShubhanshu'
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

# THEME SETTINGS
#THEME='../pelican-themes/pelican-bootstrap3'
THEME='../pelican-themes/Flex'
SITELOGO = '/assets/images/pic.jpg'
PYGMENTS_STYLE='friendly'
BOOTSTRAP_THEME='paper'
BOOTSTRAP_FLUID=True
COPYRIGHT_YEAR = 2016
MAIN_MENU = True
SITETITLE = 'Interpreting Models'
SITESUBTITLE = 'A quest to make models interpretable'
SITEDESCRIPTION = '%s\'s thoughts on mathematical models and code' % AUTHOR
MENUITEMS = (('Archives', '/blog/%s' % ARCHIVES_URL),
    ('Categories', '/blog/%s' % CATEGORIES_URL),
    ('Tags', '/blog/%s' % TAGS_URL),)
