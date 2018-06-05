from . import views
from django.urls import path
from django.conf.urls import include


app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list'),
    path('<slug:slug>', views.ArticleDetailView.as_view(), name='details'),
]
