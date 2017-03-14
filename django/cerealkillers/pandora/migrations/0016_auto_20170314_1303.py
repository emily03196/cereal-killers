# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0015_auto_20170314_1216'),
    ]

    operations = [
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
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 14, 13, 3, 39, 954560)),
        ),
    ]