from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.basic.views',
		(r'^$', 'index'),
		(r'^showroute/(?P<id>\d+)/$', 'show_route'),
		(r'^stage/(?P<id>\d+)/$', 'show_stage'),
		)
