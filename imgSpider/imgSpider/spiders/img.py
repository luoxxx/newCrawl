# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ImgspiderItem, ImgItem
import time
class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['https://image.baidu.com/']
    start_urls = [
        'http://pic.netbian.com/4kmeinv/'
        # 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1465437065,1548797927&fm=26&gp=0.jpg'
        # 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CB%EF%D2%D5%D5%E4%CD%BC%C6%AC&fr=ala&ala=1&alatpl=star&pos=0&hs=2&xthttps=000000'
        # "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9522006005630346240&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%AD%99%E8%89%BA%E7%8F%8D%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E5%AD%99%E8%89%BA%E7%8F%8D%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&cg=star&pn=90&rn=30&gsm=5a&1611472543473=",
        # 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1611462414892_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E7%8C%AB'
    ]
    # 'http://pic.netbian.com/4kmeinv/'
    # def start_requests(self):
    #     url1 = "https://movie.douban.com/top250/"
    #     url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CB%EF%D2%D5%D5%E4%CD%BC%C6%AC&fr=ala&ala=1&alatpl=star&pos=0&hs=2&xthttps=000000'
    #     yield scrapy.Request(url=url1, callback=self.parse)

    def parse(self, response):
        # print(response.body)
        # res = response.body.decode("utf-8")
        # res = response.text
        # print(res)
        item = ImgspiderItem()
        item["imgurl"] = response.xpath("//div[@class='slist']/ul/li/a/img/@src").extract()
        item["imgdirname"]=response.xpath('//div[@class="classify clearfix"]/a[@class="curr"]/text()').extract()[0]
        item["imgname"] = response.xpath("//div[@class='slist']/ul/li/a/img/@alt").extract()
        yield item
        for url in item["imgurl"]:
            url = "http://pic.netbian.com/" + url
            yield scrapy.Request(url,callback=self.parse_url,dont_filter=True)
            time.sleep(1)

    def parse_url(self,response):
        # print("img------",response.body)
        imgItem = ImgItem()
        imgItem["imgbin"] = response.body
        # print("response.body",type(response.body))
        time.sleep(1)
        yield imgItem
        pass

