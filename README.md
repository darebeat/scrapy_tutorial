# scrapy

学习和使用scrapy,简单快速写出自己的爬虫程序.

## 常用命令备注

```sh
# 这将在该project_dir目录下创建一个Scrapy项目。
# 如果project_dir没有指定，project_dir将会和myproject名称一样。
scrapy startproject myproject [ project_dir ]
cd project_dir
# 创建一个新的爬虫
scrapy genspider mydomain mydomain.com
# 列出所有spider
scrapy list
# 运行spider
scrapy crawl fang
```

## Scrapy shell 调试代码

学习如何使用Scrapy提取数据的最好方法是尝试使用shell Scrapy shell的选择器。

```py
scrapy shell 'http://quotes.toscrape.com/page/1/'

# CSS选择元素
response.css('title')
response.css('title::text').extract()
response.css('title').extract()
response.css('title::text').extract_first()
response.css('title::text')[0].extract()
# re()方法使用正则表达式提取
response.css('title::text').re(r'Quotes.*')
response.css('title::text').re(r'Q\w+')
response.css('title::text').re(r'(\w+) to (\w+)')
# XPath选择元素
response.xpath('//title')
```

## tesseract

```sh
apt install tesseract-ocr
brew install tesseract

pip3 install pytesseract
pip3 install pillow
pip install PIL
```

## 目录结构说明

```
.
├── README.md
├── docker  # docker环境部署
├── main.py # 启动类
├── out     # 文件输出目录
├── requirements.txt # 依赖包
├── scrapy.cfg # 项目结构配置
├── sqls    # sql初始化文件
└── src # 源代码地址
    ├── __init__.py
    ├── configs # 自定义配置文件
    ├── items   # 自定义数据类
    ├── middlewares # 自定义中间件
    ├── pipelines # 自定义管道处理
    ├── spiders # 自定义爬虫类
    ├── test    # 测试用例
    ├── utils # 工具类
    └── settings.py # 项目通用配置
```