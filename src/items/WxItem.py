# -*- coding: utf-8 -*-

import scrapy

# 定义信息封装类（标题、摘要、公众号、时间、URL地址）
class WxItem(scrapy.Item):
  # define the fields for your item here like:
  collection = 'wx'
  title = scrapy.Field()
  content = scrapy.Field()
  nickname = scrapy.Field()
  date = scrapy.Field()
  url = scrapy.Field()
