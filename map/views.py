from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sighting
from django.db.models import Count

from .forms import SightingUpdateForm

# Create your views here.
def index(request):
	context = {
		"sightings": Sighting.objects.all()[:50],
		}
	return render(request, 'map/map.html', context)


#view for home page
def home_view(request):
	context = {
		'title': 'Home',
		}
	return render(request, 'map/home.html', context)

#View for sightings
def list_squirrel_sightings(request):
	squirrels = Sighting.objects.all()
	context = {
		'squirrels': squirrels, 
		}
	return render(request,'map/lists.html', context)

#View for updating a sighting
def update(request, squirrel_id):
	sighting = Sighting.objects.get(unique_squirrel_id=squirrel_id)
	if request.method == 'POST':
		form = SightingUpdateForm(request.POST, instance = sighting)
		if form.is_valid():
			form.save()
	else:
		form = SightingUpdateForm(instance=sighting)

	context = {
		'form': form,
		}

	return render(request, 'map/update.html', context)


#View to add a sighting
def add_sighting(request):
	if request.method == 'POST':
		form = SightingUpdateForm(request.POST)
		if form.is_valid():
			new_squirrel_id = form['unique_squirrel_id'].value()
			form.save()
			return redirect('f/sightings/{new_squirrel_id}/')
	else:
		form = SightingUpdateForm()

	context = {
		'form': form,
		}

	return render(request, 'map/add_sighting.html', context)


#View for stats
def squirrel_stats(request):
        total_squirrels = Sighting.objects.all().count
        colors =set(Sighting.objects.all().values_list("primary_fur_color").annotate(frequency=Count("primary_fur_color")))
        daytime =set(Sighting.objects.all().values_list("shift").annotate(frequency=Count("shift")))
        squirrel_age =set(Sighting.objects.all().values_list("age").annotate(frequency=Count("age")))

        squirrel_location =set(Sighting.objects.all().values_list("location").annotate(frequency=Count("location")))
        context = {
		'total_squirrels': total_squirrels,
                'colors': colors,
                'daytime':daytime,
                'squirrel_age':squirrel_age,
                'squirrel_location':squirrel_location,
		}
        return render(request,'map/stats.html', context)

# #View for updating? Will only be able to view with this
# def get_squirrel(request, unique_squirrel_id):
#     squirrel = Sighting.objects.get(id=unique_squirrel_id)
#     return HttpResponse(f'Hello, my latitude is {squirrel.latitude}!')


