# Create your views here.

from django.http import HttpResponse

from routes.models import *
from django.views.generic.simple import direct_to_template

from math import *
import marshal

class Inconsistency():
    pass

def find_inconsistencies(max_distance):
    routes = Route.objects.all()
    D = marshal.load(open('distancegraph','rb'))
    fixables = []
    for r in routes:
        stages = r.stages.all()
        for i in xrange(0, len(stages) - 1):
            if stages[i].location and stages[i+1].location:
                dist = D[stages[i].id][stages[i+1].id]
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

