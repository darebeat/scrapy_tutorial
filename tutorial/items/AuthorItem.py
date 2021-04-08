import scrapy

class AuthorItem(scrapy.Item):
  name = scrapy.Field()
  birthdate = scrapy.Field()
  bio = scrapy.Field()