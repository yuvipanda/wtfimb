from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_DOC_ROOT}),
                       (r'^accounts/', include('registration.urls')),
                       
                       (r'^chennai/$', include('home.urls')),
                       (r'^chennai/', include('stages.urls')),
                       (r'^chennai/', include('routes.urls')),
                       (r'^chennai/api/', include('api.urls')),
                       (r'^chennai/path/', include('routing.urls')),
                       (r'^chennai/janitor/', include('janitor.urls')),
                       (r'^$', lambda req: redirect_to(req,'/chennai')),
        
                       (r'^admin/(.*)', admin.site.root),

)
