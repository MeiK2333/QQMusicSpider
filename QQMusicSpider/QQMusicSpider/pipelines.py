import pymongo


class QQMisicSpiderPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.qqmusic

    def process_item(self, item, spider):
        if item.get('item_type') == 'toplist':
            self.toplist_item(item, spider)

    def toplist_item(self, item, spider):
        collections = self.db.toplist
        collections.insert_one(item['data'])

    def close_spider(self, spider):
        pass
