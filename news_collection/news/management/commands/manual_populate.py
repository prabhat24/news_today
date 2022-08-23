import datetime
import logging
import random
from collections import deque
from django.core.management import BaseCommand

from news.news_scrappers.toi_news_feed import create_toi_news

logger = logging.getLogger('django')


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_toi_news()
