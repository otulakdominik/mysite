from . import views
from django.urls import path


app_name = 'blog'

urlpatterns = [
    path('', views.EntryListView.as_view(), name='list'),
    path('blog/<slug:slug>', views.EntryDetailView.as_view(), name='details'),
]
