"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views
from .admin import login_as_user

app_name = 'mysite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls', namespace='entry')),
    path('articles/', include('articles.urls', namespace='article')),
    path('products/', include('products.urls', namespace='product')),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^login/user/(?P<user_id>[\d_]+)$', login_as_user),
    path('search/', include('haystack.urls')),
]
