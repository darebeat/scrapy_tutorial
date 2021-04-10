# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# from datetime import datetime
# to_day = datetime.now()

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# 日志设置
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = "DEBUG" # DEBUG | INFO | WARNING | ERROR | CRITICAL
# LOG_FILE = "out/tutorial_{}_{}_{}.log".format(to_day.year,to_day.month,to_day.day)
# LOG_STDOUT = False

# 定义请求头
# USER_AGENTS = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # ept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
  'tutorial.middlewares.CustomUserAgent.RandomUserAgent': 100,
  # 'tutorial.middlewares.CustomProxy.RandomProxy': 101,
  # 'tutorial.middlewares.SeleniumJd.SeleniumJd': 543,
  # 'tutorial.middlewares.SeleniumTaobao.SeleniumTaobao': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
  # 'tutorial.pipelines.AuthorPipeline': 300,
  # 'tutorial.pipelines.DoubanPipeline': 300,
  # 'tutorial.pipelines.JDPipeline': 300,
  # 'tutorial.pipelines.QdPipeline': 300,
  # 'tutorial.pipelines.TaobaoPipeline': 300,
  # 'tutorial.pipelines.FangPipeline': 300,
  # 'tutorial.pipelines.CoursePipeline': 300,
  # 'tutorial.pipelines.HrPipeline': 300,
  # 'tutorial.pipelines.WxPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# ------------------------ mysql config
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'test'
MYSQL_USER = 'test'
MYSQL_PASSWD = 'd73XzyUo%iz(ix'
MYSQL_PORT = 3310

# ------------------------ 
# mongodb config
MONGO_URL = 'localhost'
MONGO_DB = 'test'
COLLECTION = 'ProductItem'

# ------------------------ 
# other custom config
KEYWORDS = ['iPad']
MAX_PAGE = 2
SELENIUM_TIMEOUT = 20
PHANTOMJS_SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# IMAGES_STORE = 'images'
