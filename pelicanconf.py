#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

'''
文档
`http://docs.getpelican.com/en/stable/settings.html#basic-settings`

# 编译成发布版
pelican content -s publishconf.py

# 推送output到博客分支上
ghp-import output -b gh-pages
git push origin gh-pages

# 编译less
lessc --plugin=less-plugin-clean-css themes/Just-Read/less/main.less \
themes/Just-Read/static/css/main.css
'''

AUTHOR = 'timkingnf'  # 作者
SITENAME = '小花园'  # 网站标题
SITEURL = ''  # 网站url
PATH = 'content'  # 源文件目录
TIMEZONE = 'Asia/Shanghai'  # 时区
DEFAULT_DATE_FORMAT = '%Y-%m-%d'  # 默认时间显示
DEFAULT_LANG = 'en'  # 默认语言
DEFAULT_PAGINATION = 10  # 默认一页显示数
STATIC_PATHS = ["images"]  # 设置静态资源
# DISQUS_SITENAME = "localhost-8000-1ujehaozhd"  # 评论插件
DISQUS_SITENAME = "https-timkingnf-github-io-blog"


# 配置渲染模版目录
DIRECT_TEMPLATES = ('index',
                    'tags',
                    'categories',
                    'archives',
                    'search')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 设置rss
FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

''' 网站外链 '''
# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('GitHub', "https://github.com/TimKingNF"),
    ('Email', "mailto:timking.nf@foxmail.com"),
)

# 告诉 pelican 在生成html的时候激活插件
'''
插件配置
* liquid: 添加对md嵌入ipython的支持。
    https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags
* ipynb: 对notebook更好的显示效果。
    https://github.com/danielfrg/pelican-ipynb/tree/b571cd86ab00af410bb47c060985fabb35e86392
* tag_cloud: 管理标签
    https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud
* pelican-toc: 生成文章目录
    https://github.com/ingwinlu/pelican-toc/tree/b98d89b2cfa857c59b647ef0983a470408d6d8cd
* neighbors: 生成导航目录
    https://github.com/getpelican/pelican-plugins/tree/master/neighbors
* sitemap: 站点地图
    https://github.com/getpelican/pelican-plugins/tree/master/sitemap
* my_search: 本地搜索, 由于tipie_search 7.0 不支持json的原因，改写了部分的tipue_search的代码
    https://github.com/getpelican/pelican-plugins/tree/master/tipue_search
    http://www.tipue.com/search/
'''
MARKUP = ('md', )
MD_EXTENSIONS = 'extra'
PLUGIN_PATHS = ['./plugins', './my-plugins']
PLUGINS = [
    'liquid_tags.notebook',
    'ipynb.liquid',
    'tag_cloud',
    'pelican-toc',
    "neighbors",
    'sitemap',
    'my-search',
]


NOTEBOOK_DIR = ""  # notebook dir 为content下的目录
TAG_CLOUD_SORTING = "size"  # tag cloud 排序规则
TAG_CLOUD_BADGE = True  # tag cloud  带上计数标签
TAG_CLOUD_STEPS = 8  # tag cloud 分页展示 8
IPYNB_IGNORE_CSS = True
IGNORE_FILES = ['.ipynb_checkpoints']  # 忽略check-point 文件夹
TOC = {
    'TOC_HEADERS': '^h[2-3]',  # 设置文档标题
    'TOC_RUN': 'true',  # 默认启用目录
    'TOC_INCLUDE_TITLE': 'false',  # 不包括文章标题
}
# 站点地图相关配置
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
GOOGLE_ANALYTICS = "UA-120924939-1"  # google 跟踪分析
REVERSE_ARCHIVE_ORDER = True  # 归档文件排序
TAG_CLOUD_STEPS = 8  # tag_cloud 分级

''' 主题与内容设置 '''
# THEME = "./themes/grey"
THEME = "./themes/Just-Read"
# THEME = "./themes/nice-blog"
# THEME = "./themes/pelican-simplegrey"
