import os,sys

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

if __name__ == "__main__":
   setup_environment()
   from wtfimb.stages.models import Stage
   from wtfimb.routes.models import Route
   for stage in Stage.objects.all():
      importance = stage.routelinks.count()
      importance = importance + stage.start_for_routes.count()*4
      importance = importance + stage.end_for_routes.count()*4
      if stage.is_terminus:
         importance = importance * 2
      stage.importance = importance
      stage.save()
