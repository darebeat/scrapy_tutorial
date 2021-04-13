# -*- coding: utf-8 -*-

import scrapy
 
class SunItem(scrapy.Item):
  # 每个帖子的标题
  title = scrapy.Field()
  # 每个帖子的编号
  number = scrapy.Field()
  # 每个帖子的文字内容
  content = scrapy.Field()
  # 每个帖子的url
  url = scrapy.Field()

class SupItem(scrapy.Item):
  sid = scrapy.Field()
  title = scrapy.Field()
  time = scrapy.Field()