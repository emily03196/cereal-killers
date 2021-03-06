# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 04:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0007_auto_20170311_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickrestaurantsmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='recommendationmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='rejectionmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_day',
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='arrival_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 3, 13, 23, 17, 12, 524658)),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='diet',
            field=models.CharField(blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Halal', 'Halal'), ('Kosher', 'Kosher'), ('Gluten-Free', 'Gluten-Free')], max_length=500),
        ),
        migrations.AlterField(
            model_name='responsesmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
        migrations.AlterField(
            model_name='searchrestaurantsmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pandora.Username'),
        ),
    ]
