#-*-coding:utf-8-*
from scrapy import signals
from .connection import BaseAsyncMySQL
from twisted.internet import defer
from .mysignals import (html_saved, html_saved_failed)

class MyCustomSpiderMiddleWares(BaseAsyncMySQL):
	#这个中间件用于将response存储到mysql数据库中

	def process_spider_output(self, response, result, spider):
		#该方法处理spider解析response的输出，
		#所以result有可能是item或者是可迭代的requests对象
		#这里就可以处理一些request对象或者处理tiem
		#process_spider_output() must return an iterable of Request, dict or Item objects.
		items = ()		
		self.insert(items).addCallback(self.callback)		
		return result

	def insert(self, items):
		try:
			cmd = 'INSERT INTO douban VALUES (?,)'
			return self.db.runQuery(cmd, items)
		except Exception as e:
			#发生异常就发送html_saved_failed信号
			self.crawler.signals.send_catch_log(html_saved_failed, spider=spider)
		else:
			self.crawler.signals.send_catch_log(html_saved, spider=spider)


	def callback(self, value):
		self.logger.info('')

