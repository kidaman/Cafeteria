# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=0)),
                ('message', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('1', 'pending'), ('0', 'closed')], max_length=50)),
            ],
        ),
    ]
