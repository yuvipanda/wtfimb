# Create your views here.

from django.http import HttpResponse

from stages.models import *
from routes.models import *
from django.views.generic.simple import direct_to_template

from forms import EditStageForm

def index(request):
    pass

def show_route(request, name):
    r = Route.objects.get(display_name__iexact=name)
    return direct_to_template   (
            request, 
            'routes/show_route.html', 
            {
                'route':r,
                'stages':r.stages.order_by('routestage__sequence')
                })

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
            #return HttpResponse()
            #else:
            #    return redirect_to(request, '/view/stage/%s' % id)
                
    else:
        s = Stage.objects.get(id=id)
        form = EditStageForm(
                initial = {'latitude': s.latitude,
                           'longitude': s.longitude}
                )
        return direct_to_template(request, 'stages/show_stage.html', {'form':form, 'stage':s})
    return HttpResponse()
    #Ideally, the above return should be under the else, but django complains, maybe use a variable
    # to store which response and return only that var.

def show_unmapped_stages(request):
    unmapped = Stage.objects.filter(latitude=None)
    return direct_to_template(request,"stages/show_unmapped_stages.html", 
            {'unmapped_stages':unmapped})

def show_mapped_stages(request):
    mapped = Stage.objects.filter(latitude__isnull=False)
    return direct_to_template(request, "stages/show_mapped_stages.html",
            {'mapped_stages':mapped})

def show_unmapped_routes(request):
    unmapped = Route.objects.filter(stages__latitude=None)
    return direct_to_template(request, 'routes/show_unmapped_routes.html',
            {'unmapped_routes':unmapped})

ROUTE_TYPE_MAPPING = {
        'D': 'Deluxe',
        'AC': 'Air Conditioned',
        'X': 'Express',
        'N': 'Night Service',
        'M': 'M Service',
        'O': 'Ordinary',
        'LSS': 'Limited Stop Service',
        }
def show_routes_with_type(request, type):
    routes = Route.objects.filter(types__contains=type)
    return direct_to_template(request, "routes/show_routes_with_type.html",
            {"routes": routes, "type": ROUTE_TYPE_MAPPING[type]})
