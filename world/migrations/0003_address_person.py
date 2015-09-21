# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_remove_address_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
