from .. import mysql as mc
from .. import redis as rc

author={
  'ITEM_PIPELINES': { 'src.pipelines.AuthorPipeline.AuthorPipeline': 300 },
  # mysql config
  'MYSQL_HOST': mc.MYSQL_HOST,
  'MYSQL_PORT': mc.MYSQL_PORT,
  'MYSQL_DBNAME': mc.MYSQL_DBNAME,
  'MYSQL_USER': mc.MYSQL_USER,
  'MYSQL_PASSWD': mc.MYSQL_PASSWD,
}
mbook={
  'ITEM_PIPELINES':{
    'src.pipelines.DbookPipeline.DbookMasterPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  },
  # scrapy_redis config
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
    'src.pipelines.DbookPipeline.DbookSlavePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  },
  # scrapy_redis config
  'DUPEFILTER_CLASS': rc.DUPEFILTER_CLASS,
  'SCHEDULER': rc.SCHEDULER,
  'SCHEDULER_PERSIST': rc.SCHEDULER_PERSIST,
  'SCHEDULER_QUEUE_CLASS': rc.SCHEDULER_QUEUE_CLASS,
  'REDIS_HOST': rc.REDIS_HOST,
  'REDIS_PORT': rc.REDIS_PORT,
  'REDIS_PARAMS': rc.REDIS_PARAMS,
}
sfw={
  'ITEM_PIPELINES':{
    'src.pipelines.FangPipeline.SfwPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  },
  # scrapy_redis config
  'DUPEFILTER_CLASS': rc.DUPEFILTER_CLASS,
  'SCHEDULER': rc.SCHEDULER,
  'SCHEDULER_PERSIST': rc.SCHEDULER_PERSIST,
  'SCHEDULER_QUEUE_CLASS': rc.SCHEDULER_QUEUE_CLASS,
  'REDIS_HOST': rc.REDIS_HOST,
  'REDIS_PORT': rc.REDIS_PORT,
  'REDIS_PARAMS': rc.REDIS_PARAMS,
}
fang={
  'ITEM_PIPELINES':{ 'src.pipelines.FangPipeline.FangPipeline': 300 },
  # csv export config
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
img={
  'ITEM_PIPELINES':{ 'src.pipelines.ImagePipeline.ImagePipeline': 300 },
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
    'src.pipelines.KuaidailiPipeline.KuaidailiRedisPipeline': 300,
    'src.pipelines.KuaidailiPipeline.KuaidailiPipeline': 301,
    'scrapy_redis.pipelines.RedisPipeline': 400,
  }
}

jd={ 'ITEM_PIPELINES':{ 
  'src.pipelines.JDPipeline.JDPipeline': 300 },
  'KEYWORDS':['iPad'],
  'MAX_PAGE':2,
}
taobao={ 
  'ITEM_PIPELINES':{ 'src.pipelines.TaobaoPipeline.TaobaoPipeline': 300},
  'KEYWORDS':['iPad'],
  'MAX_PAGE':2,
}
hr={ 'ITEM_PIPELINES':{ 'src.pipelines.HrPipeline.HrPipeline': 300 } }
douban={ 'ITEM_PIPELINES':{ 'src.pipelines.DoubanPipeline.DoubanPipeline': 300 } }
video={ 'ITEM_PIPELINES':{ 'src.pipelines.DoubanPipeline.DoubanPipeline': 300 } }
course={ 'ITEM_PIPELINES':{ 'src.pipelines.CoursePipeline.CoursePipeline': 300 } }
music={ 'ITEM_PIPELINES':{ 'src.pipelines.DoubanPipeline.DoubanPipeline': 300 } }
mz={ 'ITEM_PIPELINES': { 'src.pipelines.MeizhuoPipeline.MeizhuoPipeline': 300 } }
qd={ 'ITEM_PIPELINES':{ 'src.pipelines.QdPipeline.QdPipeline': 300 } }
wx={ 'ITEM_PIPELINES':{ 'src.pipelines.WxPipeline.WxPipeline': 300 } }
