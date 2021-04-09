import pymysql
from scrapy.exceptions import DropItem

class EducsdnPipeline(object):
  def process_item(self, item, spider):
    if item['price'] == None:
      raise DropItem("Drop item found: %s" % item)
    else:
      return item

class CoursePipeline(object):
  def __init__(self,host,database,user,password,port):
    self.host = host
    self.database = database
    self.user = user
    self.password = password
    self.port = port
    self.db=None
    self.cursor=None

  @classmethod
  def from_crawler(cls,crawler):
    return cls(
      host = crawler.settings.get("MYSQL_HOST"),
      database = crawler.settings.get("MYSQL_DBNAME"),
      user = crawler.settings.get("MYSQL_USER"),
      password = crawler.settings.get("MYSQL_PASSWD"),
      port = crawler.settings.get("MYSQL_PORT")
    )

  def open_spider(self,spider):
    self.db = pymysql.connect(
      host=self.host,
      port=self.port,
      database=self.database,
      user=self.user,
      password=self.password,
      charset='utf8mb4',
      use_unicode=True)
    self.cursor = self.db.cursor()

  def process_item(self, item, spider):
    sql = "insert into t_courses(title,url,pic,teacher,time,price) values('%s','%s','%s','%s','%s','%s')"%(item['title'],item['url'],item['pic'],item['teacher'],str(item['time']),str(item['price']))
    #print(item)
    self.cursor.execute(sql)
    self.db.commit()
    return item

  def close_spider(self,spider):
    self.db.close()