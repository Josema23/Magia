# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleccion', '0005_remove_mesa_circunscripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='circunscripcion',
            name='mesas',
            field=models.ManyToManyField(to='eleccion.mesa'),
        ),
    ]