# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-23 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20170222_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessontime',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lessontime',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
