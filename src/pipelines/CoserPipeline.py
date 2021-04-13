# -*- coding: utf-8 -*-

import requests,os
from ..configs.spider.settings import IMAGES_STORE
 
class CoserPipeline(object):
  def process_item(self, item, spider):
    return item