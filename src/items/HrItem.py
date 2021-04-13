# -*- coding: utf-8 -*-

import scrapy

class HrItem(scrapy.Item):
  '''
  人事招聘信息封装类
  （职位id号，名称、位置、类别、要求、人数、职责和要求）
  '''
  table = "t_hr"  # 表名
  id = scrapy.Field() 
  title = scrapy.Field()
  location = scrapy.Field()
  type = scrapy.Field()
  is_valid = scrapy.Field()
  duty = scrapy.Field()
  updatetime = scrapy.Field()