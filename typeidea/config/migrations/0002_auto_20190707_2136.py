# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-07 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]