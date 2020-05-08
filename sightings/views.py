from django.shortcuts import render

from map.models import Sighting
from django.http import HttpResponse

# Create your views here.


# Create your views here.

#view for home page Do we need this here to or just in map.views?
###############################################################
def home_view(request):
	return render(request, 'map/home.html', {'title': 'Home'})
###############################################################


#view of list of sightings with links to edit each

def list_squirrel_sightings(request):
    squirrels = Sqighting.objects.all()
    return render(request,'sightings/list.html', context, {'squirrels': squirrels})



#view to update a particular sighting


#a view to create a new sighting --> forms.py


#view with general stats about the sightings
