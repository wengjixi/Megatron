# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-02 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='module',
            field=models.CharField(max_length=32, unique=True, verbose_name='rsync\u6a21\u5757'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_dest',
            field=models.CharField(max_length=32, unique=True, verbose_name='\u9879\u76ee\u76ee\u6807\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_src',
            field=models.CharField(max_length=32, unique=True, verbose_name='\u9879\u76ee\u6e90\u5730\u5740'),
        ),
    ]