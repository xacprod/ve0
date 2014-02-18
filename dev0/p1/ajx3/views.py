#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def home(request):
	return render_to_response('base3.html', context_instance=RequestContext(request))

def test_get(request):
	message = request.GET.get('message', '')
	if message == None or message == "":
		message = 'Aucun message transmis'
	return HttpResponse("Message : "+message)
	
def test_post(request):
	nom = request.POST.get('nom', '')
	if nom == None or nom == "":
		nom = 'Inconnu'
	prenom = request.POST.get('prenom', '')
	if prenom == None or prenom == "":
		prenom = 'Inconnu'
	return HttpResponse("Nom : "+nom+"<br/>Prenom : "+prenom)