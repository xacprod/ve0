# -*- coding:utf-8 -*-

from django.forms import ModelForm
from etudevet.models import ContactMessage, CategorieMessage

class ContactForm(ModelForm):
	class Meta:
		model = ContactMessage
		fields ={'form_type', 'prenom', 'nom', 'mail', 'title', 'message'}
