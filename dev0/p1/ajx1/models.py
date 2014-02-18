# -*- coding:utf-8 -*-

from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=40)
	content = models.CharField(max_length=250)

	def __unicode__(self):
		return self.title

