# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 04:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0005_auto_20170802_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tevent',
            name='bucket',
        ),
        migrations.RemoveField(
            model_name='tevent',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='tevent',
            name='key',
        ),
        migrations.RemoveField(
            model_name='tevent',
            name='requester_pays',
        ),
    ]
