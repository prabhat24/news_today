from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import News

@registry.register_document
class NewsDocument(Document):

    class Index:
        name = "news"

    class Django:
        model = News

        fields = [
                "id", 
                "heading", 
                "body", 
                "author", 
                "article_src_link"
            ]