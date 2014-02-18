# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from app1.models import City


def index(request):
    city_list = City.objects.all().order_by('-ville')[:5]
    context = {'city_list': city_list}
    return render(request, 'app1/index.html', context)

def detail(request, city):
    city = get_object_or_404(City, ville=city)
    return render(request, 'app1/detail.html', {'city': city})

def results(request, poll_id):
   pass

   """ poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'app1/results.html', {'poll': poll})
"""
def vote(request, poll_id):
    pass
"""    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'app1/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app1:results', args=(p.id,)))
        """