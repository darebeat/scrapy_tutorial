import scrapy
import logging
logger = logging.getLogger(__name__)

class RenrenSpider(scrapy.Spider):
  name = 'renren'
  allowed_domains = ['renren.com']
  start_urls = ['http://renren.com/']

  def start_requests(self):
    url = 'http://www.renren.com/PLogin.do'
    data = {
      'email': '1861****517',
      'password': '********'
    }
    request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)
    yield request

  @staticmethod
  def parse_page(self, response):
    with open('renren.html', 'w', encoding='utf-8') as fp:
      fp.write(response.text)
