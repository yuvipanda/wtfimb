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
	(r'^chennai/', include('main.urls')),
	(r'^chennai/api/', include('api.urls')),
	(r'^chennai/path/', include('routing.urls')),
	(r'^$', lambda req: redirect_to(req,'/chennai')),
		
    # Example:
    # (r'^wtfimb/', include('wtfimb.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),

)
