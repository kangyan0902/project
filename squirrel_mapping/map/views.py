from django.shortcuts import render
from django.http import Http404

from sighting.models import Squirrel

# Create your views here.

def map(request):
	squirrels = Squirrel.objects.all()[:100]
	context = {'squirrels': squirrels}
	return render(request, 'map/map.html', context)
