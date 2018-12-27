# -*- coding: utf-8 -*-
import json

import pymongo
import scrapy

from QQMusicSpider.utils import comments_params
from QQMusicSpider.items import QQMusicItem


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['y.qq.com']

    def start_requests(self):
        collections = pymongo.MongoClient().qqmusic.toplist
        all_data = collections.find()
        for item in all_data:
            for jtem in item['songlist']:
                song_id = jtem['data']['songid']
                params = comments_params(song_id)
                yield scrapy.FormRequest(f'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg',
                                         method='GET',
                                         formdata=params,
                                         meta={
                                             'song_id': song_id,
                                             'item': jtem,
                                             'page_num': 0
                                         })

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        song_id = response.meta['song_id']
        page_num = response.meta['page_num']
        item = response.meta['item']
        total = data['comment']['commenttotal']

        # 判断是否全部获取完
        if page_num * 25 + 25 < total:
            yield scrapy.FormRequest(f'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg',
                                     method='GET',
                                     formdata=comments_params(
                                         song_id, page_num+1),
                                     meta={
                                         'song_id': song_id,
                                         'item': item,
                                         'page_num': page_num + 1
                                     })

        for comment in data['comment']['commentlist']:
            qitem = QQMusicItem()
            qitem['item_type'] = 'comments'
            comment['songid'] = song_id
            qitem['data'] = comment
            yield qitem
