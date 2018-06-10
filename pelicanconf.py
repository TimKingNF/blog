#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

'''
文档
`http://docs.getpelican.com/en/stable/settings.html#basic-settings`
'''

AUTHOR = 'timking'
SITENAME = '小花园'  # 网站标题
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# 告诉 pelican 在生成html的时候激活插件
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'ipynb.markup',
]

# 忽略check-point 文件夹
IGNORE_FILES = ['.ipynb_checkpoints']

# 设置主题
THEME = "./themes/grey"

# 设置资源
STATIC_PATHS = ["images"]
