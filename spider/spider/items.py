# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SingerListItem(scrapy.Item):
    country = scrapy.Field()
    singer_id = scrapy.Field()
    singer_mid = scrapy.Field()
    singer_name = scrapy.Field()
    singer_pic = scrapy.Field()


class TopListItem(scrapy.Item):
    rank_name = scrapy.Field()
    rank_value = scrapy.Field()
    albumdesc = scrapy.Field()
    albumid = scrapy.Field()
    albummid = scrapy.Field()
    albumname = scrapy.Field()
    alertid = scrapy.Field()
    belongCD = scrapy.Field()
    cdIdx = scrapy.Field()
    interval = scrapy.Field()
    isonly = scrapy.Field()
    label = scrapy.Field()
    msgid = scrapy.Field()
    pay = scrapy.Field()
    preview = scrapy.Field()
    rate = scrapy.Field()
    singer = scrapy.Field()
    size5_1 = scrapy.Field()
    size128 = scrapy.Field()
    size320 = scrapy.Field()
    sizeape = scrapy.Field()
    sizeflac = scrapy.Field()
    sizeogg = scrapy.Field()
    songid = scrapy.Field()
    songmid = scrapy.Field()
    songname = scrapy.Field()
    songorig = scrapy.Field()
    songtype = scrapy.Field()
    strMediaMid = scrapy.Field()
    stream = scrapy.Field()
    switch = scrapy.Field()
    type_ = scrapy.Field()
    vid = scrapy.Field()
    in_count = scrapy.Field()
    old_count = scrapy.Field()
