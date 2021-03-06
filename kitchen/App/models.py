# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

import datetime


class AppGoods(models.Model):
    name = models.CharField(max_length=50)
    ingredient = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    picture_link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'App_goods'


class AppUser(models.Model):
    u_name = models.CharField(max_length=32)
    u_password = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'App_user'


class User(models.Model):
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=2, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    regtime = models.DateTimeField(default=datetime.datetime.now)
    lasttime = models.DateTimeField(blank=True, null=True)
    login_type = models.CharField(max_length=2)
    tx = models.CharField(max_length=256, blank=True, null=True)
    rname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Aplate(models.Model):
    name = models.CharField(max_length=50)
    aid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aplate'


class Auser(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=128)
    type = models.IntegerField()
    regtime = models.DateTimeField()
    tx = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auser'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Good(models.Model):
    name = models.CharField(max_length=20)
    titleid = models.IntegerField()
    pic = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    costing = models.DecimalField(max_digits=5, decimal_places=2)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.
    click = models.IntegerField()
    kucun = models.IntegerField()
    content = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'good'


class Type(models.Model):
    ttitle = models.CharField(max_length=20)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type'
