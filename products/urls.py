from . import views
from django.urls import path, re_path

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    re_path(
        r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='details'
    ),
]
