# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 20:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0016_auto_20170310_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 10, 14, 45, 5, 79536)),
        ),
    ]
