from django import forms
from django.forms import ModelForm
from .models import PostModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control ','placeholder':'Enter name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter bio'}),
            'logo': forms.TextInput(attrs={'class':'form-control','type':'file'}),
            'price': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter Price'}),



        }