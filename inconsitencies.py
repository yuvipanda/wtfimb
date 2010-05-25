
from __future__ import division
import os
import sys

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_environment()

from stages.models import Stage
from routes.models import Route

from math import *

MAX_DISTANCE = 2

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

if __name__ == '__main__':
    routes = Route.objects.all()
    for r in routes:
        stages = r.stages.order_by('routelinks__sequence')
        for i in xrange(0, len(stages) - 1):
            if stages[i].location and stages[i+1].location:
                dist = haversine(
                        stages[i].location.y, 
                        stages[i].location.x,
                        stages[i+1].location.y,
                        stages[i+1].location.x
                        )
                print dist
                if dist > MAX_DISTANCE:
                    print r.display_name
                    print stages[i].mtc_name
                    print stages[i+1].mtc_name
                    print dist
                    print 

