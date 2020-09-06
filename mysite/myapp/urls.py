from django.urls import path

from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon_list/', views.pokemon_list, name='pokemon_list'),
    path('pokemon_list/detail/<int:id>/', views.detail, name='detail'),
    path('config/', views.config, name='config')
]