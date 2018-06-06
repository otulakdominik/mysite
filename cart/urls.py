from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('send', views.send_order, name='send_order'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(
        r'^remove/(?P<product_id>\d+)/$',
        views.cart_remove,
        name='cart_remove'
    ),
]
