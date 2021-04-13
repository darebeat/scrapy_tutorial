# -*- coding: utf-8 -*-

from scrapy import Field,Item
class QdItem(Item):
  # define the fields for your item here like:
  book_name = Field()            #书名
  author = Field()               #作者
  state = Field()                #状态
  type = Field()                 #类型
  about = Field()                #简介
  score = Field()                #评分
  story = Field()                #故事
  news = Field()                 #最新章节