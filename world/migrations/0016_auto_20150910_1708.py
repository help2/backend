# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0015_historicaladdress'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='need_helpers',
            field=models.BooleanField(default=False, verbose_name=b'We also need helpers'),
        ),
        migrations.AddField(
            model_name='historicaladdress',
            name='need_helpers',
            field=models.BooleanField(default=False, verbose_name=b'We also need helpers'),
        ),
    ]
