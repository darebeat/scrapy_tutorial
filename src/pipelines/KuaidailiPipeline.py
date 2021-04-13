# -*- coding: utf-8 -*-
from datetime import datetime
import pymysql,logging
logger = logging.getLogger(__name__)

class KuaidailiRedisPipeline(object):
  def process_item(self, item, spider):
    item["crawled"] = datetime.utcnow()
    item["spider"] = spider.name
    return item

# 存入到mysql中的管道类，这个不在settings里面开启，就不会影响整个工程的运行
class KuaidailiPipeline(object):
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
      self.cursor.execute("""select ip from t_kdl where ip = %s""", item["ip"])
      ret = self.cursor.fetchone()
      if ret:
        self.cursor.execute(
          """ update t_kdl set port = %s, crawled = %s, spider = %s where ip = %s """,(
            item['port'],
            item['crawled'],
            item['spider']
          ))
      else:
        self.cursor.execute(
          """ insert into t_kdl( ip, port, crawled, spider ) value (%s,%s,%s,%s) """,(
            item['ip'],
            item['port'],
            item['crawled'],
            item['spider']
          ))
      self.db.commit()
    except Exception as e:
      logger.error(e)
    return item

  def close_spider(self, spider):
    self.cursor.close()
    self.db.close()
