# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 20:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_perfil_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='genero',
            field=models.CharField(error_messages={'required': '\xbfC\xfaal es tu g\xe9nero?'}, max_length=6, validators=[django.core.validators.RegexValidator(message='G\xe9nero no v\xe1lido.', regex=b'^(hombre|mujer)$')]),
        ),
    ]
