import json

"""
将结果写入json文件
"""
class FangPipeline(object):
  def __init__(self):
    self.file = open('out/fang.json', '+wb')

  def process_item(self, item, spider):
    line = json.dumps(dict(item)) + "\n"
    print(line)
    self.file.write(str.encode(line))
    return item