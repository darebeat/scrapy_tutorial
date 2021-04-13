# -*- coding: utf-8 -*-

import scrapy

class CoserItem(scrapy.Item):
  url = scrapy.Field()
  name = scrapy.Field()
  info = scrapy.Field()
  cover = scrapy.Field()