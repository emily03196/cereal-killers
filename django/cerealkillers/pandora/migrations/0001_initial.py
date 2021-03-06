# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 23:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PickRestaurantsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_results1', models.CharField(blank=True, choices=[(None, None)], max_length=500)),
                ('pick_results2', models.CharField(blank=True, choices=[(None, None)], max_length=500)),
                ('pick_results3', models.CharField(blank=True, choices=[(None, None)], max_length=500)),
                ('pick_results4', models.CharField(blank=True, choices=[(None, None)], max_length=500)),
                ('pick_results5', models.CharField(blank=True, choices=[(None, None)], max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RejectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.NullBooleanField()),
                ('price_high', models.NullBooleanField()),
                ('price_low', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ResponsesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(blank=True, choices=[('VT', 'Vegetarian'), ('VG', 'Vegan'), ('HL', 'Halal'), ('KS', 'Kosher'), ('GF', 'Gluten-Free')], max_length=500)),
                ('distance', models.IntegerField(blank=True, default=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('hurry', models.NullBooleanField()),
                ('arrival_day', models.CharField(blank=True, choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=10)),
                ('arrival_time', models.TimeField(blank=True, default=datetime.datetime(2017, 3, 10, 17, 57, 23, 125591))),
            ],
        ),
        migrations.CreateModel(
            name='RestartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restart', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchRestaurantsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_query1', models.CharField(max_length=100)),
                ('search_query2', models.CharField(blank=True, max_length=100)),
                ('search_query3', models.CharField(blank=True, max_length=100)),
                ('search_query4', models.CharField(blank=True, max_length=100)),
                ('search_query5', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('username', models.CharField(max_length=12, null=True, unique=True)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
