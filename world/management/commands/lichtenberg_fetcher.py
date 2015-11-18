# -*- coding: utf-8 -*-

import logging
from django.core.management.base import BaseCommand
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse
from csvimport import Command as CsvImporter

logger = logging.getLogger("helphelp")

CSV_LINKS = ["http://marzahn.schnell-helfen.de/index.php?id=1655","http://lichtenberg.schnell-helfen.de/index.php?id=1655","http://xhain.schnell-helfen.de/index.php?id=1655","http://hma103.schnell-helfen.de/index.php?id=1655","http://gruenheide.schnell-helfen.de/index.php?id=1655","http://bernau.schnell-helfen.de/index.php?id=1655","http://unterfoehring.schnell-helfen.de/index.php?id=1655", "http://steglitz-zehlendorf.schnell-helfen.de/index.php?id=1655"]

class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_importer = CsvImporter()

        lines = []

        for l in CSV_LINKS:
            try:
                up = urlparse(l)
                html = urllib2.urlopen(l).read()
                soup = BeautifulSoup(html, 'html.parser')
                for li in soup.ul.findAll("li"):
                    path = li.a["href"]
                    url = "%s://%s/%s" % (up.scheme, up.netloc, path)
                    logger.info("Fetching CSV from %s" % url)
                    csv = urllib2.urlopen(url).read()
                    lines.append(csv.decode("utf-8"))

            except (urllib2.URLError, urllib2.HTTPError) as e:
                logger.error("Cannot fetch %s: %s" % (l, e.reason))

        csv_importer.process_lines(lines)
