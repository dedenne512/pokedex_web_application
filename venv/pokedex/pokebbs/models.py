from django.db import models

# Create your models here.
class PokeArticle(models.Model):

	#番号
	Number = models.IntegerField(primary_key=True)
	#？？ポケモン
	Pokerace = models.CharField(max_length=30)
	#ポケモン名
	Pokename = models.CharField(max_length=30)
	#高さ
	Pokeheight = models.CharField(max_length=30)
	#重さ
	Pokeweight = models.CharField(max_length=30)
	#説明文
	Pokeexp = models.CharField(max_length=2000)
	
	def __str__(self):
		return self.Pokename