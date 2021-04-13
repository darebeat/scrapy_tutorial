# -*- coding: utf-8 -*-

import scrapy

class JdProduct(scrapy.Item):
  collection = 'jd_product'
  dp = scrapy.Field()
  title = scrapy.Field()
  price = scrapy.Field()
  comment = scrapy.Field()
  url = scrapy.Field()
  type = scrapy.Field()