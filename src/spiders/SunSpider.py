# -*- coding: utf-8 -*-
 
import scrapy
from ..items.SunItem import SupItem
from ..configs.spider.settings import sun

class SunSpider(scrapy.Spider):
  name = 'sun'
  custom_settings = sun
  allowed_domains = ['wz.sun0769.com']
  start_urls = [
    'http://wz.sun0769.com/political/index/supervise?page=1',
    'http://wz.sun0769.com/political/index/supervise?page=2',
  ]
 
  def parse(self, response):
    ullist = response.css('ul.title-state-ul li')
    for it in ullist:
      item = SupItem()
      item['sid'] = it.css(".state1::text").extract_first()
      item['title'] = it.css(".state3 a::text").extract_first()
      item['time'] = it.css(".state5::text").extract_first()
      yield item