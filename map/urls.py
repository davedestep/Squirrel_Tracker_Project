from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('', views.home_view, name = 'home'),
	path('squirrels/', views.list_squirrel_sightings),

]
