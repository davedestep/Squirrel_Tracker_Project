from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('', views.home_view, name = 'home'),
	path('sightings/', views.list_squirrel_sightings),
	path('stats/', views.squirrel_stats),
	path('<int:unique_squirrel_id>/', views.get_squirrel),
]
