# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0016_auto_20150910_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='validity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicaladdress',
            name='validity',
            field=models.IntegerField(default=0),
        ),
    ]
