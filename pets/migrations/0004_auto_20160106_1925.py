# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_mascota_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
