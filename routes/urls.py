from django.conf.urls.defaults import *

urlpatterns = patterns('routes.views',        
                       url(r'^route/(?P<name>\w+)/$', 'show_route', name='show-route'),        
                       url(r'^unmapped/routes', 'show_unmapped_routes'),
                       url(r'^routes/type/(?P<type>\w+)/$', 'show_routes_with_type'),
                       )
