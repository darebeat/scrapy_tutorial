# -*- coding: utf-8 -*-

import scrapy

class SFItem(scrapy.Item):
  title = scrapy.Field()
  votes = scrapy.Field()
  body = scrapy.Field()
  tags = scrapy.Field()
  link = scrapy.Field()