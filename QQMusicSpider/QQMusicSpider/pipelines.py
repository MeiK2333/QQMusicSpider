from QQMusicSpider.models import get_session, Singer


class QqmusicspiderPipeline(object):
    def __init__(self):
        self.session = get_session()
        self.session_count = 0

    def process_item(self, item, spider):
        singer = Singer(**item)
        try:
            self.session.add(singer)
            if self.session_count % 10000 == 0:
                self.session.commit()
            self.session_count += 1
        except:
            self.session.rollback()
        return item

    def close_spider(self, spider):
        self.session.commit()
