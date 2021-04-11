import requests
import scrapy
from scrapy.selector import Selector
from fake_useragent import UserAgent
from ..items.MeizhuoItem import MeizhuoItem

headers = {
  'user-agent': UserAgent(verify_ssl=False).chrome
}


class MzSpider(scrapy.Spider):
  name = 'mz'
  allowed_domains = ['www.win4000.com']
  start_urls = [
    'http://www.win4000.com/zt/shuaige.html'
  ]

  def parse(self, response):
    sel = Selector(response)

    for img in sel.xpath('//*[@class="tab_tj"]/div/div/ul/li/a'):
      url = img.xpath('@href').extract_first()
      title = img.xpath('@title').extract_first()
      if title:
      # print(title)
        yield scrapy.Request(url, callback=self.parse_img, dont_filter=False, meta={'title': title})
    next_url = sel.xpath('//a[@class="next"]/@href').extract_first()
    # print('next_url', next_url)
    if next_url is not None:
      yield scrapy.Request(next_url, callback=self.parse, dont_filter=False, headers=headers)
      # print(next_url.extract_first())

      # cmp_img = container.append(img.xpath(''))

  #
  def parse_img(self, response):
    sel = Selector(response)
    # 这个图集url
    # print(response)
    item = MeizhuoItem()
    container = []
    """
    1、首先需要计算总的页数
    2、然后根据页数来进行循环便利，以拿到每一页的图片
    这个是源码中的内容  http://pic1.win4000.com/wallpaper/2019-07-19/5d3163399fd38_120_80.jpg
    网页中的连接     http://pic1.win4000.com/wallpaper/2019-07-19/5d3163399fd38.jpg
    
    cmp_url      http://www.win4000.com/wallpaper_detail_160109_2.jpg
    """
    for img in sel.xpath('//*[@class="scroll-img-cont"]/ul/li/a/img/@data-original'):
      cmp_url = img.extract()
      url = cmp_url.split('_')[0] + '.jpg'
      container.append(url)
    item['url'] = container
    item['title'] = response.meta['title']
    yield item
    container.clear()

