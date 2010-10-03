from django.http import HttpResponse, Http404
from routes.models import *
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404

def show_route(request, city, name):
    try:									
       r = Route.objects.filter(city=city).get(slug=slugify(name))
    except Route.DoesNotExist:
       raise Http404
    return direct_to_template   (
            request, 
            'routes/show_route.html', 
            {
                'route':r,
                'stages':r.stages.order_by('routelinks__sequence'),
                'city': city
                })


def show_unmapped_routes(request, city):
    unmapped = Route.objects.filter(city=city).filter(stages__location=None).distinct()
    return direct_to_template(request, 'routes/show_unmapped_routes.html',
            { 'city': city, 'unmapped_routes':unmapped})

ROUTE_TYPE_MAPPING = {
        'D': 'Deluxe',
        'AC': 'Air Conditioned',
        'X': 'Express',
        'N': 'Night Service',
        'M': 'M Service',
        'O': 'Ordinary',
        'LSS': 'Limited Stop Service',
        }
def show_routes_with_type(request, city, type):
    routes = Route.objects.filter(city=city).filter(types__contains=type)
    return direct_to_template(request, "routes/show_routes_with_type.html",
            {"routes": routes, 'city': city,  "type": ROUTE_TYPE_MAPPING[type]})
