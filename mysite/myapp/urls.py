from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="myapp/login.html"), name='login'),
    path('camera/', views.camera, name='camera'),
    path('pokemon_list/', views.pokemon_list, name='pokemon_list'),
    path('pokemon_list/detail/<int:id>/', views.detail, name='detail'),
    path('config/', views.config, name='config'),
    path('oauth/', include('social_django.urls', namespace='social')),
]