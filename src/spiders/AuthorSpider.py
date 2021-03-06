# -*- coding: utf-8 -*-

import scrapy,logging
from ..items.AuthorItem import AuthorItem
from ..configs.spider.settings import author
logger = logging.getLogger(__name__)

class AuthorsSpider(scrapy.Spider):
  name = 'author'
  custom_settings = author
  start_urls = ['http://quotes.toscrape.com/']

  def parse(self, response):
    # follow links to author pages
    for href in response.css('.author + a::attr(href)').extract():
      yield scrapy.Request(response.urljoin(href), callback=self.parse_author)

    # follow pagination links
    next_page = response.css('li.next a::attr(href)').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)

  def parse_author(self, response):
    def extract_with_css(query):
      return response.css(query).extract_first().strip()

    # 实例化一个管道对象
    item = AuthorItem()
    item["name"] = extract_with_css('h3.author-title::text')
    item["birthdate"] = extract_with_css('.author-born-date::text')
    item['bio'] = extract_with_css('.author-description::text')
    logger.warning(item)
    yield item