# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImgspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片二进制
    imgurl = scrapy.Field()
    imgdirname = scrapy.Field()
    imgname = scrapy.Field()

class ImgItem(scrapy.Item):
    imgbin = scrapy.Field()
