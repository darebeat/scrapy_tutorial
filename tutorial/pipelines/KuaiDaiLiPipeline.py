# -*- coding: utf-8 -*-
from datetime import datetime
import pymysql,json

class KuaidailiRedisPipeline(object):
  def process_item(self, item, spider):
    item["crawled"] = datetime.utcnow()
    item["spider"] = spider.name
    return item

# 存入到mysql中的管道类，这个不在settings里面开启，就不会影响整个工程的运行
class KuaiDaiLiPipeline(object):
  """docstring for MysqlPipeline"""
  def __init__(self):
    settings = get_project_settings()
    self.host = settings['DB_HOST']
    self.port = settings['DB_PORT']
    self.user = settings['DB_USER']
    self.pwd = settings['DB_PWD']
    self.name = settings['DB_NAME']
    self.charset = settings['DB_CHARSET']
    # 链接数据库
    self.connect()

  def connect(self):
    self.conn = pymysql.connect(host=self.host,
               port=self.port,
               user=self.user,
               password=self.pwd,
               db=self.name,
               charset=self.charset)
    self.cursor = self.conn.cursor()

  def close_spider(self, spider):
    self.conn.close()
    self.cursor.close()

  def process_item(self, item, spider):
    # sql = 'insert into ip_list(ip, port) values("%s", "%s")' % (item['ip'], item['port'])
    # # 执行sql语句
    # self.cursor.execute(sql)
    # # 提交之后才会生效
    # self.conn.commit()
    return item
