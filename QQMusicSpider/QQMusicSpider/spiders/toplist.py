# -*- coding: utf-8 -*-
import json
import re
import scrapy

from QQMusicSpider.utils import RankType
from QQMusicSpider.items import QQMusicItem


class RanklistSpider(scrapy.Spider):
    name = 'toplist'
    allowed_domains = ['y.qq.com']

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

        yield scrapy.FormRequest(f'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg', formdata=params, meta={'rank_type': rank_type})

    def parse(self, response):
        """ 解析排行信息 """
        data = json.loads(response.body_as_unicode())
        # 添加榜单本身的信息，以便后续查找使用
        data['rank_type_name'] = response.meta['rank_type'].name
        data['rank_type_value'] = response.meta['rank_type'].value

        item = QQMusicItem()
        item['item_type'] = 'toplist'
        item['data'] = data
        yield item
