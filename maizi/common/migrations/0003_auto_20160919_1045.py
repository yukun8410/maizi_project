# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20160919_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course_img/%Y/%m', verbose_name='课程封面'),
        ),
    ]
