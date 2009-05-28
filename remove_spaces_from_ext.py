import os
import sys
def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_environment()

from appmodels.models import Route

exts = Route.objects.filter(display_name__contains='Ext')
for ext in exts:
    ext.display_name = ext.display_name.replace(' ','')
    ext.save()
    print "Done %s" % ext.display_name
    
exts = Route.objects.filter(display_name__contains='Cut')
for ext in exts:
    ext.display_name = ext.display_name.replace(' ','')
    ext.save()
    print "Done %s" % ext.display_name

exts = Route.objects.filter(display_name__contains='/')
for ext in exts:
    ext.display_name = ext.display_name.replace('/','')
    ext.save()
    print "Done %s" % ext.display_name