# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-03 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u30ab\u30c6\u30b4\u30ea', 'verbose_name_plural': '\u30ab\u30c6\u30b4\u30ea'},
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Todo', 'verbose_name_plural': 'Todo'},
        ),
    ]