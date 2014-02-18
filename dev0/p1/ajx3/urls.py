# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from ajx3 import views

urlpatterns = patterns('',
    # ex: /ajx2/
    url(r'^$', views.articles),
    # ex: /ajx2/get/1/
    url(r'^get/(?P<article_id>\d+)/', views.article),

    url(r'^search/', views.search_titles),

)