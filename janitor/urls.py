from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.janitor.views',
        (r'inconsistent/routes', 'inconsistent_routes'),
        )
