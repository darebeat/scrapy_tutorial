# -*- coding: utf-8 -*-
 
# 文件处理类库，可以指定编码格式
import codecs
import json
 
class SunPipeline(object):
 
  def __init__(self):
    # 创建一个只写文件，指定文本编码格式为utf-8
    self.filename = codecs.open('out/sunwz.json', 'w', encoding='utf-8')
 
  def process_item(self, item, spider):
    content = json.dumps(dict(item), ensure_ascii=False) + "\n"
    self.filename.write(content)
    return item
 
  def spider_closed(self, spider):
    self.file.close()