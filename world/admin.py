from django.contrib.gis import admin as geoadmin
from models import Address, Item
from django.core.mail import mail_admins
from django.contrib.gis.geos import fromstr
from django import forms
import urllib2
import json
import urllib
import logging
from simple_history import admin as shadmin

# Get an instance of a logger
logger = logging.getLogger("helphelp")

GMAPS_URL = "https://maps.googleapis.com/maps/api/geocode/json?"

def geocode(city, street):
    address = urllib.urlencode({"address":"%s %s" %
            (city.encode("utf-8"), street.encode("utf-8"))})
    url = GMAPS_URL + address

    res = urllib2.urlopen(url).read()
    res = json.loads(res)["results"]

    if not res:
        raise forms.ValidationError("Incorrect address. Make sure address is correct and try again.")

    lat = res[0]["geometry"]["location"]["lat"]
    lon = res[0]["geometry"]["location"]["lng"]
    return lat, lon


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        labels ={
		'name' : ('Standortname'),
		'city' : ('Stadt'),
		'street' : ('Strasse'),
		'zipcode' : ('Postleitzahl'),
		'phone' : ('Telefon'),
		'person' : ('Kontaktperson'),
		'hours' : ('Zeiten'),
		'website' : ('Webseite'),
		'validity' : ('Ablaufzeit in Stunden'),
		'items' : ('Gegenstaende'),
		}
    def clean(self):
        street = self.cleaned_data.get("street")
        city = self.cleaned_data.get("city")

        try:
            self.lat, self.lon = geocode(city, street)

        except forms.ValidationError as e:
            raise e
        
        except Exception as e:
            logger.error("Geocode error for address %s %s : %s" % (city, street, str(e)))
            raise forms.ValidationError("Cannot geocode address. Try again.")

        return self.cleaned_data

class AddressAdmin(geoadmin.OSMGeoAdmin, shadmin.SimpleHistoryAdmin):
    form = AddressForm
    list_display = ("name", )
    fields = ("name", "city", "street", "zipcode",
        "phone", "person", "hours", "website", "need_helpers", "validity", "items")

    def get_queryset(self, request):
        qs = super(AddressAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        is_new = obj.pk is None

        if is_new:
            obj.author = request.user
        obj.location = fromstr("POINT(%s %s)" % (form.lon, form.lat))
        obj.save()

        msg = "%s https://helphelp2.com/admin/world/address/%s/" % (obj.name, obj.id)
        mail_admins(subject="Helphelp2: %s has %s address" %
            (request.user.username, "added" if is_new else "updated"), message=msg)

geoadmin.site.register(Address, AddressAdmin)
geoadmin.site.register(Item)
