#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from models import Article



def articles(request):
	articles = Article.objects.all()
	context = {'articles':articles}
	return render (request, 'ajx1/articles.html', context)



def article(request, article_id):
	article = get_object_or_404 (Article, pk=article_id)
	return render (request, 'ajx1/article.html', {'article': article})



def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(title__contains = search_text)
	return render(request,'ajx1/ajax_search.html', {'articles' : articles})
