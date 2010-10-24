import marshal
import os
import sys
from datetime import datetime
from math import *

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '..')))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../..')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

def update_adjacency_graph():
   adjacencygraph = {}
   from stages.models import Stage
   from routes.models import Route
   for src in Stage.objects.order_by('id'):
      if not adjacencygraph.has_key(src.id):
         adjacencygraph[src.id] = {}
      for adj in Stage.objects.filter(route__in=src.route_set.all()).filter(id__gt=src.id).distinct():
         if not adjacencygraph.has_key(adj.id):
            adjacencygraph[adj.id] = {}
         adjacencygraph[src.id][adj.id] = adjacencygraph[adj.id][src.id] = Route.objects.filter(stages__id=src.id).filter(stages__id=adj.id).count()
   marshal.dump(adjacencygraph, open("../adjacencygraph", "wb"))

if __name__ == "__main__":
    setup_environment()
    starttime = datetime.now()
    update_adjacency_graph()
    timedelta = datetime.now() - starttime
    print 'Executed in %d seconds'%timedelta.seconds
