#-*-coding:utf-8-*-
from scrapy import signals
from twisted.internet import defer
from twisted.enterprise import adbapi
from txredisapi import lazyConnectionPool

#mysql数据库异步非阻塞操作的基类
class BaseAsyncMySQL(object):

	def __init__(self, crawler, config):
		self.crawler = crawler
		self.config = config

	@classmethod
	def from_crawler(cls, crawler):
		instance = cls(crawler, crawler.settings.get('TWISTED_MYSQL_CONFIG'))
		crawler.signals.connect(instance.opened_spider, signal=signals.spider_opened)
		crawler.signals.connect(instance.closed_spider, signal=signals.spider_closed)
		return instance
		
	def opened_spider(self, spider):
		self.db = adbapi.ConnectionPool(**self.config)

	def closed_spider(self, spider):
		self.db.close()


#异步的redis基类
class BaseAsyncRedis(object):

	def __init__(self, config, crawler):
		self.config = config
		self.crawler = crawler

	@classmethod
	def from_crawler(cls, crawler):
		instance = cls(crawler.settings.get('TWISTED_REDIS_CONFIG'), crawler)
		crawler.signals.connect(instance.opened_spider, signal=signals.spider_opened)
		crawler.signals.connect(instance.closed_spider, signal=signals.spider_closed)
		return instance

	@defer.inlineCallbacks
	def opened_spider(self, spider):
		self.rc = yield lazyConnectionPool(**self.config)

	@defer.inlineCallbacks
	def closed_spider(self, spider):
		yield self.rc.disconnect()