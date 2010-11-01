from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                       (r'^static_mobile/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MOBILE_MEDIA_ROOT}),
                       url(r'^account/signup/$', 'registration.views.register', {'backend':'registration.backends.default.DefaultBackend' },
    name='registration_register'),
                       (r'^account/', include('django_authopenid.urls')),
                       (r'^account/settings','home.views.settings'),
                       (r'^account/password_change/$', 'django.contrib.auth.views.password_change'),
                       (r'^account/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^robots.txt$', lambda req: redirect_to(req,'/static/robots.txt')),
                       (r'^(?P<city>\w+)/api/', include('api.urls')),
                       (r'^(?P<city>\w+)/path/', include('routing.urls')),
                       (r'^(?P<city>\w+)/janitor/', include('janitor.urls')),
                       (r'^(?P<city>\w+)/', include('stages.urls')),
                       (r'^(?P<city>\w+)/', include('routes.urls')),
                       (r'^(?P<city>\w+)/$', include('home.urls')),
                       (r'^$', lambda req: redirect_to(req,'/chennai'))
                       #(r'^$', 'home.views.select_city'),
        
)
