# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 15:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Actividad', '0006_auto_20160730_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='userName',
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default=datetime.datetime(2016, 7, 30, 15, 10, 51, 871000, tzinfo=utc), max_length=90),
            preserve_default=False,
        ),
    ]