from . import views
from django.urls import path


urlpatterns = [
    path('', views.EntryListView.as_view(), name='list'),
]
