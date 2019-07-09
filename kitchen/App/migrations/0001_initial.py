# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-28 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredient', models.TextField(null=True)),
                ('score', models.FloatField(null=True)),
                ('author', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32)),
                ('u_password', models.CharField(max_length=256)),
            ],
        ),
    ]
