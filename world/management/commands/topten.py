# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from world.models import Address, Item

class Command(BaseCommand):
    def handle(self, *args, **options):
        its = []
        for item in Item.objects.all():
            its.append((item.name, len(item.address_set.all())))

        its = sorted(its, key=lambda it: it[1], reverse=True)
        for i in its:
            print i[0], i[1]
            if i[1] == 0:
                break
