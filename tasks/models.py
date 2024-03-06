from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from datetime import date
from django.utils import timezone
from datetime import datetime


class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
       
    image = models.ImageField(upload_to='imagem/')
     
     

class Maquina(models.Model):
    
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    chassi = models.CharField(max_length=17)
    data = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.tipo} {self.modelo} {self.placa} {self.chassi} ({self.data.strftime('%Y-%m-%d')})"

    

class Consumos(models.Model):
    
    operador = models.CharField(max_length=40)
    data = models.DateTimeField(default=datetime.now, blank=True)
    litragem = models.FloatField()
    valor = models.FloatField()
    kminicial = models.FloatField()
    kmfinal = models.FloatField()

def __str__(self):
        return f"{self.operador} {self.litragem} {self.valor} {self.kminicial} {self.kmfinal } ({self.data.strftime('%Y-%m-%d')})"


    
   
