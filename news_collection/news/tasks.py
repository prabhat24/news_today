from celery import shared_task
from news.news_scrappers.toi_news_feed import create_toi_news

@shared_task
def get_news():
    create_toi_news()
    

