
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CompUserRegistor(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Enter Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter Last Name'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter Password'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter Password again'}),
        }
