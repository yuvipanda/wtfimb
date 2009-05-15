# Create your views here.

from appmodels.models import *
from django.views.generic.simple import direct_to_template

from view.forms import EditStageForm
from appmodels.models import Stage

def index(request):
    pass

def show_route(request, id):
    r = Route.objects.get(id=id)
    return direct_to_template(request, 'show_route.html', {'route':r})

#def show_stage(request, id):
#    s = Stage.objects.get(id=id)
#    return  direct_to_template(request, 'show_stage.html', {'stage':s})

def show_stage(request, id):
    if request.method == 'POST':
        form = EditStageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            s = Stage.objects.get(id=id)
            s.latitude = cd['latitude']
            s.longitude = cd['longitude']
            s.save(user=request.user)
            #if 'redirect' in cd and cd['redirect'] == 'false':
            return HttpResponse()
            #else:
            #    return redirect_to(request, '/view/stage/%s' % id)
                
    else:
        s = Stage.objects.get(id=id)
        form = EditStageForm(
                initial = {'latitude': s.latitude,
                           'longitude': s.longitude}
                )
        return direct_to_template(request, 'show_stage.html', {'form':form, 'stage':s})
    return HttpResponse()
    #Ideally, the above return should be under the else, but django complains, maybe use a variable
    # to store which response and return only that var.

def show_unmapped_stages(request):
    unmapped = Stage.objects.filter(latitude=None)
    return direct_to_template(request,"show_unmapped_stages.html", 
            {'unmapped_stages':unmapped})

def show_mapped_stages(request):
    mapped = Stage.objects.filter(latitude__isnull=False)
    return direct_to_template(request, "show_mapped_stages.html",
            {'mapped_stages':mapped})

