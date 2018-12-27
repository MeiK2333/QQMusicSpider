import pymongo


class QQMisicSpiderPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.qqmusic

    def process_item(self, item, spider):
        if item.get('item_type') == 'toplist':
            self.toplist_item(item, spider)
        elif item.get('item_type') == 'comments':
            self.comments_item(item, spider)

    def toplist_item(self, item, spider):
        collections = self.db.toplist
        collections.update_one({
            'rank_type_value': item['data']['rank_type_value'],
            'update_time': item['data']['update_time']
        }, {'$set': item['data']}, upsert=True)

    def comments_item(self, item, spider):
        collections = self.db.comments
        collections.update_one({
            'songid': item['data']['songid'],
            'commentid': item['data']['commentid']
        }, {'$set': item['data']}, upsert=True)

    def close_spider(self, spider):
        self.client.close()
