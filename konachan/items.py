# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KonachanItem(scrapy.Item):
    # define the fields for your item here like:
    #由于我们使用的是scrapy 自带的图片下载通道，所以url 和图片名称必须按照配置文件设置
    # 即 Item里面 url 信息设置为 image_urls, 图片名称信息 设置为images
     image_urls = scrapy.Field()
     images=scrapy.Field()
     detailed=scrapy.Field()

