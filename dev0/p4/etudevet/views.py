#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404

from etudevet.models import Ville

def home(request):

	data = Ville.objects.all()
	return render (request, 'etudevet/home.html', {"data" : data})


def home2(request):

	data = request.POST['ville_choisie']
	return render (request, 'etudevet/home2.html', {"data" : data})

def home3(request, pk_ville): #named ville.id in the template - but to avoid confusion with Insee id

	data = get_object_or_404(Ville, pk=pk_ville)
	return render (request, 'etudevet/home3.html', {"data" : data})


def search_city(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''

	villes_possibles = Ville.objects.filter(nom_ville__contains = search_text)
	return render(request,'etudevet/city_search.html', {'villes_possibles' : villes_possibles})



def display_city(request, ville_id): 

	data_ville = get_object_or_404(Ville, pk=ville_id)
	return render (request, 'etudevet/city_display.html', {"data_ville" : data_ville})