# QQMusicSpider

QQ Music Spider

## Require

- Python 3.6 or higher

## Usage

```bash
# 创建并切换虚拟环境
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 设置远程 redis 与 mongodb（如果使用本地的可以不设置）
export REDIS_URL='redis://user:pass@host:port'
export MONGO_URL='mongodb://user:pass@host:port'

cd QQMusicSpider/
scrapy crawl toplist  # 爬取排行榜
scrapy crawl comments  # 爬取评论
```

注意：为了提高性能，请对 `qqmusic.comments` 建立联合索引 `{'commentid': 1, 'songid': 1}`

## TODO

- Airflow 任务调度
- 分布式数据处理与分析
- 发现了个很狗的问题：数据量太大了。。。。。。MongoDB 根本存不下，考虑更新存储方式
