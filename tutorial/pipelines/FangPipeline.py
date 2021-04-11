# -*- coding: utf-8 -*-

from scrapy.exporters import JsonLinesItemExporter

"""
将结果写入json文件
"""
class FangPipeline(object):
  def __init__(self):
    self.file_fp = open('out/fang.json', 'wb')
    self.file_exporter = JsonLinesItemExporter(self.file_fp, ensure_ascii=False)

  def process_item(self, item, spider):
    self.file_exporter.export_item(item)
    return item
  
  def close_spider(self, spider):
    self.file.close()


class SfwPipeline(object):
  def __init__(self):
    self.newhouse_fp = open('out/newhouse.json', 'wb')
    self.esfhouse_fp = open('out/esfhouse.json', 'wb')
    self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp, ensure_ascii=False)
    self.esfhouse_exporter = JsonLinesItemExporter(self.esfhouse_fp, ensure_ascii=False)

  def process_item(self, item, spider):
    self.newhouse_exporter.export_item(item)
    self.esfhouse_exporter.export_item(item)
    return item

  def close_spider(self, spider):
    self.newhouse_fp.close()
    self.esfhouse_fp.close()
