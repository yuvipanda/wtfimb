from django.conf.urls.defaults import *

urlpatterns = patterns('routing.views',
        (r'^(?P<start>\d+)/(?P<end>\d+)/$', 'show_shortest_path'),
        )
