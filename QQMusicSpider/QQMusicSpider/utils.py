import json
import math


def qqmusic_dict_to_url_params(data):
    return json.dumps(data).replace(' ', '')


def qqmusic_singer_list_url_args_index_and_page(index, page):
    data = {
        "singerList": {
            "module": "Music.SingerListServer",
            "method": "get_singer_list",
            "param": {
                "area": -100,
                "sex": -100,
                "genre": -100,
                "index": index,
                "sin": 80 * page,
            }
        }
    }
    return f'https://u.y.qq.com/cgi-bin/musicu.fcg?data={qqmusic_dict_to_url_params(data)}'


def qqmusic_singer_index_all_url(index, total):
    page_size = math.ceil(total / 80)
    return [qqmusic_singer_list_url_args_index_and_page(index, i) for i in range(page_size)]
