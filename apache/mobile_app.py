import os, sys

BASEDIR = os.path.join(os.path.dirname(__file__), '../..')
ROOTDIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(ROOTDIR)
sys.path.append(BASEDIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wtfimb.mobile_settings'



import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
