# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20150828_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='hours',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
