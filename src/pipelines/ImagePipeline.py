from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):
  '''自定义图片存储类'''

  def get_media_requests(self, item, info):
    '''
    通过抓取的item对象获取图片信息，并创建Request请求对象添加调度队列，等待调度执行下载
    循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
    '''
    for image_url in item['imgurl']:
      yield Request(image_url)

  def file_path(self,request,response=None,info=None):
    '''返回图片下载后保存的名称，没有此方法Scrapy则自动给一个唯一值作为图片名称'''
    url = request.url
    file_name = url.split("/")[-1]
    return file_name

  def item_completed(self, results, item, info):
    ''' 下载完成后的处理方法，其中results内容结构如下说明'''
    image_paths = [x['path'] for ok, x in results if ok]
    if not image_paths:
      raise DropItem("Item contains no images")
    #item['image_paths'] = image_paths
    return item