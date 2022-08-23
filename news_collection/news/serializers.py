from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = [
                "id", 
                "heading", 
                "body", 
                "author", 
                "article_src_link"
            ]
        read_only = True