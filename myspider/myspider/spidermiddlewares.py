#-*-coding:utf-8-*-
from scrapy import signals
from .connection import BaseMiddlewareClass

class MyCustomSpiderMiddleWares(BaseMiddlewareClass):
	#这个中间件用于将response存储到mysql数据库中
	def process_spider_output(self, response, result, spider):
		#该方法处理spider解析response的输出，
		#所以result有可能是item或者是可迭代的requests对象
		#这里就可以处理一些request对象或者处理tiem
		#process_spider_output() must return an iterable of Request, dict or Item objects.
		items = ()
		self.insert(items).addCallback(callback)
		return result

	def insert(self, items):
		cmd = 'INSERT INTO [tablename] (fieldname) VALUES (?)'
		return self.db.runQuery(cmd, items)

	def callback(self, value):
		self.logger.info()

