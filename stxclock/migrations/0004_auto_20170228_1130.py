# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stxclock', '0003_auto_20170228_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='language',
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='style',
        ),
    ]