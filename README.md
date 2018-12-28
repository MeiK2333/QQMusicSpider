# QQMusicSpider

QQ Music Spider

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

## TODO

- 分布式爬虫
- Airflow 任务调度
- 分布式数据处理与分析
