# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from urllib.parse import quote
from bs4 import BeautifulSoup
from ..items.JdProduct import JdProduct
from ..configs.spider.settings import jd
import logging
logger = logging.getLogger(__name__)

class JdSpider(Spider):
  name = 'jd'
  custom_settings = jd
  allowed_domains = ['www.jd.com']
  base_url = 'https://search.jd.com/Search?keyword='
 
  def start_requests(self):
    for keyword in self.settings.get('KEYWORDS'):
      for page in range(1, self.settings.get('MAX_PAGE') + 1):
        url = self.base_url + quote(keyword)
        # dont_filter = True  不去重
        yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)
  
  def parse(self, response):
    soup = BeautifulSoup(response.text, 'lxml')
    lis = soup.find_all(name='li', class_="gl-item")
    for li in lis:
      item = JdProduct()
      dp = li.find(name='span', class_="J_im_icon")
      if dp:
        item['dp'] = dp.get_text().strip()
      else:
        continue
      id = li.attrs['data-sku']
      title = li.find(name='div', class_="p-name p-name-type-2")
      item['title'] = title.get_text().strip()
      price = li.find(name='strong', class_="J_" + id)
      item['price'] = price.get_text()
      comment = li.find(name='a', id="J_comment_" + id)
      item['comment'] = comment.get_text() + '条评论'
      url = 'https://item.jd.com/' + id + '.html'
      item['url'] = url
      item['type'] = 'JINGDONG'
      logger.info(item)
      yield item