# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p0.views.home', name='home'),
    url(r'^app0/', include('app0.urls', namespace = 'app0')),
    url(r'^app1/', include('app1.urls', namespace = 'app1')),
    url(r'^app2/', include('app2.urls', namespace = 'app2')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

