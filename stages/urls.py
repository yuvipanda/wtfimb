from django.conf.urls.defaults import *

urlpatterns = patterns('stages.views',
                       url(r'^stage/(?P<id>\d+)/$', 'show_stage', name='show-stage'),
                       url(r'^unmapped/stages', 'show_unmapped_stages'),
                       url(r'^mapped/stages', 'show_mapped_stages'),
        )
