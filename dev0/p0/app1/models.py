# -*- coding:utf-8 -*-

from django.db import models

class City(models.Model):
    ville = models.CharField(max_length=40)
    nombre = models.IntegerField()

    def __unicode__(self):  # Python 3: def __str__(self):
	        return self.ville

