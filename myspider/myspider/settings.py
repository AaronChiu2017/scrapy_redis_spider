# -*- coding: utf-8 -*-

# Scrapy settings for myspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myspider'

SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'

#http://scrapy.readthedocs.io/en/latest/topics/broad-crawls.html
REACTOR_THREADPOOL_MAXSIZE = 20

#内存调试配置,只在linux上起作用
#启用内存调试
MEMDEBUG_ENABLED = True
#报告内存调试
MEMDEBUG_NOTIFY = ['524964426@qq.com']
#启用scrapy.extensions.memusage扩展，当找过内存限制时，就关闭scrapy进程，并发送邮件
MEMUSAGE_ENABLED = True
#内存的最大使用限制,单位是MB
MEMUSAGE_LIMIT_MB = 100
#当内存使用超过一定的限制后，就发送邮件警告,单位是MB
MEMUSAGE_WARNING_MB = 80
#每个一段时间就检查内存的使用情况
MEMUSAGE_CHECK_INTERVAL_SECONDS = 30.0
#当内存使用超过限制的时候，就发送邮件到邮箱
MEMUSAGE_NOTIFY_MAIL = ['524964426@qq.com']
#当spider关闭的时候是否发送内存使用报告
MEMUSAGE_REPORT = True

#user-agent列表，用于随机使用
MY_USER_AGENT = ["Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/28.0.1500.95+Safari/537.36+SE+2.X+MetaSr+1.0",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/50.0.2657.3+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/51.0.2704.106+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/47.0.2526.108+Safari/537.36+2345Explorer/7.1.0.12633",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_11_4)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/49.0.2623.110+Safari/537.36",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_9_5)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/42.0.2311.152+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/42.0.2311.152+Safari/537.36",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_10_2)+AppleWebKit/600.3.18+(KHTML,+like+Gecko)+Version/8.0.3+Safari/600.3.18",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/49.0.2623.22+Safari/537.36+SE+2.X+MetaSr+1.0",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_11_4)+AppleWebKit/601.5.17+(KHTML,+like+Gecko)+Version/9.1+Safari/601.5.17",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/48.0.2564.103+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/47.0.2526.80+Safari/537.36+Core/1.47.640.400+QQBrowser/9.4.8309.400",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_10_5)+AppleWebKit/600.8.9+(KHTML,+like+Gecko)+Version/8.0.8+Safari/600.8.9",
    "Mozilla/5.0+(Windows+NT+6.3;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/39.0.2171.99+Safari/537.36+2345Explorer/6.4.0.10356",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.87+Safari/537.36+QQBrowser/9.2.5584.400",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/47.0.2526.111+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/33.0.1750.146+BIDUBrowser/6.x+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/39.0.2171.99+Safari/537.36+2345Explorer/6.5.0.11018",
    "Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/42.0.2311.154+Safari/537.36+LBBROWSER"]

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 4
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
   'Accept-Language': 'zh-CN,zh;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
}

STATS_CLASS = 'scrapy.statscollectors.MemoryStatsCollector'


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #'myspider.spidermiddlewares.MyCustomSpiderMiddleWares': 543,
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 850,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}

#spider-middleware的一些配置
#UrlLengthMiddleware, 能抓取的url的最大长度
URLLENGTH_LIMIT = 200

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'myspider.downloadermiddlewares.MyCustomHeadersDownLoadMiddleware': 555,    
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 950,
    'myspider.downloadermiddlewares.MyProcessResponseDownloadMiddleware': 900,
    'myspider.downloadermiddlewares.MyProcessExceptionDownloadMiddleware': 920,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': None,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,   
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': None,
}

#启用'scrapy.downloadermiddlewares.stats.DownloaderStats'
DOWNLOADER_STATS = True

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': 100,
    'scrapy.extensions.memusage.MemoryUsage': 100,
    'scrapy.extensions.memdebug.MemoryDebugger': 100,
    'scrapy.extensions.closespider.CloseSpider': 100,
    'myspider.extensions.MyCustomExtension': 100,
    'scrapy.extensions.logstats.LogStats': 100,
    'myspider.extensions.MyCustomStatsExtension': 100,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 3.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

