from django.contrib import admin

from .models import Task
from .models import Maquina
from .models import Consumos

admin.site.register(Task)
admin.site.register(Maquina)
admin.site.register(Consumos)
