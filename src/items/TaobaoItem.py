from scrapy import Item, Field

class TaobaoItem(Item):
  collection = 'products'

  image = Field()
  price = Field()
  deal = Field()
  title = Field()
  shop = Field()
  location = Field()