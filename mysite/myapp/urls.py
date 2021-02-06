from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="myapp/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('camera/', views.camera, name='camera'),
    path('pokemon_list/', views.pokemon_list, name='pokemon_list'),
    path('pokemon_list/detail/<int:id>/', views.detail, name='detail'),
    path('config/', views.config, name='config'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('select/', views.select, name='select'),
    path("predict/", views.predict, name="predict"),
    path('save/', views.save, name='save'),
    path('delete/<int:id>/', views.delete, name='delete')
]