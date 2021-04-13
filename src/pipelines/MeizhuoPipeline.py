# -*- coding: utf-8 -*-

import os,requests,random
from ..settings import IMAGES_STORE
from ..middlewares.Resource import USER_AGENT_LIST

headers = { 'user-agent': random.choice(USER_AGENT_LIST) }

class MeizhuoPipeline(object):
  def process_item(self, item, spider):
    dir_path = IMAGES_STORE
    title = item['title']
    img_list = item['url']
    print(title, img_list)
    """
    1、我要创建指定的路径
    2、然后我要利用requests模块获取到那一个url的二进制数据保存进去
    """
    if not os.path.exists(IMAGES_STORE):
      os.mkdir(IMAGES_STORE)

    # 如果这个顶头文件夹存在的话
    collection_url = os.path.join(IMAGES_STORE, title)
    print('111', collection_url)
    if not os.path.exists(collection_url):
      os.mkdir(collection_url)
    for url_list in range(len(img_list)):
      cmp_url = os.path.join(collection_url, img_list[url_list])

      # print(cmp_url)
      file_path = os.path.join(collection_url, title) + str(url_list) + '.jpg'
      print(file_path)
      with open(file_path, 'wb') as fp:
        res = requests.get(img_list[url_list], headers=headers).content
        # print(img_list[url_list])
        fp.write(res)
        print('insert successfully!!!')
    # 如果这个文件夹存在的话
    return item
