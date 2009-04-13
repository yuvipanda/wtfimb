# Create your views here.

from appmodels.models import *
from django.shortcuts import render_to_response

def index(request):
	pass

def show_route(request, id):
	r = Route.objects.get(id=id)
	return	render_to_response('show_route.html', {'route':r})

def show_stage(request, id):
	s = Stage.objects.get(id=id)
	return	render_to_response('show_stage.html', {'stage':s})

def show_unmapped_stages(request):
	unmapped = Stage.objects.filter(lattitude=None)
	return render_to_response("show_unmapped_stages.html", 
			{'unmapped_stages':unmapped})

