# -*- coding: utf-8 -*-

import scrapy,redis,re,time,random
from scrapy import Request
from urllib.parse import quote
from ..items.TaskItem import TaskItem
from ..configs.spider.settings import mbook

class DBookMasterSpider(scrapy.Spider):
  name = 'mbook'
  custom_settings = mbook
  allowed_domains = ['book.douban.com']
  base_url = 'https://book.douban.com'

  def start_requests(self):
    """ 从redis中获取，并爬取标签对应的网页信息 """
    r = redis.Redis(host=self.custom_settings.get("REDIS_HOST"),
      port=self.custom_settings.get("REDIS_PORT"),
      db=self.custom_settings.get("REDIS_PARAMS").get('db'),
      password=self.custom_settings.get("REDIS_PARAMS").get('password'),
      decode_responses=True)
    
    while r.llen('book:tag_urls'):
      tag = r.lpop('book:tag_urls')
      url = self.base_url + quote(tag)
      yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)

  def parse(self, response):
    """ 解析每页的图书详情的url地址信息 """
    print(response.url)
    lists = response.css('#subject_list ul li.subject-item a.nbg::attr(href)').extract()
    if lists:
      for i in lists:
        item = TaskItem()
        item['url'] = i
        yield item

    #获取下一页的url地址
    next_url = response.css("span.next a::attr(href)").extract_first()
    #判断若不是最后一页
    if next_url:
      url = response.urljoin(next_url)
      #构造下一页招聘列表信息的爬取
      yield scrapy.Request(url=url,callback=self.parse)