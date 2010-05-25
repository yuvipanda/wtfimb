from django.http import HttpResponse
from routes.models import *
from django.views.generic.simple import direct_to_template


def show_route(request, name):
    r = Route.objects.get(slug__iexact=name)
    return direct_to_template   (
            request, 
            'routes/show_route.html', 
            {
                'route':r,
                'stages':r.stages.order_by('routelinks__sequence')
                })


def show_unmapped_routes(request):
    unmapped = Route.objects.filter(stages__location=None)
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
