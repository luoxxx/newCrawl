# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanDetailItem,Doubantop250Item
import time


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        message = response.xpath("//div[@class='info']")
        if message:
            item = Doubantop250Item()
            for msg in message:
                item["filmName"]=msg.xpath("./div/a/span[1]/text()").get()
                item["actors"]=msg.xpath("./div/p/text()").get().strip()
                item["mark"] = msg.xpath("./div/div/span[2]/text()").get()
                item["detailUrl"] = msg.xpath("./div/a/@href").get()
                time.sleep(2)
                yield item
                time.sleep(3)
                yield scrapy.Request(item["detailUrl"],callback=self.parse_detail,dont_filter=True)
                time.sleep(2)
        else:
            return

    def parse_detail(self, response):
        item = DoubanDetailItem()
        # response.xpath('//section[@class="subject-intro"]/h2/text()').get().strip()
        item["filmName"] = response.xpath('//div[@class="sub-title"]/text()').get()
        item["detail"] = response.xpath('//section[@class="subject-intro"]/div/p/text()').get().strip()
        time.sleep(1)
        yield item
        time.sleep(1)
        pass

