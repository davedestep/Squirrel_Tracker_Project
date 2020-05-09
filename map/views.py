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
	context = {
		'squirrels': squirrels, 
		}
	return render(request,'map/lists.html', context)

#View for stats
def squirrel_stats(request):
	total_squirrels = Sighting.objects.all().count
        colors = Sighting.objects.all().annotate(frequency=Count("primary_fur_color"))
        
	context = {
		'total_squirrels': total_squirrels, 
                'colors': colors,
		}
	return render(request,'map/stats.html', context)
