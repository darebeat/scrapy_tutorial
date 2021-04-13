# -*- coding: utf-8 -*-

import pymongo
from ..configs import mongo as mgc

class JDPipeline(object):
  ''' 完成MongoDB数据库对Item信息的存储'''
  def __init__(self,host,port,db,username,password):
    '''对象初始化'''
    self.host = host
    self.port = port
    self.db = db
    self.username = username
    self.password = password

  @classmethod
  def from_crawler(cls, crawler):
    '''通过依赖注入方式实例化当前类，并返回，参数是从配置文件获取MongoDB信息'''
    return cls(
      host=mgc.MONGO_HOST,
      port=mgc.MONGO_PORT,
      db=mgc.MONGO_DB,
      username=mgc.MONGO_USERNAME,
      password=mgc.MONGO_PASSWORD
    )

  def open_spider(self, spider):
    '''Spider开启自动调用此方法，负责连接MongoDB，并选择数据库'''
    self.client = pymongo.MongoClient(
      host=self.host,
      port=self.port,
      authSource=self.db,
      username=self.username,
      password=self.password,
      serverSelectionTimeoutMS=3000
    )
    self.db = self.client[self.db]

  def process_item(self,item, spider):
    self.db[item.collection].insert(dict(item))
    return item

  def close_spider(self,spider):
    self.client.close()