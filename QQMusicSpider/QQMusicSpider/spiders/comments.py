# -*- coding: utf-8 -*-
import json

import scrapy
# from scrapy_redis.spiders import RedisCrawlSpider

from QQMusicSpider.items import QQMusicItem
from QQMusicSpider.utils import MongoClient, comments_params


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['y.qq.com']
    # redis_key = 'comments:start_urls'

    def start_requests(self):
        cnt = int(getattr(self, 'cnt', 0))
        self.logger.info(f'获取第 {cnt} 项的评论')
        collections = MongoClient().qqmusic.toplist
        all_data = collections.find()
        item = all_data[cnt]
        # for item in all_data:
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
