# -*- coding: utf-8 -*-

import pymysql,logging
from .. import settings
from ..items.DoubanItem import DoubanItem,MusicItem,MusicReviewItem,VideoItem,VideoReviewItem
logger = logging.getLogger(__name__)

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
    if item.__class__ == DoubanItem:
      try:
        # 查重处理
        self.cursor.execute(
          """select id from t_douban where item_id = %s""",
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
            insert into t_douban(
              item_id,
              item_name,
              url,
              info,
              rating,
              comment
            ) value (%s,%s,%s,%s,%s,%s)
            """,(
              item['item_id'],
              item['item_name'],
              item['url'],
              item['info'],
              item['rating'],
              item['comment']
            ))

        # 提交sql语句
        self.connect.commit()
      except Exception as e:
        # 出现错误时打印错误日志
        logger.error(e)
      return item
    elif item.__class__ == MusicItem:
      try:
        self.cursor.execute("""select id from t_douban_music where music_url = %s""", item["music_url"])
        ret = self.cursor.fetchone()
        if ret:
          self.cursor.execute(
            """
            update t_douban_music set 
              music_name = %s,
              music_alias = %s,
              music_singer = %s,
              music_time = %s,
              music_rating = %s,
              music_votes = %s,
              music_tags = %s,
              music_url = %s
            where music_url = %s
            """,(
              item['music_name'],
              item['music_alias'],
              item['music_singer'],
              item['music_time'],
              item['music_rating'],
              item['music_votes'],
              item['music_tags'],
              item['music_url'],
              item['music_url']
            ))
        else:
          self.cursor.execute(
            """
            insert into t_douban_music(
              music_name,
              music_alias,
              music_singer,
              music_time,
              music_rating,
              music_votes,
              music_tags,
              music_url
            ) value (%s,%s,%s,%s,%s,%s,%s,%s)
            """,(
              item['music_name'],
              item['music_alias'],
              item['music_singer'],
              item['music_time'],
              item['music_rating'],
              item['music_votes'],
              item['music_tags'],
              item['music_url']
            ))
        self.connect.commit()
      except Exception as e:
        logger.error(e)
      return item
    elif item.__class__ == MusicReviewItem:
      try:
        self.cursor.execute("""select id from t_douban_music_review where review_url = %s""", item["review_url"])
        ret = self.cursor.fetchone()
        if ret:
          self.cursor.execute(
            """
            update t_douban_music_review set 
              review_title = %s,
              review_content = %s,
              review_author = %s,
              review_music = %s,
              review_time = %s,
              review_url = %s
            where review_url = %s
            """,(
              item['review_title'],
              item['review_content'],
              item['review_author'],
              item['review_music'],
              item['review_time'],
              item['review_url'],
              item['review_url']
            ))
        else:
          self.cursor.execute(
            """
            insert into t_douban_music_review(
              review_title,
              review_content,
              review_author,
              review_music,
              review_time,
              review_url)
            value (%s,%s,%s,%s,%s,%s)
            """,(
              item['review_title'],
              item['review_content'],
              item['review_author'],
              item['review_music'],
              item['review_time'],
              item['review_url']
            ))
        self.connect.commit()
      except Exception as e:
        logger.error(e)
      return item
    elif item.__class__ == VideoItem:
      try:
        self.cursor.execute("""select id from t_douban_video where video_url = %s""", item["video_url"])
        ret = self.cursor.fetchone()
        if ret:
          self.cursor.execute(
            """
            update t_douban_video set 
              video_name= %s,
              video_alias= %s,
              video_actor= %s,
              video_year= %s,
              video_time= %s,
              video_rating= %s,
              video_votes= %s,
              video_tags= %s,
              video_url= %s,
              video_director= %s,
              video_type= %s,
              video_bigtype= %s,
              video_area= %s,
              video_language= %s,
              video_length= %s,
              video_writer= %s,
              video_desc= %s,
              video_episodes= %s 
            where video_url = %s
            """,(
              item['video_name'],
              item['video_alias'],
              item['video_actor'],
              item['video_year'],
              item['video_time'],
              item['video_rating'],
              item['video_votes'],
              item['video_tags'],
              item['video_url'],
              item['video_director'],
              item['video_type'],
              item['video_bigtype'],
              item['video_area'],
              item['video_language'],
              item['video_length'],
              item['video_writer'],
              item['video_desc'],
              item['video_episodes'],
              item['video_url']
            ))
        else:
          self.cursor.execute(
            """
            insert into t_douban_video(
              video_name,
              video_alias,
              video_actor,
              video_year,
              video_time,
              video_rating,
              video_votes,
              video_tags,
              video_url,
              video_director,
              video_type,
              video_bigtype,
              video_area,
              video_language,
              video_length,
              video_writer,
              video_desc,
              video_episodes
            ) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(
              item['video_name'],
              item['video_alias'],
              item['video_actor'],
              item['video_year'],
              item['video_time'],
              item['video_rating'],
              item['video_votes'],
              item['video_tags'],
              item['video_url'],
              item['video_director'],
              item['video_type'],
              item['video_bigtype'],
              item['video_area'],
              item['video_language'],
              item['video_length'],
              item['video_writer'],
              item['video_desc'],
              item['video_episodes']
            ))
        self.connect.commit()
      except Exception as e:
        logger.error(e)
      return item
    elif item.__class__ == VideoReviewItem:
      try:
        self.cursor.execute("""select id from t_douban_video_review where review_url = %s""", item["review_url"])
        ret = self.cursor.fetchone()
        if ret:
          self.cursor.execute(
            """
            update t_douban_video_review set 
            review_title = %s,
            review_content = %s,
            review_author = %s,
            review_video = %s,
            review_time = %s,
            review_url = %s
            where review_url = %s
            """,(
              item['review_title'],
              item['review_content'],
              item['review_author'],
              item['review_video'],
              item['review_time'],
              item['review_url'],
              item['review_url']
            ))
        else:
          self.cursor.execute(
            """
            insert into t_douban_video_review(
              review_title,
              review_content,
              review_author,
              review_video,
              review_time,
              review_url
            ) value (%s,%s,%s,%s,%s,%s)
            """,(
              item['review_title'],
              item['review_content'],
              item['review_author'],
              item['review_video'],
              item['review_time'],
              item['review_url']
            ))
        self.connect.commit()
      except Exception as e:
        logger.error(e)
      return item