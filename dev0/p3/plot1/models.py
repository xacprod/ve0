# -*- coding:utf-8 -*-

from django.db import models

class Plot1(models.Model):
	title = models.CharField(max_length=40)
	x_plot = models.IntegerField()
	y_plot = models.IntegerField()

	def __unicode__(self):
		return self.title



#http://pydoc.net/Python/django-richtemplates/0.3.8/example_project.examples.views.jqplot/
