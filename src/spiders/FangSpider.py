# -*- coding: utf-8 -*-

import scrapy,logging
from ..items.FangItem import FangItem
from ..configs.spider.settings import fang
logger = logging.getLogger(__name__)

class FangSpider(scrapy.Spider):
  name = 'fang'
  allowed_domains = ['fang.5i5j.com']
  custom_settings = fang
  #start_urls = ['http://fang.5i5j.com/']
  start_urls = ['https://fang.5i5j.com/bj/loupan/']

  def parse(self, response):
    hlist = response.css("ul li.houst_ctn")
    for vo in hlist:
      item = FangItem()
      item['title'] = vo.css(".house_name::text").extract_first()
      item['address'] = vo.css(".house_info_text_address span::text").extract()[3]
      item['time'] = '-'.join(vo.css("div.house_info.left > div:nth-child(4) span::text").extract())
      item['clicks'] = vo.css("div.house_price.right span i::text").extract_first()
      item['price'] = vo.css("div.house_price.right p::text").extract_first()
      logger.info(item)
      yield item