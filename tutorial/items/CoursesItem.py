import scrapy

class CoursesItem(scrapy.Item):
  title = scrapy.Field()
  url = scrapy.Field()
  pic = scrapy.Field()
  teacher = scrapy.Field()
  time = scrapy.Field()
  price = scrapy.Field()