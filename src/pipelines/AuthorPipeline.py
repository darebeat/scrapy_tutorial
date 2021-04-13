# -*- coding: utf-8 -*-

import pymysql,logging
from ..configs import mysql as author

class AuthorPipeline:
  def __init__(self):
    # 连接数据库
    self.connect = pymysql.connect(
      host=author.MYSQL_HOST,
      port=author.MYSQL_PORT,
      database=author.MYSQL_DBNAME,
      user=author.MYSQL_USER,
      password=author.MYSQL_PASSWD,
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