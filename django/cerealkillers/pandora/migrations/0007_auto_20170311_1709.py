# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 23:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0006_auto_20170311_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickrestaurantsmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='recommendationmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='rejectionmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 11, 17, 9, 30, 786935)),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='searchrestaurantsmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
    ]