# -*- coding: utf-8 -*-
import scrapy


class RanklistSpider(scrapy.Spider):
    name = 'ranklist'
    allowed_domains = ['y.qq.com']
    start_urls = ['https://y.qq.com/']

    def parse(self, response):
        pass
