from django.shortcuts import render
from django.http import HttpResponse

#HTMLファイル参照設定 + データ受け渡し設定
def index(request):
	context = {
			'message': '三匹の中から好きなポケモンを選んでね',
			'pokemons':['ヒトカゲ','ゼニガメ','フシギダネ']
			}
	return render(request, 'pokebbs/index.html', context)

# Create your views here.
