from django.conf.urls import url 
from news import views


urlpatterns = [
    url(r'^list/(?P<query>[\w-]+)/$', views.NewsListView.as_view(), name='news_list'),
]