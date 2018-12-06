"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import re
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path('admin/', admin.site.urls, name='hoge'),
    path('top/', include('top.urls')),
    path('posts/', include('posts.urls')),
    re_path(r'\w*',  RedirectView.as_view(url='/top/'), name='redirect_to_index'),

    #path(r'^$', RedirectView.as_view(url='/index/'), name='redirect_to_index'),
    #url(r'^$', RedirectView.as_view(url='/index/'), name='redirect_to_index')
]