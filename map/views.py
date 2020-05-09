from django.http import HttpResponse
from django.shortcuts import render
from .models import Sighting

# Create your views here.
def index(request):
	return render(request, 'map/map.html', {"sightings": Sighting.objects.all()[:50]})


#view for home page
def home_view(request):
	return render(request, 'map/home.html', {'title': 'Home'})

#View for sightings
def list_squirrel_sightings(request):
    squirrels = Sighting.objects.all()
    return render(request,'map/lists.html', context)


