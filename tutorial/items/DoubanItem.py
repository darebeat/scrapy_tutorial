import scrapy

class DoubanItem(scrapy.Item):
  item_id = scrapy.Field() # ID
  item_name = scrapy.Field() # 小项名称
  url = scrapy.Field() # URL  # 小项的链接
  info = scrapy.Field() # 小项的详细信息
  rating = scrapy.Field() # 小项的评分信息
  comment = scrapy.Field() # 评论次数