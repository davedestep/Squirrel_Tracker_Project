from django.http import HttpResponse
from django.shortcuts import render
from .models import Sighting
from django.db.models import Count

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
        colors =set(Sighting.objects.all().values_list("primary_fur_color").annotate(frequency=Count("primary_fur_color")))
        daytime =set(Sighting.objects.all().values_list("shift").annotate(frequency=Count("shift")))
        squirrel_age =set(Sighting.objects.all().values_list("age").annotate(frequency=Count("age")))
        context = {
		'total_squirrels': total_squirrels,
                'colors': colors,
                'daytime':daytime,
                'squirrel_age':squirrel_age,
		}
        return render(request,'map/stats.html', context)

#View for updating? Will only be able to view with this
def get_squirrel(request, unique_squirrel_id):
    squirrel = Sighting.objects.get(id=unique_squirrel_id)
    return HttpResponse(f'Hello, my latitude is {squirrel.latitude}!')


