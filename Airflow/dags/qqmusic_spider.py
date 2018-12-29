from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email': ['meik2333+airflow@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'qqmusic_spider',
    default_args=default_args,
    description='爬取排行榜',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='toplist',
    bash_command='source ~/QQMusicSpider/venv/bin/activate && cd ~/QQMusicSpider/QQMusicSpider && scrapy crawl toplist',
    dag=dag,
)

t1.doc_md = """\
**获取排行榜**
"""

dag.doc_md = __doc__

t2 = BashOperator(
    task_id='comments_0',
    depends_on_past=False,
    bash_command='source ~/QQMusicSpider/venv/bin/activate && cd ~/QQMusicSpider/QQMusicSpider && scrapy crawl comments -a cnt=0',
    dag=dag,
)

t2.doc_md = """\
**获取评论 0**
"""

t3 = BashOperator(
    task_id='comments_1',
    depends_on_past=False,
    bash_command='source ~/QQMusicSpider/venv/bin/activate && cd ~/QQMusicSpider/QQMusicSpider && scrapy crawl comments -a cnt=1',
    dag=dag,
)

t3.doc_md = """\
**获取评论 1**
"""

t4 = BashOperator(
    task_id='comments_2',
    depends_on_past=False,
    bash_command='source ~/QQMusicSpider/venv/bin/activate && cd ~/QQMusicSpider/QQMusicSpider && scrapy crawl comments -a cnt=2',
    dag=dag,
)

t4.doc_md = """\
**获取评论 2**
"""

t1 >> [t2, t3, t4]
