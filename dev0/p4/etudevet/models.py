# -*- coding:utf-8 -*-

from django.db import models

class Ville(models.Model):

	nom_ville = models.CharField(max_length=60)
	id_ville = models.IntegerField()
	pop_ville = models.IntegerField()
	classt_pop_ville = models.IntegerField()
	
	departement = models.ForeignKey('Departement')
	region = models.ForeignKey('Region')

	def __unicode__(self):
		return self.nom_ville

class Animal(models.Model):
	#type: CN/CT
	type_al = models.CharField(max_length=3)
	nombre_al = models.IntegerField()
	nombre_med = models.IntegerField()
	# nombre total par calcul

	id_ville = models.ForeignKey('Ville')	

	def __unicode__(self):
		return self.type_al + " " + self.ville.nom_ville

class Depenses(models.Model):
	indice = models.IntegerField()
	depense_cn = models.IntegerField()
	depence_ct = models.IntegerField()

	id_ville = models.ForeignKey('Ville')	

	def __unicode__(self):
		return "Dépenses" + " " + self.ville.nom_ville


class Tops(models.Model):
	#type: population ou animal ou medical ou depense ou indice 
	type_top = models.CharField(max_length=60)
	#range: departement ou region ou France 
	range_top = models.CharField(max_length=60)
	#rank : classement de la ville dans le top !!
	rank_top =models.IntegerField()
	
	id_ville = models.ForeignKey('Ville')

	def __unicode__(self):
		return "Top" +" " + self.ville.nom_ville

class Region(models.Model):
	nom_region = models.IntegerField(max_length=60)

	def __unicode__(self):
		return self.nom_region

class Departement(models.Model):
	nom_departement = models.IntegerField(max_length=60)

	def __unicode__(self):
		return self.nom_departement