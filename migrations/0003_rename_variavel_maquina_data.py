# Generated by Django 4.2.6 on 2023-11-01 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_maquina_variavel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maquina',
            old_name='variavel',
            new_name='data',
        ),
    ]