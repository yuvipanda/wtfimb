from django.http import HttpResponse

from models import *
from django.views.generic.simple import direct_to_template
from django.contrib.gis.geos import Point

from forms import EditStageForm

def show_stage(request, id):
    if request.method == 'POST':
        form = EditStageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            s = Stage.objects.get(id=id)
            s.location = Point(cd['longitude'], cd['latitude'])
            s.save()
    else:
        s = Stage.objects.get(id=id)
        form = EditStageForm(
                initial = {'latitude': s.location.y,
                           'longitude': s.location.x}
                )
        return direct_to_template(request, 'stages/show_stage.html', {'form':form, 'stage':s})
    return HttpResponse()
    #Ideally, the above return should be under the else, but django complains, maybe use a variable
    # to store which response and return only that var.

def show_unmapped_stages(request):
    unmapped = Stage.objects.filter(location=None)
    return direct_to_template(request,"stages/show_unmapped_stages.html", 
            {'unmapped_stages':unmapped})

def show_mapped_stages(request):
    mapped = Stage.objects.filter(location__isnull=False)
    return direct_to_template(request, "stages/show_mapped_stages.html",
            {'mapped_stages':mapped})
