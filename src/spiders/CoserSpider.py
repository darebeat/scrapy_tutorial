# -*- coding: utf-8 -*-

import scrapy,json
from ..items.CoserItem import CoserItem
from ..configs.spider.settings import coser
 
class CoserSpider(scrapy.Spider):
  name = "coser"
  custom_settings = coser
  allowed_domains = ["bcy.net"]
  offset = 1
  url = "https://bcy.net/apiv3/rank/list/itemInfo?ttype=illust&sub_type=week&p="
  start_urls = [url + str(offset)]
 
  def parse(self, response):
    # 返回从json里获取 data段数据集合
    data = json.loads(response.text)["data"]["top_list_item_info"]
 
    for each in data:
      item = CoserItem()
      detail = each["item_detail"]
      item["url"] = "https://bcy.net/item/detail/"+detail["item_id"]
      item["name"] = detail["uname"]
      item["info"] = detail["plain"]
      item["cover"] = detail["cover"]
      yield item

    if self.offset <= 3:
      self.offset += 1
    yield scrapy.Request(self.url + str(self.offset), callback = self.parse)