# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-16 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190116_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='上次登录时间'),
        ),
    ]
