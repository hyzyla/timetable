# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-19 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20170219_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessontime',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]