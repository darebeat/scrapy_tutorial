from scrapy import Item,Field

class FangItem(Item):
  title = Field()
  address = Field()
  time = Field()
  clicks = Field()
  price = Field()

class NewhouseItem(Item):
  province = Field()  # 省份
  city = Field()  # 城市
  name = Field()  # 小区名
  price = Field()  # 价格
  rooms = Field()  #居室 这是个列表
  area = Field()  #面积
  address = Field()  # 地址
  district = Field()  # 行政区
  sale = Field()  # 是否在售
  origin_url = Field()  # 房天下详情页面的url


# 二手房item
class EsfItem(Item):
  province = Field()  # 省份
  city = Field()  # 城市
  name = Field()  # 小区名
  price = Field()  # 价格
  rooms = Field()  # 居室,几室几厅这是个列表
  area = Field()  # 建筑面积
  toward = Field()  # 朝向
  address = Field()  # 地址
  unit = Field()  # 单价
  floor = Field()  # 楼层
  year = Field()  # 建成年代
  origin_url = Field()  # 房天下详情页面的url