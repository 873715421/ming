# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-07-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20190629_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('aid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'aplate',
            },
        ),
        migrations.CreateModel(
            name='Auser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=128)),
                ('type', models.IntegerField()),
                ('regtime', models.DateTimeField()),
                ('tx', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auser',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('titleid', models.IntegerField()),
                ('pic', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('costing', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isdelete', models.IntegerField(db_column='isDelete')),
                ('click', models.IntegerField()),
                ('kucun', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'good',
            },
        ),
        migrations.CreateModel(
            name='GoodT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'goodt',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isdelete', models.IntegerField(db_column='isDelete')),
            ],
            options={
                'managed': False,
                'db_table': 'type',
            },
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]
