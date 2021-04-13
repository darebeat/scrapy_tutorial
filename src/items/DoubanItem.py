# -*- coding: utf-8 -*-

from scrapy import Item,Field

class DoubanItem(Item):
  item_id = Field() # ID
  item_name = Field() # 小项名称
  url = Field() # URL  # 小项的链接
  info = Field() # 小项的详细信息
  rating = Field() # 小项的评分信息
  comment = Field() # 评论次数

# 音乐
class MusicItem(Item):
  music_name = Field()
  music_alias = Field()
  music_singer = Field()
  music_time = Field()
  music_rating = Field()
  music_votes = Field()
  music_tags = Field()
  music_url = Field()

# 乐评
class MusicReviewItem(Item):
  review_title = Field()
  review_content = Field()
  review_author = Field()
  review_music = Field()
  review_time = Field()
  review_url = Field()

# 电影
class VideoItem(Item):
  video_name = Field()
  video_alias = Field()
  video_actor = Field()
  video_year = Field()
  video_time = Field()
  video_rating = Field()
  video_votes = Field()
  video_tags = Field()
  video_url = Field()
  video_director = Field()
  video_type = Field()
  video_bigtype = Field()
  video_area = Field()
  video_language = Field()
  video_length = Field()
  video_writer = Field()
  video_desc = Field()
  video_episodes = Field()

# 影评
class VideoReviewItem(Item):
  review_title = Field()
  review_content = Field()
  review_author = Field()
  review_video = Field()
  review_time = Field()
  review_url = Field()

    
class BookItem(Item):
    # define the fields for your item here like:
    id = Field()       #ID号
    title = Field()    #书名
    author = Field()   #作者
    press = Field()    #出版社
    original = Field() #原作名
    translator = Field()#译者
    imprint = Field()  #出版年
    pages = Field()    #页数
    price = Field()    #定价
    binding = Field()  #装帧
    series = Field()   #丛书
    isbn = Field()     #ISBN
    score = Field()    #评分
    number = Field()   #评论人数