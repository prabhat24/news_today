import uuid
from django.db import models

# Create your models here.

class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading = models.CharField(max_length=500)
    body = models.TextField(max_length=500)
    article_src_link = models.URLField(max_length=1000, unique=True)
    author = models.CharField(max_length=500)
    publisher = models.CharField(max_length=200, null=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.article_src_link)

