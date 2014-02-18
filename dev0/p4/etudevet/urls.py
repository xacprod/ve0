# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from etudevet import views

urlpatterns = patterns('',

    url(r'^$', views.home, name = "home"),
    url(r'^home2$', views.home2, name = "home2"),
    url(r'^home3$', views.home3, name = "home3"),
    url(r'^search/$', views.search_city),
    url(r'^display/(?P<ville_id>\d+)/$', views.display_city, name = "display" ),
)