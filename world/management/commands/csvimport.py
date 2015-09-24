from django.core.management.base import BaseCommand
from world.models import Address, Item
from world import admin 
from django.contrib.gis.geos import fromstr
import codecs
import logging

logger = logging.getLogger("helphelp")

class Command(BaseCommand):
    args = "Arguments is not needed"
    help = "CSV importer"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", nargs='+', type=str)

    def process_lines(self, lines):
        # read addresses from DB
        existing_addrs = dict()
        for addr in Address.objects.all():
            existing_addrs[addr.name.lower()] = addr            

        # read places from DB
        existing_items = dict()
        for item in Item.objects.all():
            existing_items[item.name.lower()] = item            

        # iterate via CSV addresses
        for l in lines:
            l = l.strip()

            # skip comments
            if l.startswith("#"):
                continue
            try:
                name, city, street, zipcode, phone, person, hours, website, helpers, validity, items = l.split(",")

                addr = existing_addrs.get(name.lower(), None)
                if not addr:
                    logger.info("Creating address %s" % name)
                    addr = Address()
                    existing_addrs[name.lower()] = addr
                else:
                    logger.info("Using existing address %s" % name)
                
                addr.name = name.strip()
                addr.city = city.strip()
                addr.street = street.strip()
                addr.zipcode = zipcode.strip()
                addr.phone = phone.strip()
                addr.person = person.strip()
                addr.hours = hours.strip()
                addr.website = website.strip()
                addr.need_helpers = helpers.strip() == "1"
                if validity:
                    addr.validity = int(validity.strip())

                lat, lon = admin.geocode(city.strip(), street.strip())
                addr.location = fromstr("POINT(%s %s)" % (lon, lat))

                # have to save to add m2m below
                addr.save()
            
                addr.items.clear()

                items = items.split("|")
                for item_name in items:
                    item_name = item_name.strip()
                    if not item_name:
                        continue

                    item = existing_items.get(item_name.lower(), None)
                    if not item:
                        logger.info("Creating item %s" % item_name)
                        item = Item(name=item_name)
                        item.save()
                        existing_items[item_name.lower()] = item

                    addr.items.add(item)

                addr.save()

            except Exception as e:
                logger.error("Error processing %s... : %s" % (l[:20], e))
                continue


 
    def handle(self, *args, **options):
        # read data from CSV
        lines = []
        with codecs.open(options["csv_file"][0], 'r', encoding='utf8') as f:
            lines = f.readlines()
        
        self.process_lines(lines)
        