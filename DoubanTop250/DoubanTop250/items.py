# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    filmName = scrapy.Field()
    actors = scrapy.Field()
    mark = scrapy.Field()
    detailUrl=scrapy.Field()
    pass

class DoubanDetailItem(scrapy.Item):
    filmName = scrapy.Field()
    detail = scrapy.Field()
