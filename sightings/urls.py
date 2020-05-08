from django.urls import path
from . import views

urlpatterns = [
        path('map/', views.home_view, name='home'),
        path('', views.list_squirrel_sightings, name='sqirrels'),
]

