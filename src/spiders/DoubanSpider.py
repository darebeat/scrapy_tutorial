# -*- coding: utf-8 -*-

import scrapy,re,logging
from ..items.DoubanItem import DoubanItem
from ..configs.spider.settings import douban
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

class DoubanSpider(scrapy.Spider):
  # name 是每个爬虫项目的唯一名字,用于区分不同的Spider爬虫
  name = 'douban'  # 这是 scrapy 爬虫程序的唯一标识
  custom_settings = douban
  # 这里是允许爬取的域名,如果初试或者后续的请求链接不是这个域名,则请求链接就会被过滤掉
  allowed_domains = ['douban.com']  # 允许爬虫爬取的域名(url)范围
  # 它包含了Spider在启动的时候,爬取的URL列表,初试请求是由它来定义的
  start_urls = ['https://movie.douban.com/chart']   # 爬虫程序最开始(起始)的爬取url

  # parse 解析提取
  def parse(self, response):
    # 转换为bs4对象
    bs_response = BeautifulSoup(response.text,'html.parser')
    move_list = bs_response.find_all('div',class_="pl2")
    
    for it in move_list:
      # 实例化一个管道对象
      item = DoubanItem()
      item["item_name"] = it.find('a').text.replace('\n','').replace(' ','')
      item["url"] = it.find('a')['href']
      item['item_id'] = re.search('(\d+)',item["url"]).group(1)
      item['info'] = it.find('p').text
      item['rating'] = it.find("span",class_="rating_nums").text
      item['comment'] = re.search('(\d+)',it.find("span",class_="pl").text).group(1)
      logger.warning(item)
      yield item

