# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-26 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='follows',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
