# -*- coding: utf-8 -*-
import scrapy
from QQMusicSpider.utils import qqmusic_singer_list_url_args_index_and_page, qqmusic_singer_index_all_url
import json


class SingerSpider(scrapy.Spider):
    name = 'singer'
    allowed_domains = ['y.qq.com']

    def start_requests(self):
        self.total = {}
        for i in range(1, 28):
            self.total[i] = None
            yield scrapy.Request(url=qqmusic_singer_list_url_args_index_and_page(i, 0))

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())
        index = json_response['singerList']['data']['index']
        if self.total[index] is None:
            self.total[index] = json_response['singerList']['data']['total']
            for i in qqmusic_singer_index_all_url(index, self.total[index]):
                yield scrapy.Request(url=i)

        for i in json_response['singerList']['data']['singerlist']:
            yield i
