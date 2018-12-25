# -*- coding: utf-8 -*-
import scrapy
import json


class SingerSpider(scrapy.Spider):
    name = 'singer'
    allowed_domains = ['y.qq.com']

    def start_requests(self):
        pass

    def parse(self, response):
        pass
