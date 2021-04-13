# -*- coding: utf-8 -*-

from scrapy.exporters import JsonLinesItemExporter,CsvItemExporter

class SinaPipeline(object):
  def __init__(self):
    self.json_fp = open('out/sina.json','wb')
    self.json_exporter = JsonLinesItemExporter(
      self.json_fp,
      ensure_ascii=False
    )
    self.json_exporter.start_exporting()

  def open_spider(self, spider):
    self.csv_fp = open('out/sina.csv','wb')
    self.csv_exporter = CsvItemExporter(
      self.csv_fp,
      include_headers_line=True,
      encoding='utf-8'
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