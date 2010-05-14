import marshal
import os
import sys
from datetime import datetime
from math import *

from stages.models import Stage

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

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_environment()

def update_graph():
   distancegraph = {}
   for src in Stage.objects.order_by('id'):
      if not distancegraph.has_key(src.id):
         distancegraph[src.id] = {}
      for adj in Stage.objects.filter(route__in=src.route_set.all()).filter(id__gt=src.id).distinct():
         if not distancegraph.has_key(adj.id):
            distancegraph[adj.id] = {}
         if src.longitude and src.latitude and adj.longitude and adj.latitude:
            distancegraph[src.id][adj.id] = distancegraph[adj.id][src.id] = (int)(haversine(src.longitude,src.latitude,adj.longitude,adj.latitude))
   marshal.dump(distancegraph, open("distancegraph", "wb"))

if __name__ == "__main__":
    starttime = datetime.now()
    update_graph()
    timedelta = datetime.now() - starttime
    print 'Executed in %d seconds'%timedelta.seconds
