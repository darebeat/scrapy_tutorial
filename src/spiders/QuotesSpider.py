# -*- coding: utf-8 -*-

import scrapy
from ..items import AuthorItem

# scrapy crawl q1
class QuotesSpider(scrapy.Spider):
  name = "q1"

  def start_requests(self):
    urls = [
      'http://quotes.toscrape.com/page/1/',
      'http://quotes.toscrape.com/page/2/',
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    page = response.url.split("/")[-2]
    filename = 'out/quotes-%s.html' % page
    with open(filename, 'wb') as f:
      f.write(response.body)
    self.log('Saved file %s' % filename)

# scrapy crawl q2 -o out/quotes.json
# scrapy crawl q2 -o out/quotes.jl
class Quotes2Spider(scrapy.Spider):
  name = "q2"
  start_urls = [
    'http://quotes.toscrape.com/page/1/',
    'http://quotes.toscrape.com/page/2/',
  ]

  def parse(self, response):
    for quote in response.css('div.quote'):
      yield {
        'text': quote.css('span.text::text').extract_first(),
        'author': quote.css('small.author::text').extract_first(),
        'tags': quote.css('div.tags a.tag::text').extract(),
      }

# 递归的跟随到下一页的链接，从中提取数据
# scrapy crawl q2 -o out/quotes3.json
class Quotes3Spider(scrapy.Spider):
  name = "q3"
  start_urls = [
    'http://quotes.toscrape.com/page/1/',
  ]

  def parse(self, response):
    for quote in response.css('div.quote'):
      yield {
        'text': quote.css('span.text::text').extract_first(),
        'author': quote.css('small.author::text').extract_first(),
        'tags': quote.css('div.tags a.tag::text').extract(),
      }

    next_page = response.css('li.next a::attr(href)').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback=self.parse)

# 使用爬虫参数
# scrapy crawl q4 -o quotes-humor.json -a tag=humor
class Quotes4Spider(scrapy.Spider):
  name = "q4"

  def start_requests(self):
    url = 'http://quotes.toscrape.com/'
    tag = getattr(self, 'tag', None)
    if tag is not None:
      url = url + 'tag/' + tag
    yield scrapy.Request(url, self.parse)

  def parse(self, response):
    for quote in response.css('div.quote'):
      yield {
        'text': quote.css('span.text::text').extract_first(),
        'author': quote.css('small.author::text').extract_first(),
      }

    next_page = response.css('li.next a::attr(href)').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, self.parse)
