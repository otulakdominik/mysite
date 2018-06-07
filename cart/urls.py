from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('send', views.send_order, name='send_order'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path(
        '^remove/<int:product_id>/',
        views.cart_remove,
        name='cart_remove'
    ),
]
