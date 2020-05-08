from django.http import HttpResponse
from django.shortcuts import render
from .models import Sighting

# Create your views here.
def index(request):
	#return HttpResponse('Welcome to the NYC Squirrel Tracker')
	return render(request, 'map/map.html', {"sightings": Sighting.objects.all()[:50]})


