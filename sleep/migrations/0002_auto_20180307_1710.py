# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='N1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='N2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='N3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='REM',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='score',
            field=models.FloatField(),
        ),
    ]
