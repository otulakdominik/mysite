from . import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path(
        '<int:id>/<slug:slug>/',
        views.product_detail,
        name='details'
    ),
]