# -*- coding: utf-8 -*-
import scrapy


class WensuenSpider(scrapy.Spider):
    name = 'wensuen'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass
