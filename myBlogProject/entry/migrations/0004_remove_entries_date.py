# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_entries_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='date',
        ),
    ]