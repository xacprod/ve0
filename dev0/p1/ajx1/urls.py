# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from ajx1 import views

urlpatterns = patterns('',
    # ex: /ajx1/
    url(r'^$', views.articles),
    # ex: /ajx1/get/1/
    url(r'^get/(?P<article_id>\d+)/', views.article),

    url(r'^search/', views.search_titles),

)