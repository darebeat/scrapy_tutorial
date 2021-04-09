from scrapy import Item,Field

class FangItem(Item):
  title = Field()
  address = Field()
  time = Field()
  clicks = Field()
  price = Field()