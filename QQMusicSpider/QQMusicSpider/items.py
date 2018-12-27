import scrapy


class QQMusicItem(scrapy.Item):
    item_type = scrapy.Field()
    data = scrapy.Field()
