# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from app2 import views

urlpatterns = patterns('',

    url(r'^$', views.contact, name='contact'),
)