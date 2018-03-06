# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateField(auto_now_add=True)),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('move', models.IntegerField()),
                ('breathe_stop', models.IntegerField(default=0)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('N1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('N2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('N3', models.DecimalField(decimal_places=2, max_digits=4)),
                ('REM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('data', models.FileField(upload_to='sleepData/%Y/%m/%d')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleeps', to='device.Device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleeps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('time_stamp',),
            },
        ),
        migrations.AddField(
            model_name='report',
            name='sleep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='sleep.Sleep'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
    ]
