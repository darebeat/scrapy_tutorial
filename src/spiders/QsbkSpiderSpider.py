# -*- coding: utf-8 -*-

import scrapy
import logging
logger = logging.getLogger(__name__)

class QsbkSpiderSpider(scrapy.Spider):
  name = 'qsbk'
  allowed_domains = ['qiushibaike.com']
  start_urls = ['http://qiushibaike.com/']

  def parse(self, response):
    item = {}
    # 我们进行奇数偶数的不同参数处理
    for i in range(0, 50):
      if (i % 2) == 0:
        # 偶数处理
        item['come_from'] = 'oushu'
        item['data'] = i
      else:
        # 奇数处理
        item['come_from'] = 'jishu'
        item['data'] = i
      logger.warning(item)
      yield item
