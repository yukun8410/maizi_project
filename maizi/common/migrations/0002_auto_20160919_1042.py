# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careercourse',
            name='image',
            field=models.ImageField(upload_to='course_img/%Y/%m', verbose_name='课程小图标'),
        ),
    ]