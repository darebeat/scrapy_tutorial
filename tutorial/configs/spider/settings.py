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
  },
  'CSV_DELIMITER': ',',
  'FEED_EXPORT_ENCODING': 'utf-8',
  'FIELDS_TO_EXPORT':[
    'address',
    'title',
    'time',
    'clicks',
    'price'
  ]
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
  'IMAGES_STORE':'images',
  # 30天后过期
  'IMAGES_EXPIRES':30,
  # Images Pipline可以自动创建下载图像的缩略图，在setting中增加IMAGES_THUMBS参数,参数为一个字典，其中的键是缩略图名称，而值是它们的维数：
  'IMAGES_THUMBS':{ 'small': (50, 50), 'big': (270, 270)},
  # 如果想过滤掉小图片，通过设置IMAGES_MIN_HEIGHT和 IMAGES_MIN_WIDTH来指定图像大小：
  'IMAGES_MIN_HEIGHT':110,
  'IMAGES_MIN_WIDTH':110,
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
