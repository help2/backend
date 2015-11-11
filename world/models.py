# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from urlparse import urlparse

class Item(models.Model):
    name = models.CharField('Gegenstand',max_length=64)
    comment = models.CharField('Beschreibung',max_length=256, blank=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    zipcode = models.CharField(max_length=5)
    street = models.CharField(max_length=64)
    website = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=64)
    phone = models.CharField(max_length=32, blank=True)
    person = models.CharField(max_length=64, blank=True)
    hours = models.CharField(max_length=64, blank=True)
    need_helpers = models.BooleanField(default=False, verbose_name="Wir benötigen Helfer!")
    validity = models.PositiveSmallIntegerField(default=0, help_text="In wie vielen Stunden sollen die benötigten Gegenstände automatisch entfernt werden? Um keine Ablaufzeit zu definieren, geben Sie bitte 0 ein.")

    author = models.ForeignKey(User, default=1, editable=False)

    items = models.ManyToManyField(Item, blank=True)

    objects = models.GeoManager()

    history = HistoricalRecords()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # add missing http:// prefix to make link open correctly in browser
        if self.website:
            p = urlparse(self.website)
            if not p.scheme:
                self.website = "http://%s" % self.website

        super(Address, self).save(*args, **kwargs)
