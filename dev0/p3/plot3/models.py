# -*- coding:utf-8 -*-

from django.db import models

class Animal(models.Model):

	animal_type = models.CharField(max_length=15)
	number_total =models.IntegerField()
	number_medical =models.IntegerField()
	expense =models.IntegerField()

	city = models.ForeignKey('City')

	def __unicode__(self):
		return self.animal_type


class City(models.Model):

	city_name = models.CharField(max_length=80)

	def __unicode__(self):
		return self.city_name

