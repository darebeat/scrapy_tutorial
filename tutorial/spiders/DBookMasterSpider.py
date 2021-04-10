# -*- coding: utf-8 -*-
import scrapy
from ..items import TaskItem 
from scrapy import Request
from urllib.parse import quote
import redis,re,time,random

class DBookMasterSpider(scrapy.Spider):
  name = 'mbook'
  allowed_domains = ['book.douban.com']
  base_url = 'https://book.douban.com'

  custom_settings = {
    'ITEM_PIPELINES':{
      'tutorial.pipelines.DbookMasterPipeline': 300,
      'scrapy_redis.pipelines.RedisPipeline': 400,
    }
  }

  def start_requests(self):
    """ 从redis中获取，并爬取标签对应的网页信息 """
    r = redis.Redis(host=self.settings.get("REDIS_HOST"),
      port=self.settings.get("REDIS_PORT"),
      db=0,
      password=self.settings.get("REDIS_PARAMS").get('password'),
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