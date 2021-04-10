# -*- coding: utf-8 -*-
import scrapy
from ..items import CoursesItem
import logging
logger = logging.getLogger(__name__)

class CoursesSpider(scrapy.Spider):
  name = 'courses'
  custom_settings = {
    'ITEM_PIPELINES':{
      'tutorial.pipelines.CoursePipeline': 300
    }
  }
  allowed_domains = ['edu.csdn.net']
  start_urls = ['https://edu.csdn.net/course?cat1=5329']
  p=1
  def parse(self, response):
    #获取所有课程
    dlist = response.selector.css("div.card_item_edu_course")
    #遍历课程，并解析信息后封装到item容器中
    for dd in dlist:
      item = CoursesItem()
      item['title'] = dd.css("div.item_title a::attr(title)").extract_first()
      item['url'] = dd.css("div.item_title a::attr(href)").extract_first()
      item['pic'] = dd.css("img::attr(src)").extract_first()
      item['teacher'] = dd.css(".item_footer_msg::text").extract_first().replace(" ",'').split('\n')[2]
      item['time'] = dd.css(".item_footer_msg").re_first("([0-9]+)人学习")
      item['price'] = dd.css(".price").re_first("￥([0-9\.]+)")
      logger.info(item)
      logger.info("-"*70)
      yield item

    #获取前10页的课程信息 
    self.p += 1
    if self.p <= 10:
      next_url = 'https://edu.csdn.net/courses/o280/p'+str(self.p)
      url = response.urljoin(next_url) #构建绝对url地址（这里可省略）
      yield scrapy.Request(url=url,callback=self.parse)