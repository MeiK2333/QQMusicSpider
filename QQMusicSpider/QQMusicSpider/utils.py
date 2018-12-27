from enum import Enum


class RankType(Enum):
    巅峰榜_欧美 = 3
    巅峰榜_流行指数 = 4
    巅峰榜_内地 = 5
    巅峰榜_港台 = 6
    巅峰榜_韩国 = 16
    巅峰榜_日本 = 17
    巅峰榜_热歌 = 26
    巅峰榜_新歌 = 27
    巅峰榜_网络歌曲 = 28
    巅峰榜_影视金曲 = 29
    巅峰榜_K歌金曲 = 36
    巅峰榜_腾讯音乐人原创榜 = 52
    说唱榜 = 58
    台湾Hito中文榜 = 103
    日本公信榜 = 105
    韩国Mnet榜 = 106
    英国UK榜 = 107
    美国公告牌榜 = 108
    香港电台榜 = 113
    香港商台榜 = 114
    美国iTunes榜 = 123


def comments_params(song_id, page_num=0, page_size=25):
    params = {
        'format': 'json',
        'reqtype': '2',
        'biztype': '1',
        'topid': str(song_id),
        'cmd': '8',
        'pagenum': str(page_num),
        'pagesize': str(page_size)
    }
    return params
