from django.db import models

# Create your models here.
class PokeArticle(models.Model):
    number = models.IntegerField('図鑑ナンバー')
    name_jpn = models.CharField('名前', max_length=255)
    name_eng = models.CharField('名前(英語)', max_length=255)
    classification = models.CharField('分類', max_length=255)
    type1 = models.CharField('タイプ1', max_length=255)
    type2 = models.CharField('タイプ2', null=True, max_length=255)
    height = models.DecimalField('高さ', max_digits=4, decimal_places=1)
    weight = models.DecimalField('重さ', max_digits=4, decimal_places=1)
    ability1 = models.CharField('特性1', max_length=255)
    ability2 = models.CharField('特性2', null=True, max_length=255)
    hidden_ability = models.CharField('夢特性', null=True, max_length=255)
    detail = models.TextField('図鑑説明', max_length=500)
    image = models.FilePathField('画像', path='pokebbs/static/pokebbs/images')
    voice = models.FilePathField('音声', path='pokebbs/static/pokebbs/voices')

    def __str__(self):
        return self.name_jpn