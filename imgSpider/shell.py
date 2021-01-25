from scrapy.cmdline import execute
url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CB%EF%D2%D5%D5%E4%CD%BC%C6%AC&fr=ala&ala=1&alatpl=star&pos=0&hs=2&xthttps=000000"
s = "scrapy shell " + url

execute(s.split())