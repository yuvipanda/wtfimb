from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.main.views',
        (r'^$', 'index'),
        (r'route/(?P<id>\d+)/$', 'show_route'),
        (r'stage/(?P<id>\d+)/$', 'show_stage'),
        (r'unmapped/stages', 'show_unmapped_stages'),
		(r'unmapped/routes', 'show_unmapped_routes'),
        (r'mapped/stages', 'show_mapped_stages')
        )
