# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0003_auto_20170225_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='descrpcion',
            new_name='descripcion',
        ),
    ]
