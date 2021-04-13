# -*- coding: utf-8 -*-

import scrapy

class ImdbItem(scrapy.Item):
  # define the fields for your item here like:
  url = scrapy.Field()        #url
  title = scrapy.Field()      #影片名