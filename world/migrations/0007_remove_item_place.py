# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='place',
        ),
    ]
