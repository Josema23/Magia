# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleccion', '0002_mesa_circunscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='partidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
