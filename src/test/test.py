# -*- coding: utf-8 -*-

import os,pymongo

def test1():
  __all__ = []
  for f in os.listdir(os.getcwd()):
    matchObj = re.match( r'(\w+).py$', f, re.M|re.I)
    if matchObj and f != '__init__.py':
      __all__.append(re.sub(r'\.py','',f))
  
  print(__all__)

def test2():
  MONGO_HOST='127.0.0.1'
  MONGO_PORT=27017
  MONGO_DB='scrapy'
  MONGO_USERNAME='dev'
  MONGO_PASSWORD='dev12345'

  client = pymongo.MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    authSource=MONGO_DB,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authMechanism='SCRAM-SHA-256',
    serverSelectionTimeoutMS=3000
  )
  db = client[MONGO_DB]
  res = db['jd_product'].find_one()
  print(res)

#主程序入口
if __name__ == '__main__':
  # test1()
  test2()