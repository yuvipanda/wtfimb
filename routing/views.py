from django.conf import settings
from stages.models import *
from routes.models import *
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse
import marshal

from django.conf import settings
import os

from dijkstra import shortestPath
from a_star import A_star

H = marshal.load(open(os.path.join(settings.ROOT_DIR, 'distancegraph'),'rb'))
G = marshal.load(open(os.path.join(settings.ROOT_DIR, 'adjacencygraph'),'rb'))

class ChangeOver:
    def __init__(self, start_stage, end_stage, routes):
        self.start_stage = start_stage
        self.end_stage = end_stage
        self.routes = routes

def direct_routes_between(start, end):
    return Route.objects.filter(stages__id=start.id).filter(stages__id=end.id)  

def find_distance(path):
    distance = 0
    for i in range(1,len(path)):
        distance = distance + H[path[i-1]][path[i]]
    return distance

def sort_route(route):
    return 
        

def show_shortest_path(request, start, end):
    paths = A_star(int(start), int(end), H, G)
    if not paths:
        return HttpResponse("Path not found")
    routes = []
    for path in paths:
        stages = [Stage.objects.get(id=sid) for sid in path]
        changeovers = []
        for i in xrange(0,len(stages) - 1):
            startStage = stages[i]
            endStage = stages[i+1]
            rc = ChangeOver(
                start_stage = startStage,
                end_stage = endStage,
                routes=direct_routes_between(startStage, endStage))
            changeovers.append(rc)
        routes.append({
                'changeovers':changeovers})

    return direct_to_template(request, "show_shortest_path.html",
                              {'paths': routes,
                               'start_stage':Stage.objects.get(id=start),
                               'end_stage':Stage.objects.get(id=end)})
