# -*- coding: utf-8 -*-

import pymysql
import logging
from tutorial import settings

class AuthorPipeline:
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
        """select * from t_author where name = %s""",
        item['name'])
      # 是否有重复数据
      repetition = self.cursor.fetchone()

      # 重复
      if repetition:
        logging.debug(item['name'],"记录已存在!")
        pass
      else:
        self.cursor.execute('insert into t_author(name,birthdate,bio) values (%s,%s,%s)',(
          item['name'],
          item['birthdate'],
          item['bio']
        ))

      self.connect.commit()
    except Exception as e:
      logging.error(e)
      self.connect.rollback()

    return item