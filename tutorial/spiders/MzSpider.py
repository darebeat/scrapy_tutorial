# -*- coding: utf-8 -*-

import scrapy
from ..items.MeizhuoItem import MeizhuoItem
from ..configs.spider.settings import mz

class MzSpider(scrapy.Spider):
  name = 'mz'
  custom_settings = mz
  allowed_domains = ['www.win4000.com']
  start_urls = [ 'http://www.win4000.com/wallpaper_2285_0_0_1.html' ]

  def parse(self, response):
    list = response.xpath('//*[@class="list_cont Left_list_cont"]/div/div/div/ul/li/a')

    for img in list:
      # 这个是每个图集得到的url
      url = img.xpath('@href').extract_first()
      title = img.xpath('@title').extract_first()
      # 对我的每一个URL进行解析
      yield scrapy.Request(url, callback=self.get_all_img, meta={'title': title})
    # 对于下一页进行定位，如果存在就进行跳转
    next_url = response.xpath('//*[@class="next"]/@href').extract_first()
    if next_url is not None:
      yield scrapy.Request(next_url, callback=self.parse)

  def get_all_img(self, response):
    item = MeizhuoItem()

    # 这个是所有照片的所有的总共的页数
    img_list = response.xpath('//*[@class="scroll-img-cont"]/ul')
    for img in img_list:
      img_url = img.xpath('li/a/img/@src').extract()
      for url in img_url:
        # 这个url还是需要经过处理的，所以要循环出来挨个进行修改
        cmp_url = url.split('_')[0] + '.jpg'
      item['url'] = cmp_url
      item['title'] = response.meta['title']
      print(item)
      yield item
      