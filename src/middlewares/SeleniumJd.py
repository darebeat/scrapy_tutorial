# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from ..configs import selenium as jd

class SeleniumJd(object):
  # Not all methods need to be defined. If a method is not defined,
  # scrapy acts as if the downloader middleware does not modify the
  # passed objects.
 
  def __init__(self,timeout=None):
    self.logger=getLogger(__name__)
    self.timeout = timeout
    self.browser = webdriver.Chrome()
    self.browser.set_window_size(1400,700)
    self.browser.set_page_load_timeout(self.timeout)
    self.wait = WebDriverWait(self.browser,self.timeout)

  def __del__(self):
    self.browser.close()

  @classmethod
  def from_crawler(cls, crawler):
    # This method is used by Scrapy to create your spiders.
    return cls(timeout=jd.SELENIUM_TIMEOUT)

  def process_request(self, request, spider):
    '''
    在下载器中间件中对接使用selenium，输出源代码之后，构造htmlresponse对象，直接返回
    给spider解析页面，提取数据
    并且也不在执行下载器下载页面动作
    htmlresponse对象的文档：
    :param request:
    :param spider:
    :return:
    '''
 
    print('PhantomJS is Starting')
    page = request.meta.get('page', 1)
    self.wait = WebDriverWait(self.browser, self.timeout)
    # self.browser.set_page_load_timeout(30)
    # self.browser.set_script_timeout(30)
    try:
      self.browser.get(request.url)
      if page > 1:
        input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))
        input.clear()
        input.send_keys(page)
        time.sleep(5)
        # 将网页中输入跳转页的输入框赋值给input变量 EC.presence_of_element_located，判断输入框已经被加载出来
        input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))
        # 将网页中调准页面的确定按钮赋值给submit变量，EC.element_to_be_clickable 判断此按钮是可点击的
        submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
        input.clear()
        input.send_keys(page)
        submit.click()  # 点击按钮
        time.sleep(5)
        # 判断当前页码出现在了输入的页面中，EC.text_to_be_present_in_element 判断元素在指定字符串中出现
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'),str(page)))
        # 等待 #J_goodsList 加载出来，为页面数据，加载出来之后，在返回网页源代码
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'),str(page)))
      return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',status=200)
    except TimeoutException:
      return HtmlResponse(url=request.url, status=500, request=request)