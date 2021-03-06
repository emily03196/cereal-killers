# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0018_auto_20170314_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickrestaurantsmodel',
            name='pick_result',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pickrestaurantsmodel',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 14, 13, 54, 48, 804542)),
        ),
    ]
