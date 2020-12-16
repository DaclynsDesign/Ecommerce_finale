# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-25 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20201026_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='quantity',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2),
        ),
    ]
