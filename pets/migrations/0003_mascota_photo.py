# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20160106_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas'),
        ),
    ]
