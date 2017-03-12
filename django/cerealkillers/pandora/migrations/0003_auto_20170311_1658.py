# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 22:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0002_auto_20170310_1759'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RestartModel',
        ),
        migrations.AddField(
            model_name='pickrestaurantsmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AddField(
            model_name='recommendationmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AddField(
            model_name='rejectionmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AddField(
            model_name='responsesmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AddField(
            model_name='searchrestaurantsmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 11, 16, 58, 7, 50392)),
        ),
    ]