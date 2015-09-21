from django.http import JsonResponse
from django.contrib.gis.geos import fromstr
from .models import Address
import logging

logger = logging.getLogger("helphelp")

def places(request):
    lat, lon = request.GET.get("lat", "0").replace(",", "."), request.GET.get("lon", "0").replace(",", ".")

    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError as e:
        logger.error("lat/lon are not float: %s" % e)
        lat = lon = 0
    
    places_list =[]
    point = fromstr("POINT(%s %s)" % (lon, lat))
    places = Address.objects.distance(point).order_by("distance")
    for p in places: 
        items = []
        for i in p.items.all():
            items.append(i.name)
        addr = {
            "city": p.city,
            "street": p.street,
            "zip": p.zipcode,
            "lat": p.location.y,
            "lon": p.location.x 
        }
        place = {
            "name": p.name,
            "addr": addr,
            "items": items,
            "distance": p.distance.m,
            "id": p.id,
            "person": p.person,
            "hours": p.hours,
            "phone": p.phone,
            "website": p.website,
            "helpers": p.need_helpers
        }
        places_list.append(place)
    output={"places": places_list}
    return JsonResponse(output)
