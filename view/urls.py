from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.view.views',
		(r'^$', 'index'),
		(r'route/(?P<id>\d+)/$', 'show_route'),
		(r'stage/(?P<id>\d+)/$', 'show_stage'),
		)
