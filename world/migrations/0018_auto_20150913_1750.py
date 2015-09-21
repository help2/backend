# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0017_auto_20150912_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='validity',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'In wie vielen Stunden sollen die ben\xc3\xb6tigten Gegenst\xc3\xa4nde automatisch entfernt werden? Um keine Ablaufzeit zu definieren, geben Sie bitte 0 ein.'),
        ),
        migrations.AlterField(
            model_name='historicaladdress',
            name='validity',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'In wie vielen Stunden sollen die ben\xc3\xb6tigten Gegenst\xc3\xa4nde automatisch entfernt werden? Um keine Ablaufzeit zu definieren, geben Sie bitte 0 ein.'),
        ),
    ]