#scrapy-redis setting
######################################################################################################################
########################################################################################################################3
# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
#scapy_redis过滤请求是把请求的指纹放到redis的集合数据结构中。然后比较
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Default requests serializer is pickle, but it can be changed to any module
# with loads and dumps functions. Note that pickle is not compatible between
# python versions.
# Caveat: In python 3.x, the serializer must return strings keys and support
# bytes as values. Because of this reason the json or msgpack module will not
# work by default. In python 2.x there is no such issue and you can use
# 'json' or 'msgpack' as serializers.
#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"


# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
	#scrapy_redis管道是把提取到的item放到redis的item队列中
    #所以需要另外编写一个脚本从这个队列中获取item
    'scrapy_redis.pipelines.RedisPipeline': 300
    #'myspider.pipelines.MyCustomSpiderPipeline': 100
}

# The item pipeline serializes and stores the items in this redis key.
#这等于spider.name:items.在这个spider中，存储item的redis队列的名字叫做："static_html:items"
REDIS_ITEMS_KEY = '%(spider)s:items'

# The items serializer is by default ScrapyJSONEncoder. You can use any
# importable path to a callable object.
#使用json将item序列化
REDIS_ITEMS_SERIALIZER = 'json.dumps'

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
#REDIS_URL = 'redis://user:pass@hostname:9001'

# Custom redis client parameters (i.e.: socket timeout, etc.)
#REDIS_PARAMS  = {}
# Use custom redis client class.
#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# If True, it uses redis' ``spop`` operation. This could be useful if you
# want to avoid duplicates in your start urls list. In this cases, urls must
# be added via ``sadd`` command or you will get a type error from redis.
REDIS_START_URLS_AS_SET = True

# How many start urls to fetch at once.
REDIS_START_URLS_BATCH_SIZE = 3

# Default start urls key for RedisSpider and RedisCrawlSpider.
#如果在spider中设置了redis_key，那么就会覆盖这个配置。
#REDIS_START_URLS_KEY = '%(name)s:start_urls'

#"""dialect+driver://username:password@host:port/database"""
SQLALCHEMY_URL = 'mysql+pymysql://root:lymlhhj123@127.0.0.1/douban'

#SQLALCHEMY的engine配置
SQLALCHEMY_ENGINE_CONFIG = {'pool_recycle': 3600,
                            'encoding': 'utf-8', 
                            'pool': None,
                            'poolclass': None,
                            'pool_size': 5,
                            'echo': False,
                            'echo_pool': False,
                            'max_overflow': 10, 
                            'pool_timeout': 30,}

#自定义的redis的客户端参数配置
MY_REDIS_CONFIG = {'host': '127.0.0.1',
        'port': 6379,
        'db': 0,
        'max_connections': 25,
        'password': None}

#e-mail scrapy.mail.MailSender设置
#MAIL_FROM = 
#MAIL_PORT = 
#MAIL_USER = 
#MAIL_PASS = 
#MAIL_TLS = 
#MAIL_SSL = 

#当达到下面的设置条件后就关闭spider
#以下的条件默认值都是0，表示没有设置任何条件
#如要设置条件，设置一个整数值即可
#http://scrapy.readthedocs.io/en/latest/topics/extensions.html
CLOSESPIDER_TIMEOUT = 0
CLOSESPIDER_ITEMCOUNT = 0
CLOSESPIDER_PAGECOUNT = 0
CLOSESPIDER_ERRORCOUNT = 0


#log配置
#https://github.com/scrapy/scrapy/pull/2242
#scrapy目前还不支持自定义log handler，但应该会在以后的版本出现，具体看上面的链接
LOG_ENABLED = True
LOG_ENCODING = 'UTF-8'
LOG_FILE = None
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False


#twisted mysql config
TWISTED_MYSQL_CONFIG = {'dbapiName': 'MySQLdb',
                        'db': 'douban',
                        'host': '127.0.0.1',
                        'port': '3306',
                        'passwd': 'lymlhhj123',
                        'user': 'root',
                        'cp_reconnect': True,}


#twisted redis config
TWISTED_REDIS_CONFIG = {'host': "localhost", 
                        'port': 6379, 
                        'dbid': None,
                        'poolsize': 10, 
                        'reconnect': True, 
                        'charset': "utf-8",
                        'password': None, 
                        'connectTimeout': None, 
                        'replyTimeout': None,
                        'convertNumbers': True,}



