from scrapy_redis.spiders import RedisSpider
from ..items import KuaidailiItem

class KuaidailiSpider(RedisSpider):
  """Spider that reads urls from redis queue (KuaidailiSpider:start_urls)."""
  name = 'kdl'
  custom_settings = {
    'ITEM_PIPELINES': {
      'tutorial.pipelines.KuaidailiRedisPipeline': 300,
      'tutorial.pipelines.KuaidailiPipeline': 301,
      'scrapy_redis.pipelines.RedisPipeline': 400,
    }
  }
  
  # 注意这里原本应该是start_urls，但是使用redis后变成redis_key
  redis_key = 'kdl:start_urls'
  
	# 这里本来应该是 allowed_domains = ['www.kuaidaili.com'] ，然后变成自动捕捉的，
	#值得注意的是这里使用allowed_domains = ['www.kuaidaili.com']仍然有效
  def __init__(self, *args, **kwargs):
    # Dynamically define the allowed domains list.
    domain = kwargs.pop('domain', '')
    self.allowed_domains = filter(None, domain.split(','))
    super(KuaidailiSpider, self).__init__(*args, **kwargs)

  def parse(self, response):
    print('开始爬取...')
    ip_list = response.xpath('//tbody/tr/td[1]/text()').extract()
    port_list = response.xpath('//tbody/tr/td[2]/text()').extract()
    for i in range(len(ip_list)):
      item = KuaidailiItem()
      item['ip'] = ip_list[i]
      item['port'] = port_list[i]
      yield item
