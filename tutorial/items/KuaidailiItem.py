# -*- coding: utf-8 -*-
import scrapy

class KuaidailiItem(scrapy.Item):
  # 需要的数据现在这里制定好，因为在settings里面已近设置好了，所以可以和pipelines联系在一块处理数据
  # ip地址
  ip = scrapy.Field()
  # 端口
  port = scrapy.Field()
  # 爬取时间
  crawled = scrapy.Field()
  # 爬虫名
  spider = scrapy.Field() 
  # 来源名
  # source = scrapy.Field() 