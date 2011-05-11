from django.http import HttpResponse,HttpResponseRedirect, Http404

from models import *
from django.views.generic.simple import direct_to_template
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.shortcuts import get_object_or_404

from forms import EditStageForm

def show_stage(request, city, id):
    if request.method == 'POST':
        form = EditStageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            s = Stage.objects.get(id=id)
            s.location = Point(cd['longitude'], cd['latitude'])
            s.save()
        return HttpResponseRedirect('.')
    else:
        s = get_object_or_404(Stage, id=id)
        if s.city != city:
            raise Http404
        if s.location!=None:
            form = EditStageForm(
                initial = {'latitude': s.location.y,
                           'longitude': s.location.x}
            )
        else:
            form = EditStageForm()
        default_map = {'zoom':12}
        if city == "chennai":
            default_map["lat"] = 13.0456;
            default_map["lon"] = 80.232;
        elif city == "bangalore":
            default_map["lat"] = 12.9832;
            default_map["lon"] = 77.5915;
        elif city == "delhi":
            default_map["lat"] = 28.6038;
            default_map["lon"] = 77.2134;
        else:
            default_map["lat"] = 13.0456;
            default_map["lon"] = 80.232;
        nearby_stages = Stage.objects.filter(city=city).filter(location__distance_lte=(s.location, D(km=2))).exclude(pk=s.id)
        return direct_to_template(request, 'stages/show_stage.html', {'form':form, 'city': city, 'default_map': default_map, 'stage':s, 'nearby_stages':nearby_stages})

def show_unmapped_stages(request, city):
    unmapped = Stage.objects.filter(city=city).filter(location=None)
    return direct_to_template(request,"stages/show_unmapped_stages.html", 
            { 'city': city, 'unmapped_stages':unmapped})

def show_mapped_stages(request, city):
    mapped = Stage.objects.filter(city=city).filter(location__isnull=False)
    return direct_to_template(request, "stages/show_mapped_stages.html",
            { 'city': city, 'mapped_stages':mapped})
