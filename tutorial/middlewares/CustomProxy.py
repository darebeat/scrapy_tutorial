# -*- coding: utf-8 -*-

from tutorial.middlewares.Resource import PROXIES
import random

class RandomProxy(object):
  def process_request(self,request, spider):
    proxy = random.choice(PROXIES)
    request.meta['proxy'] = 'http://%s'% proxy