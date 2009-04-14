import marshal
import os
import sys

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_environment()

from appmodels.models import *

def update_graph():
    graph = {}

    for src in Stage.objects.all():
        route_stages = src.routestage_set.all()
        for rs in route_stages:
            position = rs.sequence
            
            innerRS = rs.route.routestage_set.all()

            for irs in innerRS:
                dest = irs.stage
                position2 = irs.sequence
                if dest.id == src.id:
                    continue

                dist = abs(position - position2)

                if not graph.has_key(src.id):
                    graph[src.id] = {}

                if not graph[src.id].has_key(dest.id) or graph[src.id][dest.id] > dist:
                    graph[src.id][dest.id] = dist

    marshal.dump(graph, open("graph", "wb"))

if __name__ == "__main__":
    update_graph()
