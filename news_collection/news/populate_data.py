from elasticsearch import Elasticsearch
from django.conf import settings
from .utils import *


HOST = "http://{DOMAIN_NAME}:{PORT}".format(DOMAIN_NAME=settings.ELASTIC_SEARCH["HOST"],
        PORT=settings.ELASTIC_SEARCH["PORT"])

es = Elasticsearch(host=HOST)

class ElasticsearchHandler:

    def __init__(self):
        self.connection = Elasticsearch(host=HOST)


    def check_and_create_index(self, index: str, news):
        mappings = news.get_dict()
        if not self.connection.indices.exists(index):
            self.connection.indices.create(index=index, body=mappings, ignore=400)


def populate():
    es = ElasticsearchHandler()
    from news.news_scrappers.toi_news_feed import get_toi_news_feeds
    all_feeds = get_toi_news_feeds()
    for news in all_feeds:
        es.check_and_create_index("TOI_NEWS_FEEDS", news)
