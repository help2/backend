# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('zipcode', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=64)),
                ('website', models.CharField(max_length=256, blank=True)),
                ('city', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=32)),
                ('person', models.CharField(max_length=64)),
            ],
        ),
    ]
