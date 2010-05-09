from django.conf.urls.defaults import *

urlpatterns = patterns('api.views',
        (r'^routes/$', 'all_routes'),
        (r'^autocomplete/stages$', 'autocomplete_stages'),
        (r'^route/(?P<route_name>\w+)/$', 'single_route'),
        )
