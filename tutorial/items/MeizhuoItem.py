# -*- coding: utf-8 -*-

import scrapy

class MeizhuoItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  # 图集的标题
  title = scrapy.Field()
  # 图片的url，需要来进行图片的抓取
  url = scrapy.Field()
