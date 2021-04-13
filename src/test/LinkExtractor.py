# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor

class WeidsSpider(scrapy.Spider):
  name = "weids"
  allowed_domains = ["wds.modian.com"]
  start_urls = ['http://www.gaosiedu.com/gsschool/']

  def parse(self, response):
    pattern = '/gsschool/.+\.shtml'
    link = LinkExtractor(allow=pattern)
    links = link.extract_links(response)
    print(type(links))
    for link in links:
      print(link)