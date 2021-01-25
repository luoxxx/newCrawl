# -*- coding: utf-8 -*-
import scrapy
from lxml import etree

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        res = etree.HTML(response.body)
        print(res.xpath("/html/head/title/text()"))
        pass
