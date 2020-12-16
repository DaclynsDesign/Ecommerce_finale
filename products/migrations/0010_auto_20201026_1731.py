# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-26 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_productmodel_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('white', 'white'), ('orange', 'orange'), ('newcolor', 'newcolor')], default='white', max_length=10),
        ),
    ]
