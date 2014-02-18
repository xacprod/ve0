#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p1.views.home', name='home'),
    url(r'^ajx1/', include('ajx1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.defaults import patterns, include, url
from ajx3.views import home, test_get, test_post


urlpatterns += patterns('',
	url(r'^ajx3$', home, name='home'),
	url(r'^ajx3/home/$', home, name='home2'),
	url(r'^ajx3/test-get/$', test_get, name='testget'),
	url(r'^ajx3/test-post/$', test_post, name='testpost'),
)