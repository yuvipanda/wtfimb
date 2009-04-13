from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.api.views',
		(r'routes/$', 'all_routes'),
		)
