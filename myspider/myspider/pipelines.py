# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from .connection import BaseAsyncMySQL
from .mysignals import (item_saved, item_saved_failed)

#异步执行数据库操作的管道
class MyCustomMySQLPipeline(BaseAsyncMySQL):
	#python2.7中使用yield的函数，就不允许使用return
	#所以在2.7中发送信号就使用send_catch_log()

	def process_item(self, item, spider):
		try:
			self.insert(item, spider).addCallback(self.callback)
		except Exception:
			 self.crawler.signals.send_catch_log(item_saved_failed,
				                                 spider=spider)
		else:
			 self.crawler.signals.send_catch_log(item_saved,
											     spider=spider)
		return item

	def insert(self, item):
		cmd = 'INSERT INTO douban VALUES (?,?,?);'		
		return self.db.runOperation(cmd, item)
		
	def callback(self, value):
		self.logger.info('successfully')








