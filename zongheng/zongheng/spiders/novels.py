# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import time
from ..items import ZonghengItem
class NovelsSpider(CrawlSpider):
    name = 'novels'
    # allowed_domains = ['http://book.zongheng.com/store.html']
    start_urls = ['http://book.zongheng.com/store.html']
    num = 0
    rules = (
        # 匹配小说
        Rule(LinkExtractor(allow=r'http://book.zongheng.com/book/(\d+)\.html'), callback='parse_item',process_links="prolink1", follow=True),
        # 目录
        Rule(LinkExtractor(allow=r'http://book.zongheng.com/showchapter/(\d+)\.html'),process_links="prolink2",follow=True),
        # 内容
        Rule(LinkExtractor(allow=r'http://book.zongheng.com/chapter/(\d+)/(\d+)\.html',restrict_xpaths='//li/a'), callback='get_content', process_links="prolink3",follow=False),
    )
    # 过滤
    def prolink1(self,links):
        for link in links:
            # num = int(re.findall(r"\d+\.html", link.url)[0])
            num = int(re.findall(r"(\d+)\.html", link.url)[0])
            if num <= 1032046 and num>1020000:
                print("prolink1",link.url)
                yield link

    def prolink2(self, links):
        for link in links:
            print("prolink2", link.url)
            yield link
        pass

    def prolink3(self, links):
        for link in links:
            print("prolink3", link.url)
            yield link
        pass

    # 翻页
    def parse_start_url(self, response):
        # 'http://book.zongheng.com/store/c0/c0/b0/u0/p3/v9/s9/t0/u0/i1/ALL.html'
        # 'http://book.zongheng.com/store/c0/c0/b0/u0/p2/v9/s9/t0/u0/i1/ALL.html'
        # "http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html"
        self.num += 1
        url = "http://book.zongheng.com/store/c0/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html".format(self.num)
        if self.num <= 3:
            time.sleep(1)
            yield scrapy.Request(url,dont_filter=True)
            time.sleep(1)
        else:
            return

    def get_content(self,response):
        item = ZonghengItem()
        item["book_name"]=response.xpath('//div[@class="reader_crumb"]/a/text()').getall()[-1]
        item["chapter_name"]=response.xpath('//div[@class="title_txtbox"]/text()').get()
        content=response.xpath('//div[@class="content"]/p/text()').getall()
        item["content"]="\n".join(content)
        yield item
        time.sleep(2)
        pass

    def parse_item(self, response):
        item = {}
        print(response.text)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
