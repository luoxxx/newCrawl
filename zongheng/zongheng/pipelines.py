# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class ZonghengPipeline(object):
    def process_item(self, item, spider):
        book_name = item["book_name"]
        chapter_name = item["chapter_name"]
        content = item["content"]
        if not os.path.exists(book_name) :
            os.mkdir(book_name)
        with open(book_name+"/"+chapter_name+".txt", "w", encoding="utf-8") as f:
            f.write(content)
        return item
