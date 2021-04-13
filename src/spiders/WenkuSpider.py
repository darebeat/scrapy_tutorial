# -*- coding: utf-8 -*-

# 实现一个爬取循环，获取10页信息
import scrapy

class WenkuSpider(scrapy.Spider):
  name = 'wenku'
  allowed_domains = ['wenku.baidu.com']
  start_urls = ['https://wenku.baidu.com/search?word=python&pn=0']
  p=0
  def parse(self, response):
    dllist = response.selector.xpath("//dl")
    #print(len(dllist))
    for dd in dllist:
      print(dd.xpath("./dt/p/a/@title").extract_first())

    print("="*70)

    self.p += 1
    if self.p < 10:
      next_url = 'https://wenku.baidu.com/search?word=python&pn='+str(self.p*10)
      url = response.urljoin(next_url) #构建绝对url地址（这里可省略）
      yield scrapy.Request(url=url,callback=self.parse)