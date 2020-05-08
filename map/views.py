from django.http import HttpResponse
from django.shortcuts import render
from .models import Sighting

# Create your views here.
def index(request):
	#return HttpResponse('Welcome to the NYC Squirrel Tracker')
	return render(request, 'map/map.html', {"sightings": Sighting.objects.all()[:50]})


#view for home page
def home_view(request):
	return render(request, 'map/home.html', {'title': 'Home'})

	#return HttpResponse('Welcome to Squirrel Tracker')