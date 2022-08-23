from django.conf.urls import url 
from news import views


urlpatterns = [
    url(r'^list/$', views.NewListView.as_view(), name='news_list'),
]