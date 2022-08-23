import datetime
import logging
import random
from collections import deque
from django.core.management import BaseCommand

from news.populate_data import populate

logger = logging.getLogger('django')


class Command(BaseCommand):

    def handle(self, *args, **options):
        populate()
