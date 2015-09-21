# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from world.models import Address, Item
from datetime import datetime, tzinfo, timedelta
import logging
from django.core.mail import send_mail

logger = logging.getLogger("helphelp")

EMAIL_TXT = """
Hallo,

Du hast eine Ablaufzeit für Deine Bedarfsliste hinterlegt, alle Einträge wurden nun entfernt.
Du kannst neue benötigte Gegenstände hier eintragen: %s

Dein helphelp2 Team

FB: https://www.facebook.com/helphelp2
Twitter: https://twitter.com/helphelpApp 

"""

class Command(BaseCommand):

    ZERO = timedelta(0)
    class UTC(tzinfo):
        def utcoffset(self, dt):
            return Command.ZERO
        def tzname(self, dt):
            return "UTC"
        def dst(self, dt):
            return Command.ZERO
    utc = UTC()

    help = "Remove items from addresses with expired validity"

    def log(self, msg):
        logger.info(msg)

    def handle(self, *args, **options):
        
        now = datetime.now(Command.utc)
        for addr in Address.objects.all():
            if addr.validity > 0 and addr.items.count():
                # calculate delta between last edit and now
                self.log("%s: validity %d hours" % (addr.name, addr.validity))
                last_updated = addr.history.latest().history_date
                delta = (now - last_updated).total_seconds() / 3600
                self.log("delta %d hours" % delta)
                
                # remove items if validity is expires
                if delta > addr.validity:
                    self.log(u"delete %d items: %s" % (addr.items.count(), ", ".join([n.name for n in addr.items.all()])))
                    addr.items.clear()
                    addr.save() 

                    # send email to author
                    if addr.author:
                        msg = EMAIL_TXT % ("https://helphelp2.com/admin/world/address/%d/" % addr.id)
                        send_mail("Deine Bedarfsliste läuft ab", msg,
                            "noreply@helphelp2.com", [addr.author.email], fail_silently=False)
