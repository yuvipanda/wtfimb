from django.conf.urls.defaults import *

urlpatterns = patterns('janitor.views',
        (r'^inconsistent/routes/(?P<maxdist>\d+)?$', 'inconsistent_routes'),
        )
