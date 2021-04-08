# -*- coding: utf-8 -*-

import random

'''
这个类主要用于产生随机UserAgent
'''
#创建一个随机请求头
class RandomUserAgent(object):
    #实例化一个USER_AGENTS
    def __init__(self,agents):
        self.agents = agents
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    #添加随机请求头
    def process_request(self,request,spider):
        request.headers['User-Agent'] = random.choice(self.agents)