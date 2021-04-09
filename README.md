# README

## 创建项目

```sh
# 这将在该project_dir目录下创建一个Scrapy项目。
# 如果project_dir没有指定，project_dir将会和myproject名称一样。
scrapy startproject myproject [ project_dir ]
```

## 控制项目

```sh
cd project_dir
# 创建一个新的爬虫
scrapy genspider mydomain mydomain.com
```

## Scrapy shell

学习如何使用Scrapy提取数据的最好方法是尝试使用shell Scrapy shell的选择器。

```sh
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