# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-30 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0001_initial'),
        ('orders', '0002_auto_20190829_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billings.BillingModel'),
        ),
    ]