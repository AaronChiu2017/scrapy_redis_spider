# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re
from urlparse import urlparse, urljoin
import scrapy
import parsel
from w3lib.url import canonicalize_url
from scrapy.loader.processors import TakeFirst, Join, Compose
from . import html

class RegExp(object):
    def __init__(self):
        self.reg = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')

    def __call__(self, item):
        result = self.reg.search(item)
        result = result.group() if result else ''
        return result
        
#def custom_output_process(item):
#	pass


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #关于这里使用的输入输出处理器，建议最好配合mapcompose一起使用
    #首先调用scrapy内建的输入输出处理器函数，然后在调用自定义的函数
    #这样就可以得到较为精准的数据
    movie_name = scrapy.Field(input_processor=Compose(TakeFirst()),
    					  output_processor=Compose(Join()),)

    movie_type = scrapy.Field(input_processor=Compose(TakeFirst()),
    					  output_processor=Compose(Join()),)

    movie_rate = scrapy.Field(input_processor=Compose(TakeFirst()),
    					  output_processor=Compose(Join()),)

    movie_year = scrapy.Field(input_processor=Compose(TakeFirst(), RegExp()),
    					  output_processor=Compose(Join()),)

    url = scrapy.Field(output_processor=Compose(Join()))


class LinkExtractor(object):
    def __init__(self, allow=(), deny=(), allow_domains=()):
        self.allow_re = [re.compile(x) for x in allow] if allow else []
        self.deny_re = [re.compile(x) for x in deny] if deny else []
        self.allow_domains = allow_domains
        self.selector = parsel.Selector

    def url_allowed(self, url):
        parsed_url = urlparse(url)
        if parsed_url.netloc:
            domained = [x in parsed_url.netloc for x in self.allow_domains] if self.allow_domains else [True]
            if not any(domained):
                return False
        allowed = [x.search(url) for x in self.allow_re ] if self.allow_re else [True]
        denied = [x.search(url) for x in self.deny_re] if self.deny_re else []

        return any(allowed) and not any(denied)

    def extract_links(self, response):
        l = []
        base_url = response.url
        text = html.html_to_unicode(response)
        self.sel = self.selector(text, type='html')
        links  = set(self.sel.xpath('//a/@href').extract())
        links = [url for url in links if self.url_allowed(url)]
        for url in links:
            url = canonicalize_url(urljoin(base_url, url))
            l.append(url)
        else:
            return l




