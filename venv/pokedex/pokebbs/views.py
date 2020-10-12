from django.shortcuts import render
from django.http import HttpResponse
from .models import PokeArticle

#HTMLファイル参照設定 + データ受け渡し設定

#test
def test(request):
	articles = PokeArticle.objects.all()
	context = {
			'message': 'ポケモン図鑑リスト',
			'articles': articles,
			}
	return render(request, 'pokebbs/test.html', context)

#index
def index(request):
    return render(request, 'pokebbs/index.html')
	
#camera
def camera(request):
    return render(request, 'pokebbs/camera2.html')
	
# ポケモン一覧
def pokemon_list(request):
    list = PokeArticle.objects.all().order_by('id')
    return render(
        request,
        'pokebbs/list.html',
        {'pokemon': list}
    )


#detail
def detail(request, id):
    poke_info = PokeArticle.objects.get(id = id)
    return render(
        request,
        'pokebbs/detail.html',
        {'pokemon': poke_info}
    )

#config
def config(request):
    return render(request, 'pokebbs/config.html')
# Create your views here.
