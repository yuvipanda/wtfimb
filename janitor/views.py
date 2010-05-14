# Create your views here.

from django.http import HttpResponse

from routes.models import *
from django.views.generic.simple import direct_to_template

from math import *


def haversine(lon1, lat1, lon2, lat2):
    # convert to radians 
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a)) 
    km = 6367 * c
    return km 

class Inconsistency():
    pass

def find_inconsistencies(max_distance):
    routes = Route.objects.all()
    fixables = []
    for r in routes:
        stages = r.stages.all()
        for i in xrange(0, len(stages) - 1):
            if stages[i].latitude and stages[i+1].latitude:
                dist = haversine(
                        stages[i].longitude, 
                        stages[i].latitude,
                        stages[i+1].longitude,
                        stages[i+1].latitude
                        )
                if dist > max_distance:
                    ic = Inconsistency()
                    ic.route = r
                    ic.stage = stages[i+1]
                    ic.distance = ceil(dist)
                    fixables.append(ic)
                    break
    return fixables

def inconsistent_routes(request, maxdist):
    if not maxdist:
        maxdist = 5
    incs = find_inconsistencies(int(maxdist))
    incs.sort(key=lambda x: x.distance,reverse=True)
    return direct_to_template   (
            request, 
            'janitor/routes.html', 
            {
                'inconsistencies':incs
                })

