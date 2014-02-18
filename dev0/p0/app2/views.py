# -*- coding:utf-8 -*-
from django.shortcuts import  render
from django.forms import ModelForm
from app2.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact


def contact(request):

    contact_form = ContactForm()
    return render (request,'app2/contact.html', {'contact_form' : contact_form})