from django.urls import path
from . import views


urlpatterns = [
	path('', views.test, name='test'),
	path('index/', views.index, name='index'),
    path('camera/', views.camera, name='camera'),
    path('pokemon_list/', views.pokemon_list, name='pokemon_list'),
    path('pokemon_list/detail/<int:id>/', views.detail, name='detail'),
    path('config/', views.config, name='config')
]