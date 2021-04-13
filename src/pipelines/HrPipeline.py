# -*- coding: utf-8 -*-

import pymysql

class HrPipeline(object):
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
    '''执行数据表的写入操作'''
    #组装sql语句
    data = dict(item)
    keys = ','.join(data.keys())
    values=','.join(['%s']*len(data))
    sql = "insert into %s(%s) values(%s)"%(item.table,keys,values)
    #指定参数，并执行sql添加
    self.cursor.execute(sql,tuple(data.values()))
    #事务提交
    self.db.commit()
    return item

  def close_spider(self, spider):
    self.cursor.close()
    self.db.close()