# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from etudevet import views

urlpatterns = patterns('',

    url(r'^$', views.home, name = "home"),
    url(r'^home2$', views.home2, name = "home2"),
    url(r'^home3$', views.home3, name = "home3"),
    url(r'^search/$', views.search_city),
    url(r'^display/$', views.display_city, name = "display" ),
    url(r'^base/$', views.base, name = "base" ),
    url(r'^pricing/$', views.pricing, name = "pricing" ),
    url(r'^mon_etude1/$', views.mon_etude1, name = "mon_etude1" ),
    url(r'^mon_etude2/$', views.mon_etude2, name = "mon_etude2" ),
    url(r'^mon_etude3/$', views.mon_etude3, name = "mon_etude3" ),
    url(r'^infos1/$', views.infos1, name = "infos1" ),
    url(r'^infos2/$', views.infos2, name = "infos2" ),
    url(r'^infos3/$', views.infos3, name = "infos3" ),
    url(r'^infos4/$', views.infos4, name = "infos4" ),
    url(r'^contact/$', views.contact, name = "contact" ),
    url(r'^order1/$', views.order1, name = "order1" ),
)