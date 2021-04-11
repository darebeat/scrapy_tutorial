import scrapy

class ImageItem(scrapy.Item):
  imgurl = scrapy.Field()