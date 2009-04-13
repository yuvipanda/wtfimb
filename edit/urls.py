from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.edit.views',
		(r'route/(?P<id>\d+)/$', 'edit_route'),
		(r'stage/(?P<id>\d+)/$', 'edit_stage'),
		)
