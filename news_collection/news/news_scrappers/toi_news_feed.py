import requests
import json
import uuid
from datetime import datetime as dt

urls = ["https://timesofindia.indiatimes.com/rssfeeds/-2128839596.cms?feedtype=sjson", 
        "https://timesofindia.indiatimes.com/rssfeeds/6547154.cms?feedtype=sjson"
        "https://timesofindia.indiatimes.com/rssfeeds/-2128838597.cms?feedtype=sjson"]


class TOIFeed(News):


    def create_news(self, single_feed):
        self.heading = single_feed.get('title', None)
        self.body = single_feed.get('description', None).split(">")[-1]
        self.article_src_link = single_feed.get('link', None)
        self.published_date = dt.strptime(single_feed.get('pubDate', None).split("+")[0], "%Y-%m-%dT%H:%M:%S")
        self.publisher = "TOI"



def get_toi_news_feeds():
    all_news = []
    for url in urls:
        response = requests.get(url).json()
        content = response.get('channel')['item']
        for c in content:
            news = TOIFeed()
            news.create_news(c)
            all_news.append(news)
    return all_news

