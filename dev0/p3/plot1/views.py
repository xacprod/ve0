#-*- coding:utf-8 -*-

from django.shortcuts import render,get_object_or_404


def plot(request):

	#GET Title
	graph_data1 =[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]
	graph_data2 =[[1,45],[2,23],[3,89]]
	return render (request, 'plot1/plot_page.html', {"graph_data1" : graph_data1,
													"graph_data2" : graph_data2
													})


