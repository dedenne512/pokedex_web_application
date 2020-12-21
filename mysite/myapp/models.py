from django.db import models
import numpy as np
import keras, sys
import tensorflow.compat.v1 as tf
from keras.models import load_model
from PIL import Image
import io, base64
# from cloudinary.models import CloudinaryField

# Create your models here.
graph = tf.get_default_graph()
class PredictedImage(models.Model):
    image = models.ImageField(upload_to="images")

    IMAGE_SIZE = 64 #画像サイズ
    MODEL_PATH="./myapp/ml_models/cnn.h5"
    classes = ["Blastoise", "Bulbasaur", "Charizard", "Charmander", "Charmeleon", "Diglett", "Dragonite", "Eevee", "Flareon", "Ivysaur", "Jolteon", "Magikarp", "Pidgey", "Pikachu", "Snorlax", "Squirtle", "Vaporeon", "Venusaur", "Vulpix", "Wartortle"]
    num_classes = len(classes)

    def predict(self):
        model = None
        global graph # 毎回同じモデルのセッションに投入して推論可能にする。
        with graph.as_default():
            model = load_model(self.MODEL_PATH)

            img_data = self.image.read()
            img_bin = io.BytesIO(img_data)

            image = Image.open(img_bin)
            image = image.convert("RGB")
            image = image.resize((self.IMAGE_SIZE,self.IMAGE_SIZE))
            data = np.asarray(image) / 255.0
            X = []
            X.append(data)
            X = np.array(X)

            result = model.predict([X])[0]
            predicted = result.argmax()
            percentage = int(result[predicted]*100)

            return self.classes[predicted], percentage

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode('utf-8')

            return base64_img
            # return "data:" + img.file.content_type + ";base64," + base64_img


class Pokemon(models.Model):
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
    image = models.ImageField('画像', upload_to='images', blank=True)
    # voice = models.FilePathField('音声', path=r'E:\develop\git\pokedex_web_application\mysite\myapp\static\myapp\voices')

    def __str__(self):
        return self.name_eng


# class Users(models.Model):
#     user_id = models.AutoField('ユーザーID', primary_key=True)
#     user_name = models.CharField('名前', max_length=255)
#     email = models.CharField('Eメール', max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.email


class Predicts(models.Model):
    predict_id = models.AutoField('判別ID', primary_key=True)
    user_email = models.CharField('Eメール', max_length=500)
    pokemon_id = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    image = models.ImageField('画像', upload_to='images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User:' + self.user_email + ' Pokemon:' + self.pokemon_id + ' date:' + self.created_at
