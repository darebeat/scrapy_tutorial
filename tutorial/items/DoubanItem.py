from scrapy import Item,Field

class DoubanItem(Item):
  item_id = Field() # ID
  item_name = Field() # 小项名称
  url = Field() # URL  # 小项的链接
  info = Field() # 小项的详细信息
  rating = Field() # 小项的评分信息
  comment = Field() # 评论次数