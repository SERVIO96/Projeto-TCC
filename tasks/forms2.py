from django.forms import ModelForm
from .models import Consumos

class ConsumosForm(ModelForm):
    class Meta:
        model = Consumos
        fields = ['operador', 'data', 'litragem', 'valor', 'kminicial', 'kmfinal']