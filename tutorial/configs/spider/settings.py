from .. import mysql as mc
from .. import redis as rc

author={
  'ITEM_PIPELINES': { 'tutorial.pipelines.AuthorPipeline.AuthorPipeline': 300 },
  'MYSQL_HOST': mc.MYSQL_HOST,
  'MYSQL_PORT': mc.MYSQL_PORT,
  'MYSQL_DBNAME': mc.MYSQL_DBNAME,
  'MYSQL_USER': mc.MYSQL_USER,
  'MYSQL_PASSWD': mc.MYSQL_PASSWD,
}
course={
  'ITEM_PIPELINES':{ 'tutorial.pipelines.CoursePipeline.CoursePipeline': 300 } 
}
music={
  'ITEM_PIPELINES':{ 'tutorial.pipelines.DoubanPipeline.DoubanPipeline': 300 }
}
mbook={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.DbookPipeline.DbookMasterPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  },
  'DUPEFILTER_CLASS': rc.DUPEFILTER_CLASS,
  'SCHEDULER': rc.SCHEDULER,
  'SCHEDULER_PERSIST': rc.SCHEDULER_PERSIST,
  'SCHEDULER_QUEUE_CLASS': rc.SCHEDULER_QUEUE_CLASS,
  'REDIS_HOST': rc.REDIS_HOST,
  'REDIS_PORT': rc.REDIS_PORT,
  'REDIS_PARAMS': rc.REDIS_PARAMS,
}
sbook={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.DbookPipeline.DbookSlavePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  },
  'DUPEFILTER_CLASS': rc.DUPEFILTER_CLASS,
  'SCHEDULER': rc.SCHEDULER,
  'SCHEDULER_PERSIST': rc.SCHEDULER_PERSIST,
  'SCHEDULER_QUEUE_CLASS': rc.SCHEDULER_QUEUE_CLASS,
  'REDIS_HOST': rc.REDIS_HOST,
  'REDIS_PORT': rc.REDIS_PORT,
  'REDIS_PARAMS': rc.REDIS_PARAMS,
}
douban={
  'ITEM_PIPELINES':{ 'tutorial.pipelines.DoubanPipeline.DoubanPipeline': 300 }
}
video={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.DoubanPipeline.DoubanPipeline': 300
  }
}
fang={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.FangPipeline.FangPipeline': 300
  }
}
sfw={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.FangPipeline.SfwPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  },
  'DUPEFILTER_CLASS': rc.DUPEFILTER_CLASS,
  'SCHEDULER': rc.SCHEDULER,
  'SCHEDULER_PERSIST': rc.SCHEDULER_PERSIST,
  'SCHEDULER_QUEUE_CLASS': rc.SCHEDULER_QUEUE_CLASS,
  'REDIS_HOST': rc.REDIS_HOST,
  'REDIS_PORT': rc.REDIS_PORT,
  'REDIS_PARAMS': rc.REDIS_PARAMS,
}
hr={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.HrPipeline.HrPipeline': 300
  }
}
jd={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.JDPipeline.JDPipeline': 300
  }
}
img={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.ImagePipeline.ImagePipeline': 300
  },
  'IMAGES_STORE': 'images'
}
kdl={
  'ITEM_PIPELINES': {
    'tutorial.pipelines.KuaidailiPipeline.KuaidailiRedisPipeline': 300,
    'tutorial.pipelines.KuaidailiPipeline.KuaidailiPipeline': 301,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  }
}
mz={
  'ITEM_PIPELINES': {
    'tutorial.pipelines.MeizhuoPipeline.MeizhuoPipeline': 300
  }
}
qd={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.QdPipeline.QdPipeline': 300
  }
}
taobao={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.TaobaoPipeline.TaobaoPipeline': 300
  }
}
wx={
  'ITEM_PIPELINES':{
    'tutorial.pipelines.WxPipeline.WxPipeline': 300
  }
}
