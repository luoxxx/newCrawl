# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import re
from..items import ZonghengItem


class NovelSpider(CrawlSpider):
    name = 'novel'
    # allowed_domains = ['http://www.zongheng.com/']
    start_urls = ['http://book.zongheng.com/book/189169.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://book.zongheng.com/showchapter/189169.html'), callback='parse_item',follow=True),

        Rule(LinkExtractor(allow=r'http://book.zongheng.com/chapter/\d+/\d+.html'), callback='get_content',
             process_links="processLinks", follow=False)
    )
    # 过滤links
    def processLinks(self,links):
        for link in links:
            num = int(re.findall(r"(\d+)\.html", link.url)[0])
            if num<3500000:
                yield link

    def parse_item(self, response):
        item = ZonghengItem()
        # item["book_name"] = response.xpath('//div[@class="container"]/div/h1/text()').get()
        # print("-----------------------------------parse")
        # content = response.xpath('//li[@class=" col-4"]/a/text()').getall()
        # print(content)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
    def get_content(self, response):
        item = ZonghengItem()
        item["book_name"]="雪中悍刀行"
        item["chapter_name"]=response.xpath('//div[@class="title_txtbox"]/text()').get()
        content=response.xpath('//div[@class="content"]/p/text()').getall()
        item["content"]="\n".join(content)
        yield item
        time.sleep(2)
        pass



    # def parse_start_url(self, response):
    #     print("主页",response.text)
    #     return []

    # 非章节：
    # 'http://book.zongheng.com/chapter/189169/3441845.html'
    # "http://book.zongheng.com/chapter/189169/5743839.html"
    # "http://book.zongheng.com/chapter/189169/3602933.html"
    # "http://book.zongheng.com/chapter/189169/34894298.html"
    # "http://book.zongheng.com/chapter/189169/3574899.html"


    # 章节：
    # "http://book.zongheng.com/chapter/189169/3431546.html"
    # "http://book.zongheng.com/chapter/189169/3431692.html"
    # "http://book.zongheng.com/chapter/189169/4531354.html"
    # "http://book.zongheng.com/chapter/189169/3431696.html"
    # http: // book.zongheng.com / chapter / 189169 / 3434307.html"