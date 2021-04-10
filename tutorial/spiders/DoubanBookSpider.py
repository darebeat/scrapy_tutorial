# -*- coding: utf-8 -*-

import scrapy,redis,re,time,random
from ..items import TaskItem,BookItem
from scrapy_redis.spiders import RedisSpider
from urllib.parse import quote

class DBookMasterSpider(scrapy.Spider):
  name = 'mbook'
  allowed_domains = ['book.douban.com']
  base_url = 'https://book.douban.com'

  custom_settings = {
    'ITEM_PIPELINES':{
      'tutorial.pipelines.DbookMasterPipeline': 300,
      'scrapy_redis.pipelines.RedisPipeline': 400,
    },
    'REDIS_PARAMS': {
      'db': 0
    }
  }

  def start_requests(self):
  ''' 从redis中获取，并爬取标签对应的网页信息 '''
  r = redis.Redis(
    host=self.settings.get("REDIS_HOST"), 
    port=self.settings.get("REDIS_PORT"), 
    password=self.settings.get('REDIS_PARAMS').get('password'),
    decode_responses=True)
  while r.llen('book:tag_urls'):
    tag = r.lpop('book:tag_urls')
    url = self.base_url + quote(tag)
    yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)

  def parse(self, response):
  ''' 解析每页的图书详情的url地址信息 '''
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




class DBookSlaveSpider(RedisSpider):
  name = 'sbook'
  custom_settings = {
    'ITEM_PIPELINES':{
      'tutorial.pipelines.DbookSlavePipeline': 300,
      'scrapy_redis.pipelines.RedisPipeline': 400,
    },
    'REDIS_PARAMS': {
      'db': 0
    }
  }
  #allowed_domains = ['book.douban.com']
  #start_urls = ['http://book.douban.com/']
  redis_key = "bookspider:start_urls"

  def __init__(self, *args, **kwargs):
    # Dynamically define the allowed domains list.
    domain = kwargs.pop('domain', '')
    self.allowed_domains = filter(None, domain.split(','))
    super(SlaveSpider, self).__init__(*args, **kwargs)

  def parse(self, response):
    print("======================",response.status)
    item = BookItem()
    vo = response.css("#wrapper")
    item['id'] = vo.re_first('id="collect_form_([0-9]+)"') #ID号
    item['title'] = vo.css("h1 span::text").extract_first() #书名

    #使用正则获取里面的info里面的图书信息
    info = vo.css("#info").extract_first()
    #print(info)
    authors = re.search('<span.*?作者.*?</span>(.*?)<br>',info,re.S).group(1)
    item['author'] = "、".join(re.findall('<a.*?>(.*?)</a>',authors,re.S)) #作者
    item['press'] = " ".join(re.findall('<span.*?出版社:</span>\s*(.*?)<br>',info)) #出版社
    item['original'] = " ".join(re.findall('<span.*?原作名:</span>\s*(.*?)<br>',info)) #原作名
    yz = re.search('<span.*?译者.*?</span>(.*?)<br>',info,re.S)
    if yz:
      item['translator'] = "、".join(re.findall('<a.*?>(.*?)</a>',yz.group(1),re.S)) #译者
    else:
      item['translator'] = ""
    item['imprint'] = re.search('<span.*?出版年:</span>\s*([0-9\-]+)<br>',info).group(1) #出版年
    item['pages'] = re.search('<span.*?页数:</span>\s*([0-9]+)<br>',info).group(1) #页数
    item['price'] = re.search('<span.*?定价:</span>.*?([0-9\.]+)元?<br>',info).group(1) #定价
    item['binding'] = " ".join(re.findall('<span.*?装帧:</span>\s*(.*?)<br>',info,re.S)) #装帧
    item['series'] = " ".join(re.findall('<span.*?丛书:</span>.*?<a .*?>(.*?)</a><br>',info,re.S)) #丛书
    item['isbn'] = re.search('<span.*?ISBN:</span>\s*([0-9]+)<br>',info).group(1) #ISBN

    item['score'] = vo.css("strong.rating_num::text").extract_first().strip() #评分
    item['number'] = vo.css("a.rating_people span::text").extract_first() #评论人数
    #print(item)
    yield item