# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
 
from todolist import views


urlpatterns = patterns('',

    url(r'^todolist/', include('todolist.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
