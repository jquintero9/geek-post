# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(max_length=160),
        ),
    ]
