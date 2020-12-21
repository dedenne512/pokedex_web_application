from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Pokemon, PredictedImage, Predicts
from django.template.loader import get_template
from myapp.forms import UploadImageForm
import datetime
from django.contrib.auth.models import User
import base64, io
from PIL import Image
from io import BytesIO

# Create your views here.

# 初期アクセスページ
def index(request):
    return render(request, 'myapp/index.html')

def camera(request):
    return render(request, 'myapp/camera2.html')

# ポケモン一覧
def pokemon_list(request):
    list = Pokemon.objects.all().order_by('number')
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
        'photo': photo_data
    }

    request.session['predicted_data'] = data

    return HttpResponse(template.render(context, request))

def save(request):
    if not 'predicted_data' in request.session:
        return redirect('pokedex:select')
    
    pred = request.session['predicted_data']
    poke_id = pred['pokemon_id']
    photo_str = pred['photo']

    poke_info = Pokemon.objects.get(id = poke_id)

    # imgdata = base64.b64decode(photo_str)
    # filename = poke_info.name_eng + '.jpg'  # I assume you have a way of picking unique filenames
    # with open(filename, 'wb') as f:
    #     f.write(imgdata)
    #     template = get_template("myapp/index.html")


    # imgdata = Image.open(BytesIO(base64.b64decode(photo_str)))
    # imgdata.save(poke_info.name_eng + '.jpg', 'JPEG')

    user = User.objects.get()

    im = Image.open(BytesIO(base64.b64decode(photo_str)))
    output = BytesIO()
    im_img = im.save(output, "JPEG")
    jpg_img = output.read()

    Predicts.objects.create(user_email=user.username, pokemon_id_id=poke_id, image=im_img)
    return redirect('pokedex:index')
