from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('', views.home_view, name = 'home'),
	#path('sightings/', views.list_squirrel_sightings),
	#path('stats/', views.squirrel_stats),
	# path('sightings/<squirrel_id>/', views.update),
	# path('sightings/add/', views.add_sighting),
	
]
