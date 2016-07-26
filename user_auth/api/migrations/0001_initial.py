# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-16 23:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=128, verbose_name='\u30bf\u30b9\u30af')),
                ('complete', models.BooleanField(default=False, verbose_name='\u72b6\u614b')),
                ('comment', models.CharField(blank=True, max_length=512, verbose_name='\u30b3\u30e1\u30f3\u30c8')),
                ('done_date', models.DateField(blank=True, null=True, verbose_name='\u5b8c\u4e86\u65e5')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
