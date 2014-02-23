# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
 
from todolist import views

urlpatterns = patterns('',

    url(r'^$', views.index),
	
    url(r'^add/$', views.add),
	url(r'^remove/(?P<task_id>\d+)/$', views.remove),
)
