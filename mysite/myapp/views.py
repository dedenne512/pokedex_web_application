from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Pokemon

# Create your views here.

# 初期アクセスページ
def index(request):
    return render(request, 'myapp/index.html')

def camera(request):
    return render(request, 'myapp/camera2.html')

# ポケモン一覧
def pokemon_list(request):
    list = Pokemon.objects.all().order_by('id')
    return render(
        request,
        'myapp/list.html',
        {'pokemon': list}
    )

def detail(request, id):
    poke_info = Pokemon.objects.get(id = id)
    return render(
        request,
        'myapp/detail.html',
        {
            'pokemon': poke_info
        }
    )

def config(request):
    return render(request, 'myapp/config.html')