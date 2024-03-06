
from .models import Task
from django import forms
from django.db import models
from .models import Maquina
from django.forms import ModelForm



class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = ['tipo', 'modelo', 'placa', 'chassi','data']