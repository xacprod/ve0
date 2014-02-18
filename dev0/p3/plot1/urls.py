# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from plot1 import views

urlpatterns = patterns('',

    url(r'^$', views.plot),

)