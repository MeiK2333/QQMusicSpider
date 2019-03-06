# -*- coding: utf-8 -*-
import json
import re

import scrapy

from spider.conf import RankType
from spider.items import TopListItem


class ToplistSpider(scrapy.Spider):
    name = 'toplist'

    def start_requests(self):
        for item in RankType:
            yield scrapy.Request(f'https://y.qq.com/n/yqq/toplist/{item.value}.html', meta={'rank_type': item}, callback=self.parse_date)

    def parse_date(self, response):
        """ 解析页面以获得日期参数 """
        rank_type = response.meta['rank_type']
        js_data = re.search(r'toplist.init(.*);', response.body_as_unicode())
        data = json.loads(js_data.group()[13:-2])

        first_date = data['dateList'][0]
        params = {
            'date': first_date,
            'page': 'detail',
            'topid': str(rank_type.value),
            'type': 'top',
            'song_begin': '0',
            'song_num': '300',
            'jsonpCallback': '',
            'format': 'jsonp',
        }
        if rank_type.value > 100:
            params['type'] = 'global'

        yield scrapy.FormRequest(f'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg', method='GET', formdata=params, meta={'rank_type': rank_type})

    def parse(self, response):
        """ 解析排行信息 """
        data = json.loads(response.body_as_unicode())
        for i in data['songlist']:
            j = i['data']
            item = TopListItem()
            item['in_count'] = i['in_count']
            item['old_count'] = i['old_count']
            item['rank_name'] = response.meta['rank_type'].name
            item['rank_value'] = response.meta['rank_type'].value
            item['type_'] = j.pop('type')
            for key, value in j.items():
                item[key] = value
            yield item
