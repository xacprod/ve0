# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from app0 import views

urlpatterns = patterns('',
    # ex: /app0/
    url(r'^$', views.index, name='index'),
    # ex: /app0/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /app0/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /app0/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)