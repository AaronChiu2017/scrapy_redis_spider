# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from txredisapi import lazyConnectionPool
from scrapy import signals
from twisted.internet import defer
from .connection import BaseMiddlewareClass
from .mysignals import (item_saved, item_saved_failed)

class MyCustomRedisSpiderPipeline(object):
	"""
	scrapy-redis的pipeline是将item放到redis的队列中
	只要是出于分布式抓取的考虑，可以把不同机器上的item
	集中放到一个地方。
	所以自定义的pipeline最好优先级高于redis的pipeline
	可以做一些item去重，过滤，清洗的工作等

	但如果我们只是使用一台机器抓取，可以禁用scrapy-redis的
	pipeline，然后直接将item存放到数据库中

	异步执行redis操作
	"""
	def __init__(self, crawler, redis):
		self.crawler = crawler
		#https://github.com/fiorix/txredisapi
		self.redis = redis

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler, crawler.settings.get('TWISTED_REDIS_CONFIG'))
		
	@defer.inlineCallbacks
	def open_spider(self, spider):
		#使用的是适用于twisted的redis非阻塞链接
		#如果单独使用，就需要创建一个reactor
		#scrapy中已经有reactor,所以不需要我们创建
		self.rc = yield lazyConnectionPool(**self.redis)

	@defer.inlineCallbacks
    	def process_item(self, item, spider):
    		#所有的操作都是异步的，即都是使用yield,因此都需要用装饰器包装
    		yield self.rc.push('item', item)
    		#do something
       		yield item

    	@defer.inlineCallbacks
    	def close_spider(self, spider):
    		yield self.rc.disconnect()


#异步执行数据库操作的管道
class MyCustomMySQLPipeline(BaseMiddlewareClass):
	
	@classmethod
	def from_crawler(cls, crawler):
		instance = super(MyCustomMySQLPipeline, cls).from_crawler(crawler)
		instance.crawler = crawler
		return instance

	def process_item(self, item, spider):
		try:
			self.insert(item).addCallback(callback)
		except:
			self.crawler.signals.send_catch_log(item_saved_failed,
				                                               spider=spider)
		else:
			self.crawler.signals.send_catch_log(item_saved,
															   spider=spider)
		finally:
			return item

	def insert(self, item):
		cmd = 'INSERT INTO [tablename] (fieldname) VALUES (???)'
		return self.db.runQuery(cmd, item)

	def callback(self, value):
		self.logger.info()





