# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from world.models import Address
from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("email", nargs='+', type=str)

    def handle(self, *args, **options):
        email = options["email"][0]
        user = User.objects.filter(email=email)
        if not user:
            return

        addresses = Address.objects.filter(author=user)
        for addr in addresses:
            print "%s" % addr.name
