from django.conf.urls.defaults import *

urlpatterns = patterns('janitor.views',
        url(r'^inconsistent/routes/(?P<maxdist>\d+)?$', 'inconsistent_routes'),
        url(r'^nearby/stage/(?P<stage_id>\d+)?/$','softlinking_stages',name='softlinking_stages'),
        )
