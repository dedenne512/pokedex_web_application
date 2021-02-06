from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from myapp.models import Pokemon, PredictedImage, Predicts
from django.template.loader import get_template
from myapp.forms import UploadImageForm
import datetime
import base64, io, os
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
from django.core.files import File


# Create your views here.

# 初期アクセスページ
def index(request):
    return render(request, 'myapp/index.html')

def camera(request):
    return render(request, 'myapp/camera2.html')

# ポケモン一覧
def pokemon_list(request):
    predict_list = Predicts.objects.filter(author__id=request.user.id)
    pokemon_list = Pokemon.objects.all().order_by('number')

    dic = {}

    for poke in pokemon_list:
        for pred in predict_list:
            if poke.number == pred.pokemon.number:
                dic[poke.name_eng] = pred.image
                break

    print(dic)

    return render(
        request,
        'myapp/list.html',
        {
            'poke': pokemon_list,
            'pred': dic
        }
    )

def detail(request, id):
    poke_images = Predicts.objects.filter(author__id=request.user.id, pokemon__id=id)
    poke_info = Pokemon.objects.get(id = id)

    poke_image = poke_images[0]

    return render(
        request,
        'myapp/detail.html',
        {
            'p_image': poke_images,
            'p_data': poke_info,
            'image': poke_image
        }
    )

def config(request):
    return render(request, 'myapp/config.html')

def select(request):
    template = get_template("myapp/select.html")
    context = {'form': UploadImageForm()}
    return HttpResponse(template.render(context,request))

def predict(request):
    if not request.method == "POST":
        return redirect("pokedex:index")
    form = UploadImageForm(request.POST, request.FILES)
    if not form.is_valid():
        raise ValueError("Formが不正です")

    photo = PredictedImage(image = form.cleaned_data["image"])
    predicted, percentage = photo.predict()

    template = get_template("myapp/result.html")

    # original
    poke_info = Pokemon.objects.get(name_eng = predicted)
    photo_data = photo.image_src()

    context = {
        "photo_name": photo.image.name,
        "photo_data": photo_data,
        "predicted": predicted,
        "percentage": percentage,
        "pokemon": poke_info
    }

    data = {
        'pokemon_id': poke_info.id,
        'photo': photo_data,
        'photo_name': photo.image.name
    }

    request.session['predicted_data'] = data

    return HttpResponse(template.render(context, request))

def save(request):
    if not 'predicted_data' in request.session:
        return redirect('pokedex:select')
    
    if not request.user.is_authenticated:
        return redirect('pokedex:select')
    
    pred = request.session['predicted_data']
    poke_id = pred['pokemon_id']
    photo_str = pred['photo']
    photo_name = pred['photo_name']

    poke_info = Pokemon.objects.only('id').get(id = poke_id)


    img = base64.b64decode(photo_str.encode())
    with open(photo_name, 'bw') as f4:
        im = f4.write(img)

    user_model = get_user_model()
    user_data = user_model.objects.only('id').get(id=request.user.id)

    Predicts.objects.create(author=user_data, pokemon=poke_info, image=File(open(photo_name, 'rb')))

    os.remove(photo_name)

    return redirect('pokedex:index')

def delete(request, id):
    Predicts.objects.filter(predict_id=id).delete()
    return redirect('pokedex:index')