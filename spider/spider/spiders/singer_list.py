# -*- coding: utf-8 -*-
import json

import scrapy

from spider.items import SingerListItem


class SingerListSpider(scrapy.Spider):
    name = 'singer_list'
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&inCharset=utf8&outCharset=utf-8&notice=0&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A{index}%2C%22sin%22%3A80%2C%22cur_page%22%3A2%7D%7D%7D'

    def start_requests(self):
        for i in range(1, 28):
            yield scrapy.Request(url=self.url.format(index=i), meta={
                'index': i,
                'cur_page': 1
            })

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        index = response.meta['index']
        cur_page = response.meta['cur_page']
        total = data['singerList']['data']['total']

        for i in data['singerList']['data']['singerlist']:
            item = SingerListItem(
                country=i['country'],
                singer_id=i['singer_id'],
                singer_mid=i['singer_mid'],
                singer_name=i['singer_name'],
                singer_pic=i['singer_pic']
            )
            yield item

        if cur_page * 80 < total:
            yield scrapy.Request(url=self.url.format(index=index), meta={
                'index': index,
                'cur_page': cur_page+1
            })
