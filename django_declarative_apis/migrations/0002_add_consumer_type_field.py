#
# Copyright (c) 2019, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-23 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_declarative_apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauthconsumer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='oauthconsumer',
            name='type',
            field=models.CharField(choices=[('RO', 'Read Only'), ('RW', 'Read/Write')], db_index=True, default='RW', max_length=2),
        ),
    ]
