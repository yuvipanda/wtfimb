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

setup_environment()
from stages.models import Stage
from routes.models import Route, RouteStage

def calculate_heuristics (src, dest):
    dist = distance_heuristic (src, dest)
    route_count = route_count_heuristic (src, dest)
    return ( (dist, importance_heuristic(src, dest), route_count),
             (dist, importance_heuristic(dest, src), route_count) )

def distance_heuristic (src, dest):
    return src.location.distance(dest.location)*111.195101192

def importance_heuristic (src, dest):
    return pow(dest.importance, 1/4)

def route_count_heuristic (src, dest):
    route_count = Route.objects.filter(stages__id=src.id).filter(stages__id=dest.id).count()
    return route_count

def update_distance_graph():
   distancegraph = {}
   for stage in Stage.objects.all():
      distancegraph[stage.id] = {}
      distancegraph[stage.id][stage.id] = (0,0,0)
   for src in Stage.objects.all():
      if src.location is None:
         continue
      for adj in Stage.objects.filter(id__gt = src.id):
         if adj.location:
             # distance in degrees * (pi / 180) * Radius of earth(6371.01)
             distancegraph[src.id][adj.id], distancegraph[adj.id][src.id] = calculate_heuristics(src, adj)
             print "%s (%s) -> %s (%s)" % (src.display_name,
                                           distancegraph[src.id][adj.id],
                                           adj.display_name,
                                           distancegraph[adj.id][src.id]
                                           )
   marshal.dump(distancegraph, open("distancegraph", "wb"))

if __name__ == "__main__":
    setup_environment()
    starttime = datetime.now()
    update_distance_graph()
    timedelta = datetime.now() - starttime
    print 'Executed in %d seconds'%timedelta.seconds
