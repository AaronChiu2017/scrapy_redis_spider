#-*-coding:utf-8-*-
from __future__ import division
import json
from pprint import pprint
from scrapy import signals
from twisted.internet import task
from twisted.internet import defer
from datetime import datetime
from . import mysignals
from txredisapi import lazyConnectionPool

class MyCustomExtension(object):
	#结合signals, 可以使用extension来定义和收集scrapy的stats
	#并将收集到的stats输出，绘制成图形
	#也可以在其他的类中使用from_crawler这个方法。用来记录日志
	#log出现的error的次数。也可以记录response中多少个404页面等等

	def __init__(self, stats):
		self.stats = stats

	@classmethod
	def from_crawler(cls, crawler):
		instance = cls(crawler.stats)
		crawler.signals.connect(instance.item_dropped, 
								signal=signals.item_dropped)
		crawler.signals.connect(instance.item_scraped, 
								signal=signals.item_scraped)
		crawler.signals.connect(instance.response_received, 
								signal=signals.response_received)
		crawler.signals.connect(instance.response_downloaded, 
								signal=signals.response_downloaded)
		crawler.signals.connect(instance.item_saved,
								signal=mysignals.item_saved)
		crawler.signals.connect(instance.item_saved_failed,
								signal=mysignals.item_saved_failed)
		crawler.signals.connect(instance.html_saved,
								signal=mysignals.html_saved)
		crawler.signals.connect(instance.html_saved_failed,
								signal=mysignals.html_saved_failed)
		crawler.signals.connect(instance.timeouterror,
			                    signal=mysignals.timeouterror)
		crawler.signals.connect(instance.dnslookuperror,
								signal=mysignals.dnslookuperror)
		return instance

	def item_dropped(self, item, spider):
		#接受item在经过itempipeline时被丢弃是发出的信号		
		self.stats.inc_value('item/dropped', spider=spider)	

	def item_scraped(self, item, spider):
		#接受item成功通过所有itempipeline时发出的信号		
		self.stats.inc_value('item/scraped', spider=spider)		

	def response_received(self, response, spider):
		#接受engine接收到一个response时发送的信号	
		self.stats.inc_value('response/received', spider=spider)	

	def response_downloaded(self, response, spider):
		#接受下载器成功下载一个response时发送的信号		
		self.stats.inc_value('response/downloaded', spider=spider)

	def item_saved(self, spider):
		self.stats.inc_value('item/saved', spider=spider)

	def item_saved_failed(self, spider):
		self.stats.inc_value('item_saved/failed', spider=spider)

	def html_saved(self, spider):
		self.stats.inc_value('html/saved', spider=spider)

	def html_saved_failed(self, spider):
		self.stats.inc_value('html_saved/failed', spider=spider)

	def timeouterror(self, spider):
		self.stats.inc_value('twisted/timeouterror', spider=spider)

	def dnslookuperror(self, spider):
		self.stats.inc_value('twisted/dnslookuperror', spider=spider)


class MyCustomStatsExtension(object):
	"""
	这个extension专门用来定期搜集一次stats
	"""
	def __init__(self, stats, config):
		self.config = config
		self.stats = stats
		self.time = 60.0

	@classmethod
	def from_crawler(cls, crawler, *args, **kwargs):
		instance = cls(crawler.stats, crawler.settings.get('TWISTED_REDIS_CONFIG'))
		crawler.signals.connect(instance.opened_spider, signal=signals.spider_opened)
		crawler.signals.connect(instance.closed_spider, signal=signals.spider_closed)
		return instance
	
	@defer.inlineCallbacks
	def opened_spider(self, *args, **kwargs):
		self.rc = yield lazyConnectionPool(**self.config)
		self.tsk = task.LoopingCall(self.collect)
		self.tsk.start(self.time, now=True)

	@defer.inlineCallbacks
	def closed_spider(self, *args, **kwargs):
		yield self.rc.disconnect()		
		if self.tsk.running:
			self.tsk.stop()

	@defer.inlineCallbacks
	def collect(self):
		#这里收集stats并写入相关的redis
		result = self.stats.get_stats()
		result.pop('start_time', 0)
		start_cpu = result.get('memusage/startup')
		if start_cpu:
			result['memusage/startup'] = round(start_cpu/1024/1024, 3)

		max_cpu = result.get('memusage/max')
		if max_cpu:
			result['memusage/max'] = round(max_cpu/1024/1024, 3)

		yield self.rc.rpush('scrapy_stats', json.dumps(result))
		


