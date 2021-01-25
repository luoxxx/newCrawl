# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from .items import ImgItem

class ImgspiderPipeline(object):
    # def open_spider(self,spider):
    #     self.f = open("img/")
    #     pass
    num = 0
    def process_item(self, item, spider):
        if isinstance(item,ImgItem):
        # file = "img/"+item["imgname"]+'.jpg'
            self.num += 1
            file = "img/"+str(self.num)+".jpg"
            with open(file,"wb+") as f:
                f.write(item["imgbin"])
            return item

    # def close_spider(self,spider):
    #     pass
