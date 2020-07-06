from django.urls import path
from . import views

urlpatternd = [
		path('', views.index, name='index'),
]