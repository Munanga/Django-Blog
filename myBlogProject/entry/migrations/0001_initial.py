# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 00:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('topic', models.CharField(max_length=55)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 21, 0, 32, 29, 876245, tzinfo=utc))),
            ],
        ),
    ]
