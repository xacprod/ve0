# -*- coding:utf-8 -*-

from django.db import models
 
class Task(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name	   = models.CharField(max_length=256)
	completed  = models.BooleanField(default=False)