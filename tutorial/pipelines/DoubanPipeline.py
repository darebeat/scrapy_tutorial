# -*- coding: utf-8 -*-

import pymysql
from tutorial import settings

class DoubanPipeline(object):
  def __init__(self):
    # 连接数据库
    self.connect = pymysql.connect(
      host=settings.MYSQL_HOST,
      port=settings.MYSQL_PORT,
      database=settings.MYSQL_DBNAME,
      user=settings.MYSQL_USER,
      password=settings.MYSQL_PASSWD,
      charset='utf8mb4',
      use_unicode=True)

    # 通过cursor执行增删查改
    self.cursor = self.connect.cursor();

  def process_item(self, item, spider):
    try:
      # 查重处理
      self.cursor.execute(
        """select * from t_douban where item_id = %s""",
        item['item_id'])
      # 是否有重复数据
      repetition = self.cursor.fetchone()

      # 重复
      if repetition:
        pass
      else:
        # 插入数据
        self.cursor.execute(
          """
          insert into t_douban(item_id, item_name, url, info, rating, comment) 
          value (%s, %s, %s, %s, %s, %s)
          """, (
            item['item_id'],
            item['item_name'],
            item['url'],
            item['info'],
            item['rating'],
            item['comment']
          ))

      # 提交sql语句
      self.connect.commit()
    except Exception as error:
      # 出现错误时打印错误日志
      print(error)

    return item