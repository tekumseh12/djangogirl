# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 15:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181102_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 15, 37, 34, 986453, tzinfo=utc)),
        ),
    ]
