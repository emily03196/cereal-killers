# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0002_auto_20170308_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietRestrictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(choices=[('VT', 'Vegetarian'), ('VG', 'Vegan'), ('HL', 'Halal'), ('KS', 'Kosher'), ('GF', 'Gluten-Free')], max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Hurry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hurry_choice', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='boolean',
            name='question',
        ),
        migrations.RemoveField(
            model_name='mchoice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='address',
            name='question',
        ),
        migrations.RemoveField(
            model_name='distance',
            name='question',
        ),
        migrations.RemoveField(
            model_name='time',
            name='question',
        ),
        migrations.DeleteModel(
            name='Boolean',
        ),
        migrations.DeleteModel(
            name='MChoice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]