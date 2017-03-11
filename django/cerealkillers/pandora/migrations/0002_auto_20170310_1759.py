# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 23:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickrestaurantsmodel',
            name='rating1',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, max_length=1),
        ),
        migrations.AddField(
            model_name='pickrestaurantsmodel',
            name='rating2',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, max_length=1),
        ),
        migrations.AddField(
            model_name='pickrestaurantsmodel',
            name='rating3',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, max_length=1),
        ),
        migrations.AddField(
            model_name='pickrestaurantsmodel',
            name='rating4',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, max_length=1),
        ),
        migrations.AddField(
            model_name='pickrestaurantsmodel',
            name='rating5',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, max_length=1),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 10, 17, 59, 7, 128400)),
        ),
    ]