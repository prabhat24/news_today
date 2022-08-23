import requests
from datetime import datetime as dt

from news.models import News

urls = ["https://timesofindia.indiatimes.com/rssfeeds/-2128839596.cms?feedtype=sjson", 
        "https://timesofindia.indiatimes.com/rssfeeds/6547154.cms?feedtype=sjson"
        "https://timesofindia.indiatimes.com/rssfeeds/-2128838597.cms?feedtype=sjson"]


def create_toi_news():
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.json()
            if isinstance(content, dict):
                content = content.get('channel')['item']
                for c in content:
                    try:
                        news, created = News.objects.get_or_create(article_src_link=c.get('link'))
                        if created:
                            news.heading = c.get('title', None)
                            news.body = c.get('description', None).split(">")[-1]
                            news.publisher = "TOI"
                            news.published_date = dt.strptime(c.get('pubDate', None).split("+")[0], "%Y-%m-%dT%H:%M:%S")
                            news.save()
                    except Exception as e:
                        print(e)
                        continue


