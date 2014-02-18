#-*- coding:utf-8 -*-

from django.shortcuts import render,get_object_or_404
from django.utils import simplejson 
import json
# Pour passer des mots en JS http://stackoverflow.com/questions/12174494/passing-unicode-strings-from-django-to-javascript

from plot3.models import Animal, City 



# ATTENTION MULTICHARTS = > MULTI VIEWS => ORGANISATION POUR AVOIR TOUT EN UNE FOIS

#def send_object(request): #Envoi d'un objet directement dans le template

	#Technique 1(Pas d'utilisation de cette technique mais ça fonctionne aussi)
	#dogs_number = get_object_or_404(Animal, pk=1).number_total
	
	#Technique 2
	#dogs = get_object_or_404(Animal, pk=1)
	#return render (request, 'plot3/plot_page.html', {"dogs" : dogs}) 
	# L'objet est envoyé et peux être travaillé du template



def barchart1(request):

	dog_array = []
	city_array =[]
	for i in [1,Animal.objects.count()]:
		objet = get_object_or_404(Animal, pk=i)
		
		dogs = [objet.number_total,objet.number_medical]
		dog_array.append(dogs)

		cities = [objet.city.city_name]
		city_array.append(cities)
	
	json_cities = json.dumps(city_array)

	return render (request, 'plot3/plot_page.html', 
		{"dog_array" : dog_array,"city_array" : json_cities}) 
