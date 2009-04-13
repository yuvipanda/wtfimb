from django.conf.urls.defaults import *

urlpatterns = patterns('wtfimb.edit.views',
		(r'stage/(?P<id>\d+)/$', 'edit_stage'),
		)
