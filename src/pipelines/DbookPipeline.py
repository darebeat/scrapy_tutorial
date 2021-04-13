# -*- coding: utf-8 -*-

import redis,re,pymysql,logging
from ..items.DoubanItem import BookItem
from ..configs import redis as rconf
logger = logging.getLogger(__name__)

class DbookMasterPipeline(object):
  def __init__(self,host,port,db,password):
    #连接redis数据库
    self.r = redis.Redis(host=host,port=port,db=db,password=password,decode_responses=True)

  @classmethod
  def from_crawler(cls,crawler):
    '''注入实例化对象（传入参数）'''
    return cls(
      host = rconf.REDIS_HOST,
      port = rconf.REDIS_PORT,
      db = rconf.REDIS_PARAMS['db'],
      password = rconf.REDIS_PARAMS['password']
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
  def __init__(self,host,user,password,database,port):
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    self.port = port

  @classmethod
  def from_crawler(cls,crawler):
    return cls(
      host = crawler.settings.get("MYSQL_HOST"),
      database = crawler.settings.get("MYSQL_DBNAME"),
      user = crawler.settings.get("MYSQL_USER"),
      password = crawler.settings.get("MYSQL_PASSWD"),
      port = crawler.settings.get("MYSQL_PORT")
    )

  def open_spider(self, spider):
    '''负责连接数据库'''
    self.db = pymysql.connect(
      host=self.host,
      port=self.port,
      database=self.database,
      user=self.user,
      password=self.password,
      charset='utf8mb4',
      use_unicode=True
    )
    self.cursor = self.db.cursor()

  def process_item(self, item, spider):
    try:
      self.cursor.execute("""select id from t_douban_book where id = %s""", item["id"])
      ret = self.cursor.fetchone()
      if ret:
        self.cursor.execute(
          """
          update t_douban_book set
            title = %s,
            author = %s,
            press = %s,
            original = %s,
            translator = %s,
            imprint = %s,
            pages = %s,
            price = %s,
            binding = %s,
            series = %s,
            isbn = %s,
            score = %s,
            number = %s
          where id = %s
          """,(
            item['title'],
            item['author'],
            item['press'],
            item['original'],
            item['translator'],
            item['imprint'],
            item['pages'],
            item['price'],
            item['binding'],
            item['series'],
            item['isbn'],
            item['score'],
            item['number']
          ))
      else:
        self.cursor.execute(
          """
          insert into t_douban_book(
            id,
            title,
            author,
            press,
            original,
            translator,
            imprint,
            pages,
            price,
            binding,
            series,
            isbn,
            score,
            number
          ) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
          """,(
            item['id'],
            item['title'],
            item['author'],
            item['press'],
            item['original'],
            item['translator'],
            item['imprint'],
            item['pages'],
            item['price'],
            item['binding'],
            item['series'],
            item['isbn'],
            item['score'],
            item['number']
          ))
      self.db.commit()
    except Exception as e:
      logger.error(e)
    return item