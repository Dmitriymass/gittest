# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-27 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0002_user_userstats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='genger',
            new_name='gender',
        ),
    ]
