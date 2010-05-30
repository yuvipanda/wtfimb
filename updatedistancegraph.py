import marshal
import os
import sys
from datetime import datetime
from math import *

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

def update_distance_graph():
   distancegraph = {}
   from stages.models import Stage
   for stage in Stage.objects.all():
      distancegraph[stage.id] = {}
      distancegraph[stage.id][stage.id] = 0
   for src in Stage.objects.all():
      if src.location is None:
         continue
      for adj in Stage.objects.filter(id__gt = src.id):
         if adj.location:
            distancegraph[src.id][adj.id] = distancegraph[adj.id][src.id] = (src.location.distance(adj.location)*111.195101192)# distance in degrees * (pi / 180) * Radius of earth(6371.01)
   marshal.dump(distancegraph, open("distancegraph", "wb"))

if __name__ == "__main__":
    setup_environment()
    starttime = datetime.now()
    update_distance_graph()
    timedelta = datetime.now() - starttime
    print 'Executed in %d seconds'%timedelta.seconds
