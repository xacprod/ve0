# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from plot3 import views

urlpatterns = patterns('',

    url(r'^$', views.barchart1),

)