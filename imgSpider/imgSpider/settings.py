# -*- coding: utf-8 -*-

# Scrapy settings for imgSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'imgSpider'

SPIDER_MODULES = ['imgSpider.spiders']
NEWSPIDER_MODULE = 'imgSpider.spiders'

# URLLENGTH_LIMIT = 10000
# URLLENGTH_LIMIT = 60
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imgSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
  #   "Accept": "text/plain, */*; q=0.01",
  #   "Accept-Encoding": "gzip, deflate, br",
  #   "Accept-Language": "zh-CN,zh;q=0.9",
  #   "Cache-Control": "no-cache",
  #   "Connection": "keep-alive",
  #   "Cookie": "winWH=%5E6_1242x597; BDIMGISLOGIN=0; BDqhfp=%25CB%25EF%25D2%25D5%25D5%25E4%25CD%25BC%25C6%25AC%26%26NaN-1undefined%26%260%26%261; PSTM=1565685151; BIDUPSID=95243DA221AD7C3BBA34F7D9DF20052E; BDUSS=FVIa1NkaFRnd0wzYVNZcjgxSmVjN1YwWnh-WWJ4a3pUVjNLWHN2UGtaQ2dYdUpkRVFBQUFBJCQAAAAAAAAAAAEAAAAw~DRU0rvWprbAuq7DtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDRul2g0bpde; BDUSS_BFESS=FVIa1NkaFRnd0wzYVNZcjgxSmVjN1YwWnh-WWJ4a3pUVjNLWHN2UGtaQ2dYdUpkRVFBQUFBJCQAAAAAAAAAAAEAAAAw~DRU0rvWprbAuq7DtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDRul2g0bpde; BAIDUID=0416B19BD25B6F015648C9BD54B3EB1A:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; __yjs_duid=1_9f2119b612fe5171cd63d101a5a466891611455075705; H_WISE_SIDS=110085_154619_155932_162898_163115_163566_164215_165134_165143_165294_166419_167390_167406_167603_168013_168099_168397_168402; yjs_js_security_passport=1628b6f0b4ee6dae185bc28bccbbc8da2d04bd64_1611458448_js; delPer=0; PSINO=1; BAIDUID_BFESS=470B622335419ED730F5263C05AEACBE:FG=1; BDRCVFR[zv4OXfrzgxs]=lPVrSIjWtIsuAFWuA68mvqV; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ZD_ENTRY=baidu; cleanHistoryStatus=0; indexPageSugList=%5B%22%E7%8C%AB%22%2C%22%E5%9B%BE%E7%89%87%22%2C%22%E9%9F%A9%E5%AD%9D%E5%91%A8%22%2C%22iu%22%2C%22%E5%AD%99%E8%89%BA%E7%8F%8D%E5%AD%A6%E7%94%9F%E5%A3%81%E7%BA%B8%22%2C%22%E5%AD%99%E8%89%BA%E7%8F%8D%E5%B9%B4%E8%BD%BB%E6%97%B6%E5%80%99%E6%A1%8C%E9%9D%A2%E5%A3%81%E7%BA%B8%22%2C%22%E7%88%B1%E7%AC%91%E7%9A%84%E6%9D%8E%E7%9F%A5%E6%81%A9%22%2C%22%E5%8F%AF%E7%88%B1%E7%9A%84%E6%9D%8E%E7%9F%A5%E6%81%A9%22%2C%22%E9%9F%A9%E5%AD%9D%E5%91%A8%E5%A3%81%E7%BA%B8%22%5D; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; BDRCVFR[Im6cQUY0Pc3]=mk3SLVN4HKm; BCLID=10730866281541475173; BDSFRCVID=YRtOJexroG3VXHneBXqY-_t9hdSNzdcTDYLEOwXPsp3LGJLVN4vPEG0Pt_U-mEt-J8jwogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbkD_C-MfIvDqTrP-trf5DCShUFsB6DjB2Q-XPoO3KO4ohnkbf5iKt7DBp88aP3gBjQb3MbgylRp8P3y0bb2DUA1y4vpWj3qLgTxoUJ2XMKVDq5mqfCWMR-ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5PVKgTa54cbb4o2WbCQbqQT8pcN2b5oQTtZW-7XKxjv-6uLM--X2nb684cg-pOUWfAkXpJvQnJjt2JxaqRCBDb-Vh5jDh3MBpQDhtoJexIO2jvy0hvctn3cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDNtDt60jfn3aQ5rtKRTffjrnhPF35jvDXP6-hnjy3b7phpn85loiqfFzBn8BM-09Xl6b5h3RymJ42-39LPO2hpRjyxv4X60B0-oxJpOJXaILWl52HlFWj43vbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK0hJC-2bKvPKITD-tFO5eT22-usK5rW2hcHMPoosIOKWM7_bfDRKJ8Lyb082Ing2tceKMbUoqRHXnJi0btQDPvxBf7pBJnqbp5TtUJM_UKzhfoMqfTbMlJyKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDTtajj3QeaRabK6aKC5bL6rJabC3ofomXU6q2bDeQNbpXUvX5mrvQxIEX--BjbbbXR6f-p0vWtv4WbbvLT7johRTWqR48CbC0MonDh83Bn_L2xQJHmLOBt3O5hvvhb3O3MA-yUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRFeVI-y3f; BCLID_BFESS=10730866281541475173; BDSFRCVID_BFESS=YRtOJexroG3VXHneBXqY-_t9hdSNzdcTDYLEOwXPsp3LGJLVN4vPEG0Pt_U-mEt-J8jwogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbkD_C-MfIvDqTrP-trf5DCShUFsB6DjB2Q-XPoO3KO4ohnkbf5iKt7DBp88aP3gBjQb3MbgylRp8P3y0bb2DUA1y4vpWj3qLgTxoUJ2XMKVDq5mqfCWMR-ebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5PVKgTa54cbb4o2WbCQbqQT8pcN2b5oQTtZW-7XKxjv-6uLM--X2nb684cg-pOUWfAkXpJvQnJjt2JxaqRCBDb-Vh5jDh3MBpQDhtoJexIO2jvy0hvctn3cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDNtDt60jfn3aQ5rtKRTffjrnhPF35jvDXP6-hnjy3b7phpn85loiqfFzBn8BM-09Xl6b5h3RymJ42-39LPO2hpRjyxv4X60B0-oxJpOJXaILWl52HlFWj43vbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK0hJC-2bKvPKITD-tFO5eT22-usK5rW2hcHMPoosIOKWM7_bfDRKJ8Lyb082Ing2tceKMbUoqRHXnJi0btQDPvxBf7pBJnqbp5TtUJM_UKzhfoMqfTbMlJyKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDTtajj3QeaRabK6aKC5bL6rJabC3ofomXU6q2bDeQNbpXUvX5mrvQxIEX--BjbbbXR6f-p0vWtv4WbbvLT7johRTWqR48CbC0MonDh83Bn_L2xQJHmLOBt3O5hvvhb3O3MA-yUKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRFeVI-y3f; userFrom=ala; ab_sr=1.0.0_ZWIxOWM2ZjQ1ZGJmZjljZWJlMWI1YmI3NDhjNGJmYmY4NzVjY2VjZDAyYmNiMWIwZGM0YjFmZmViNTJhODg3MjBlYzE0NWJmNDUzYzJiYjBlMjFmYTczNzk0OGMxMzZlNDBmOGY5MmVlOTM1M2UzNjhkN2NjYzU4N2NhOGNiOWI=",
  #   "Host": "image.baidu.com",
  #   "Pragma": "no-cache",
  #   "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CB%EF%D2%D5%D5%E4%CD%BC%C6%AC&fr=ala&ala=1&alatpl=star&pos=0&hs=2&xthttps=000000",
  #   "sec-ch-ua": '"Google Chrome";v="87", "\"Not;A\\Brand";v="99", "Chromium";v="87"',
  #   "sec-ch-ua-mobile": "?1",
  #   "Sec-Fetch-Dest": "empty",
  #   "Sec-Fetch-Mode": "cors",
  #   "Sec-Fetch-Site": "same-origin",
  #   "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest",
}
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'imgSpider.middlewares.ImgspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'imgSpider.middlewares.ImgspiderDownloaderMiddleware': 543,
#     'myproject.middlewares.ProxyMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'imgSpider.pipelines.ImgspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

