# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
from scrapy.crawler import CrawlerProcess

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from src.spiders.QdSpider import QdSpider
from src.spiders.FangSpider import FangSpider

tasks = {
    "author":"scrapy crawl author",
    "course":"scrapy crawl course",
    "douban":"scrapy crawl douban",
    "fang":"scrapy crawl fang",
    "hr":"scrapy crawl hr",
    "imdb":"scrapy crawl imdb",
    "img":"scrapy crawl img",
    "jd":"scrapy crawl jd",
    "kdl":"scrapy crawl kdl",
    "mbook":"scrapy crawl mbook",
    "music":"scrapy crawl music",
    "myspider1":"scrapy crawl myspider1",
    "myspider2":"scrapy crawl myspider2",
    "mz":"scrapy crawl mz",
    "q1":"scrapy crawl q1",
    "q2":"scrapy crawl q2",
    "q3":"scrapy crawl q3",
    "q4":"scrapy crawl q4",
    "qd":"scrapy crawl qd",
    "qsbk":"scrapy crawl qsbk",
    "renren":"scrapy crawl renren",
    "sbook":"scrapy crawl sbook",
    "sf":"scrapy crawl sf",
    "sfw":"scrapy crawl sfw",
    "taobao":"scrapy crawl taobao",
    "video":"scrapy crawl video",
    "wenku":"scrapy crawl wenku",
    "wx":"scrapy crawl wx",
    "youdao":"scrapy crawl youdao",
  }

def cmd1():
  # execute 运行单个(推荐)爬虫
  execute(tasks['jd'].split())

def cmd2():
  # CrawlerProcess 运行多个爬虫
  process = CrawlerProcess()
  process.crawl(QdSpider)
  process.crawl(FangSpider)
  process.start()

def cmd3():
  # CrawlerRunner 运行多个爬虫
  configure_logging()
  runner = CrawlerRunner({ 'LOG_FORMAT': '%(message)s' })
  runner.crawl(QdSpider)
  runner.crawl(FangSpider)
  d = runner.join()
  d.addBoth(lambda _: reactor.stop())

  reactor.run()

if __name__ == '__main__':
  cmd1()