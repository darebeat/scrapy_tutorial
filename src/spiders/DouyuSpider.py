# -*- coding: utf-8 -*-

import scrapy,json
from ..items.DouyuItem import DouyuItem
from ..configs.spider.settings import douyu
 
class DouyuSpider(scrapy.Spider):
  name = "douyu"
  custom_settings = douyu
  allowd_domains = ["http://capi.douyucdn.cn"]
 
  offset = 0
  url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
  start_urls = [url + str(offset)]
 
  def parse(self, response):
    # 返回从json里获取 data段数据集合
    data = json.loads(response.text)["data"]
 
    for each in data:
      item = DouyuItem()
      item["name"] = each["nickname"]
      item["imagesUrls"] = each["vertical_src"]
 
      yield item
 
    self.offset += 20
    yield scrapy.Request(self.url + str(self.offset), callback = self.parse)