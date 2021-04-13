# -*- coding: utf-8 -*-
 
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items.QdItem import QdItem
from ..configs.spider.settings import qd
import requests

class QdSpider(CrawlSpider):
  name = 'qd'
  custom_settings = qd
  # allowed_domains = ['qidian.com']
  start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']
  rules = (
    #匹配全部主页面的url规则  深度爬取子页面
    Rule(LinkExtractor(allow=(r'https://www.qidian.com/all\?orderId=\&style=1\&pageSize=20\&siteid=1\&pubflag=0\&hiddenField=0\&page=(\d+)')),follow=True),
    #匹配详情页面 不作深度爬取
    Rule(LinkExtractor(allow=r'https://book.qidian.com/info/(\d+)'), callback='parse_item', follow=False),
  )
  
  def parse_item(self, response):
    item=QdItem()
    item['book_name']=self.get_book_name(response)
    item['author']=self.get_author(response)
    item['state']=self.get_state(response)
    item['type']=self.get_type(response)
    item['about']=self.get_about(response)
    item['score']=self.get_score(response)
    item['story']=self.get_story(response)
    item['news']=self.get_news(response)
    yield item
  
  def get_book_name(self,response):
    book_name=response.xpath('//h1/em/text()').extract()[0]
    if len(book_name)>0:
      book_name=book_name.strip()
    else:
      book_name='NULL'
    return book_name
  
  def get_author(self,response):
    author=response.xpath('//h1/span/a/text()').extract()[0]
    if len(author)>0:
      author=author.strip()
    else:
      author='NULL'
    return author
  
  def get_state(self,response):
    state=response.xpath('//p[@class="tag"]/span/text()').extract()[0]
    if len(state)>0:
      state=state.strip()
    else:
      st='NULL'
    return state
  
  def get_type(self,response):
    type=response.xpath('//p[@class="tag"]/a/text()').extract()
    if len(type)>0:
      t=""
      for i in type:
        t+=' '+i
      type=t
    else:
      type='NULL'
    return type
  
  def get_about(self,response):
    about=response.xpath('//p[@class="intro"]/text()').extract()[0]
    if len(about)>0:
      about=about.strip()
    else:
      about='NULL'
    return about
  
  def get_score(self,response):
    
    def get_sc(id):
      urll = 'https://book.qidian.com/ajax/comment/index?_csrfToken=ziKrBzt4NggZbkfyUMDwZvGH0X0wtrO5RdEGbI9w&bookId=' + id + '&pageSize=15'
      rr = requests.get(urll)
      # print(rr)
      score = rr.text[16:19]
      return score
    bid=response.xpath('//a[@id="bookImg"]/@data-bid').extract()[0]     #获取书的id
    if len(bid)>0:
      score=get_sc(bid)       #调用方法获取评分 若是整数 可能返回 9，"
      if score[1]==',':
        score=score.replace(',"',".0")
      else:
        score=score
    else:
      score='NULL'
    return score
  
  def get_story(self,response):
    story=response.xpath('//div[@class="book-intro"]/p/text()').extract()[0]
    if len(story)>0:
      story=story.strip()
    else:
      story='NULL'
    return story
  
  def get_news(self,response):
    news=response.xpath('//div[@class="detail"]/p[@class="cf"]/a/text()').extract()[0]
    if len(news)>0:
      news=news.strip()
    else:
      news='NULL'
    return news