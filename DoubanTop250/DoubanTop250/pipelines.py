# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from .items import Doubantop250Item,DoubanDetailItem
import pymysql

class DoubanDetailPipeline(object):
    def open_spider(self,spider):
        self.f = open("detail.txt","w+",encoding="utf-8")


    def process_item(self, item, spider):
        if isinstance(item, DoubanDetailItem):
            data = json.dumps(dict(item),ensure_ascii=False)+"\n"
            self.f.write(data)
        return item


    def close_spider(self,spider):
        self.f.close()

class Doubantop250Pipeline(object):
    def open_spider(self,spider):
        db = {
            'host':"localhost",
            "port":3306,

            "db":"stu",
            "charset":"utf8"
        }
        self.conn = pymysql.connect(**db)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, Doubantop250Item):
            data = dict(item)
            sql = "insert into movies(filmname,actor,mark,detailurl) value('{}','{}','{}','{}')".format(data['filmName'], data['actors'], data['mark'], data['detailUrl'])
            self.cur.execute(sql)
            self.conn.commit()
        return item


    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()
        pass