# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_auto_20170223_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='middle_name',
        ),
        migrations.AlterField(
            model_name='timetable',
            name='week_type',
            field=models.CharField(choices=[('1', 'Парний тиждень'), ('2', 'Непарний тиждень'), ('0', 'Обидва тижні')], max_length=2),
        ),
    ]
