# Generated by Django 4.2.6 on 2023-10-31 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='variavel',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
