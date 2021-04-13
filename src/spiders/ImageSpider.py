import scrapy
from ..items.ImageItem import ImageItem
from ..configs.spider.settings import img

class ImageSpider(scrapy.Spider):
  name = 'img'
  custom_settings = img
  allowed_domains = ['lab.scrapyd.cn']
  start_urls = ['http://lab.scrapyd.cn/archives/55.html']

  def parse(self, response):
    item = ImageItem()  # 实例化item
    imgurls = response.css(".post img::attr(src)").extract() # 注意这里是一个集合也就是多张图片
    item['imgurl'] = imgurls
    yield item