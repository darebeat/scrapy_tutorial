# -*- coding: utf-8 -*-
import scrapy

# scrapy crawl myspider1
class MySpider1(scrapy.Spider):
  name = 'myspider1'
  allowed_domains = ['darebeat.cn']
  start_urls = [
    'http://blog.darebeat.cn/article/1'
  ]

  def parse(self, response):
    self.logger.info('A response from %s just arrived!', response.url)

class MySpider2(scrapy.Spider):
  name = 'myspider2'
  allowed_domains = ['darebeat.cn']
  start_urls = [
    'http://blog.darebeat.cn/article/1'
  ]

  def parse(self, response):
    for h3 in response.xpath('//h3/text()').getall():
      yield {"title": h3}

    # for url in response.xpath('//a/@href').extract():
    #   yield scrapy.Request(url, callback=self.parse)