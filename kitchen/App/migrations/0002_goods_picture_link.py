# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-28 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='picture_link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
