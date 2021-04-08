# -*- coding: utf-8 -*-

# 导入 cmdline模块,可以控制终端命令行
from scrapy import cmdline

# 使用execute()方法,输入运行scrapy的命令
cmdline.execute(['scrapy', 'crawl', 'author'])