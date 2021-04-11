# -*- coding: utf-8 -*-

import scrapy,time,json,logging
from ..items.HrItem import HrItem
from ..configs.spider.settings import hr
logger = logging.getLogger(__name__)

class HrSpider(scrapy.Spider):
  name = 'hr'
  custom_settings = hr
  allowed_domains = ['tencent.com']
  start_urls = [
      'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp='
    + str(int(time.time()*1000))
    + '&pageIndex=1&pageSize=10&language=zh-cn&area=us'
  ]

  def parse(self, response):
    res = json.loads(response.text)
    posts = res['Data']['Posts']

    for post in posts:
      #构造招聘信息的Item容器对象
      item = HrItem()
      
      item["id"] = post['RecruitPostId'] # 解析id号信息，并封装到Item中
      item["title"] = post['RecruitPostName'] #标题
      item["location"] = post['LocationName'] #位置
      item["type"] = post['CategoryName'] #类别
      item["is_valid"] = post['IsValid']
      item["duty"] = post['Responsibility']
      item["updatetime"] = post['LastUpdateTime']
      logger.info(item)
      #交给管道文件
      yield item