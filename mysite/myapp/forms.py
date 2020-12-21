from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField(widget = forms.FileInput(attrs={"class":"custom-file-input"}))