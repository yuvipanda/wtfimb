# Create your views here.

from appmodels.models import *
from django.views.generic.simple import direct_to_template

def index(request):
    pass

def show_route(request, id):
    r = Route.objects.get(id=id)
    return direct_to_template(request, 'show_route.html', {'route':r})

def show_stage(request, id):
    s = Stage.objects.get(id=id)
    return  direct_to_template(request, 'show_stage.html', {'stage':s})

def show_unmapped_stages(request):
    unmapped = Stage.objects.filter(latitude=None)
    return direct_to_template(request,"show_unmapped_stages.html", 
            {'unmapped_stages':unmapped})

def show_mapped_stages(request):
    mapped = Stage.objects.filter(latitude__isnull=False)
    return direct_to_template(request, "show_mapped_stages.html",
            {'mapped_stages':mapped})

