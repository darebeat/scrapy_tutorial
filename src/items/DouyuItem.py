# -*- coding: utf-8 -*-

from scrapy import Item,Field

class DouyuItem(Item):
  name = Field()# 存储照片的名字
  imagesUrls = Field()# 照片的url路径
  imagesPath = Field()# 照片保存在本地的路径