#-*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from etudevet.forms import ContactForm
from etudevet.models import Ville, Animal, Departement, Region, Tops, Depenses, ContactMessage, CategorieMessage
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()


            #ALERT ALERT ALERT


            confirmation = "Message envoyé"
            send_mail('Subject here', 'Here is the message.', 'x.carbonel@gmail.com',
    ['x.carbonel@gmail.com'], fail_silently=False)
            return render(request, 'etudevet/base.html', locals())
    else:
        form = ContactForm() # An unbound form

    return render(request, 'etudevet/contact.html', {'form': form})





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



def display_city(request):
	if request.method == "POST":
		city_to_display = request.POST['city_to_display']
	else:
		city_to_display = ''

	city_chosen = get_object_or_404(Ville,pk = city_to_display )
	animals_chosen = city_chosen.animal_set.all()

	return render(request,'etudevet/city_display.html', 
		{'city_chosen' : city_chosen, 'animals': animals_chosen}
		)


def base(request):
	return render (request,'etudevet/base.html')

def pricing(request):
	return render (request,'etudevet/pricing.html')


def mon_etude1(request):
	return render (request,'etudevet/mon_etude1.html')
def mon_etude2(request):
	return render (request,'etudevet/mon_etude2.html')
def mon_etude3(request):
	return render (request,'etudevet/mon_etude3.html')


def infos1(request):
	return render (request,'etudevet/infos1.html')
def infos2(request):
	return render (request,'etudevet/infos2.html')
def infos3(request):
	return render (request,'etudevet/infos3.html')
def infos4(request):
	return render (request,'etudevet/infos4.html')

def order1(request):
	return render (request,'etudevet/order1.html')