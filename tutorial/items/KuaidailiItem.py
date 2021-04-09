# -*- coding: utf-8 -*-
from scrapy import Item,Field

class KuaidailiItem(Item):
    # 需要的数据现在这里制定好，因为在settings里面已近设置好了，所以可以和pipelines联系在一块处理数据
    # ip地址
    ip = Field()
    # 端口
    port = Field()
    # 爬取时间
    crawled = Field()
    # 爬虫名
    spider = Field() 
    # 来源名
    # sourec = Field()  