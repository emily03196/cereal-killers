# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 01:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pandora', '0002_auto_20170309_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='username',
            old_name='user_text',
            new_name='username',
        ),
    ]
