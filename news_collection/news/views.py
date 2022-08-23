from django.db.models import query
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from elasticsearch_dsl import Q

from .documents import NewsDocument
from .serializers import NewsSerializer


class NewsListView(APIView, LimitOffsetPagination):
    search_document = NewsDocument
    serializer = NewsSerializer

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    'heading',
                    'body'
                ]
            )
            search = self.search_document.search().query(q)
            response = search.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(e, status=500)
        