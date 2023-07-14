# Scrapy settings for licence project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "licence"

SPIDER_MODULES = ["licence.spiders"]
NEWSPIDER_MODULE = "licence.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "licence (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

LOG_LEVEL = 'ERROR'

# Disable cookies (enabled by default)
#COOKIES_ENABLED = FalseWORNING

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

    # 'Cookie':'C9nvPf17Htt4O=55pu4znTEkOVP.q4xayk.rpio_5GQF91LIfz.4Hu7uX2Yz0h0c7utU24.kERjPq7TDayUaHM8Fv86oDbMuWgg_A;849899999d514676a3=2849534d163fd9d6a7384fb2986215a1; JSESSIONID=34577909F264D1185B48E23C7DE1C72A;C9nvPf17Htt4P=NSuxz6ngIDP2FPuZ1d9YxENKEerHu.N7DHx6CtnCCuGpFFkP5e4c7f4XrKAeDm8X2wRLpdBsDowO_MsF0bPQSyngliHLAXQu2_9bHE3NWi3p_U0k0C.8d3_548ysnZt5B3Bd7juAu2p7lbMwKv2jZrwBfN1xt2hPqFVv9yXwVSs_ojPmYU31mksCoSudluVsPKElq8jm6.y1kSM.A2qlg_16OLQTwtQL0HeY0jalU3tUSp_IXJNOzstLCRlEA_KYlQg9mNX5S4629z8zX8HaYdFuR3sOP2nmFFb9nxuZaNOlJL9FhJKPoeUDvYIK6.JrHayPzdovCtVspfx1WSpldN.3Y1IhCGCxzIXSzTArEssgXAuDaKNlv6ysY6YNvCKCUodb7yh1hY1PHZjwfsWtiuUuQ4NYfY6Vd6JXrgD8Mw8Q9m.1rnGXk8nTgqHbfzOW',
    # 'Host':'entp.yjj.gxzf.gov.cn',
    # # 'Origin':'http://spxk.scjg.tj.gov.cn',
    # # 'Referer':'http://spxk.scjg.tj.gov.cn/enterpriseSearch/enterpriseSearchAction!spscList.dhtml',
    # 'Upgrade-Insecure-Requests':1,
    # 'Sec-Fetch-Dest':'document',
    # 'Sec-Fetch-Mode':'navigate'
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control':'max-age=0',
    # 'Connection':'keep-alive',
    # 'Content-Type':'application/x-www-form-urlencoded',
    # 'Content-Type':'application/json',
    # 'Cookie':'C9nvPf17Htt4O=55pu4znTEkOVP.q4xayk.rpio_5GQF91LIfz.4Hu7uX2Yz0h0c7utU24.kERjPq7TDayUaHM8Fv86oDbMuWgg_A; 849899999d514676a3=2849534d163fd9d6a7384fb2986215a1; JSESSIONID=34577909F264D1185B48E23C7DE1C72A; C9nvPf17Htt4P=zkPXNsGI5fwJ3wCcQsrEct1yalSfBILIjp8JnmYM3FSaGy7cSlGKb2QEj.9TQS_4oUF.hyqyGTd5Hg8LgvJcqSzPAlgHVtUDab2TcNTR71Ca3IlCSLOP9hXsKEGrcZFA9.w.c7zDxyTDo3SnPUGSE0Y8DWUwIpJAcq0KCzZtGKVicQaOOvGj95zbhQJa8QhAfceAQ4X2UzyPWZnmJykIQYzruvmD6dkFRmDutIioIYyEpUtTbNEx508Cu1ozMnRXjfWr4k.moLqHF97y2lsxGGp0lxzDde81oeUVFqSkJP3TPe0Y3Cjx9BHa2P9PKu0R0ixIBWfMBeJp6bMDgF0O3LodzktpEHIGVcrwcyu3d1NTGig.Oc9QkZfA10fqAWLQ',
    # 'Host':'entp.yjj.gxzf.gov.cn',
    # 'Origin':'https://entp.yjj.gxzf.gov.cn',
    # 'Referer':'https://entp.yjj.gxzf.gov.cn/appnet/appEntpList.action',
    # 'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    # 'Sec-Ch-Ua-Mobile':'?0',
    # 'Sec-Ch-Ua-Platform':"Windows",
    # 'Sec-Fetch-Dest':'document',
    # 'Sec-Fetch-Mode':'navigate',
    # 'Sec-Fetch-Site':'same-origin',
    # 'Sec-Fetch-User':'?1',
    # 'Upgrade-Insecure-Requests':'1',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'





    # neimenggu
    # 'Cookie':'JSESSIONID=E058476F79E473BCA308CD0E85E09238',
    # 'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Content-Type':'application/json',
    # 'Host':'117.161.154.157:7011',
    # 'Origin':'http://117.161.154.157:7011',
    # 'Referer':'http://117.161.154.157:7011/dc/jsp/dc/industry/query/fooddrug/spschz_info_list.jsp',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # 'X-Requested-With':'XMLHttpRequest',

    # yunnan
    # 'sign': 'RdSuZszAa+26T8RF2X9uItAstVrdrTdryVgzK6zfS6YHuCdd2TEmCd6GdZkIGef9l8UOMJbgM7fvNI0R/oODEE3O/HRtwr2RyO/OLBpqlOX1GMQmn5DwmryVhQgRuFZ3ETjRG3ETCIId2H9r2HyxpU72va9YrhNxfFB/NbB0LHU=',
    # 'timestamp': '1688697584000',
    # 'Cookie': 'COLLPCK=3323192790; xzxk_wbjg=60111794; notice=35733588'

    # guanxgi 
    'Cookie':'C9nvPf17Htt4O=5HOeo.t4JxNCJtSBxjvR9fMF7GKE3zMUYr54tjrp44W4.zhJZdHnixX_92PydR.mjCdXpiXBgVXuuCLzKAd7erA; 849899999d514676a3=db5b19f02871b5caed0ddb84d90821ce; JSESSIONID=BCD53D9DA25890DCC9995757716F5AD6; C9nvPf17Htt4P=X4BQZ.aJHFZsejqL3A0ovAYNOPOxYu._uMw77_41shBR4VnHENHYZaew4vnpNKm0xmHn55BLLBtdZ5H5frXqtwBy.1Yx1HrnpnrWRIBBgU031zGTMuFMJuWWaavdz8xAVgcKKqv1lOOyQfNDhJbIx0DUvtN1wjSuwCG6Adab7oUzo0UCRsaaz33M5byQxp2Or7KlI5mIVx8mUgS7LDHJwByJH1skl2tD5.9R4UB.Pl5sReod9uA3TEUB2GhI2SOSoKQBtsTt3aZ5QF6R0ekoUldMdPW_Iq9cKrwGB_C_YrU9GouCa_DVicnaWOSmhw6ImxvHVeH5KczwM0SzrZ9X2gFLIvj78chbgQFUCubuz5o1wrhwmQcGfawkaXR54.mSUldyzS.tZwQ_QL0bjrrdRYNYTNHeR.NBmzz1x2Do2AKaDIUIxC91M9Yo7hFegE92'
}
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "licence.middlewares.LicenceSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "licence.middlewares.LicenceDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "licence.pipelines.LicenceCsvPipeline": 300,
#    "licence.pipelines.FujianLicenceCsvPipeline": 300
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
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

