# -*- coding: utf-8 -*-

from tutorial.middlewares.Resource import USER_AGENT_LIST
import random

class RandomUserAgent(object):
  def process_request(self, request, spider):
    ua = random.choice(USER_AGENT_LIST)
    print(ua)
    request.headers.setdefault('User-Agent', ua)
