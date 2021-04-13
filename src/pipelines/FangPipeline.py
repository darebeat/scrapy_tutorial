# -*- coding: utf-8 -*-

from scrapy.exporters import JsonLinesItemExporter,CsvItemExporter
from ..configs.spider.settings import fang

"""
将结果写入json文件
"""
class FangPipeline(object):
  def __init__(self):
    self.json_fp = open('out/fang.json','wb')
    self.json_exporter = JsonLinesItemExporter(
      self.json_fp,
      fields_to_export=fang.get('FIELDS_TO_EXPORT',[]), # 指定字段顺序
      encoding=fang.get('FEED_EXPORT_ENCODING','utf-8'),
      ensure_ascii=False
    )
    self.json_exporter.start_exporting()

  def open_spider(self, spider):
    self.csv_fp = open('out/fang.csv','w+b')
    self.csv_exporter = CsvItemExporter(
      self.csv_fp,
      include_headers_line=True,
      join_multivalued=fang.get('CSV_DELIMITER',','),
      fields_to_export=fang.get('FIELDS_TO_EXPORT',[]),
      encoding=fang.get('FEED_EXPORT_ENCODING','utf-8')
    )
    self.csv_exporter.start_exporting()

  def process_item(self, item, spider):
    self.json_exporter.export_item(item)
    self.csv_exporter.export_item(item)
    return item

  def close_spider(self, spider):
    self.json_exporter.finish_exporting()
    self.csv_exporter.finish_exporting()
    self.json_fp.close()
    self.csv_fp.close()

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
