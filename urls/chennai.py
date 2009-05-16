from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
	('^$', include('home.urls')),	
	(r'', include('admin.urls')),
	(r'^api/', include('api.urls')),
	(r'^path/', include('routing.urls')),
		
    # Example:
    # (r'^wtfimb/', include('wtfimb.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
