import redis,re

class DbookMasterPipeline(object):
  def __init__(self,host,port,password):
    #连接redis数据库
    print(host,port,password)
    self.r = redis.Redis(host=host, port=port, password=password,decode_responses=True)

  @classmethod
  def from_crawler(cls,crawler):
    '''注入实例化对象（传入参数）'''
    return cls(
      host = crawler.settings.get("REDIS_HOST"),
      port = crawler.settings.get("REDIS_PORT"),
      password = crawler.settings.get('REDIS_PARAMS').get('password')
    )

  def process_item(self, item, spider):  
    #使用正则判断url地址是否有效，并写入redis。
    bookid = re.findall("book.douban.com/subject/([0-9]+)/",item['url'])
    if bookid:
      if self.r.sadd('books:id',bookid[0]):
        self.r.lpush('bookspider:start_urls', item['url'])
    else:
      self.r.lpush('bookspider:no_urls', item['url'])


class DbookSlavePipeline(object):
  def process_item(self, item, spider):
    return item