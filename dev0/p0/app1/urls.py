# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from app1 import views

urlpatterns = patterns('',
    # ex: /app1/
    url(r'^$', views.index, name='index'),
    # ex: /app1/Paris/
    url(r'^(?P<city>\D+)/$', views.detail, name='detail'),
    # ex: /app1/Paris/results/
    url(r'^(?P<city>\D+)/results/$', views.results, name='results'),

)