# -*- coding:utf-8 -*-

from django.contrib import admin
from app0.models import Poll, Choice

# Pour plus de possibilités : Voir https://docs.djangoproject.com/en/1.6/intro/tutorial02/
admin.site.register(Poll)
admin.site.register(Choice)