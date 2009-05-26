# Create your views here.

from appmodels.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

def all_routes(request):
    stages = Stage.objects.all()
    data = dict([ (s.id, 
        {'display_name': s.display_name,
         'latitude': s.latitude,
         'longitude': s.longitude}
        ) for s in stages])
    return HttpResponse(simplejson.dumps(data))

def autocomplete_stages(request):
    stages = Stage.objects.all()
    data = dict( [ (s.display_name, s.id) for s in stages] )
    return HttpResponse(simplejson.dumps(data))
