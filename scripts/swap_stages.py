import os
import sys
def setup_env():
   pathname = os.path.dirname(sys.argv[0])
   sys.path.append(os.path.abspath(pathname))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '..')))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../..')))
   os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_env()

def copy_stage(dest, src):
   dest.display_name = src.display_name
   dest.location = src.location
   dest.mtc_name = src.mtc_name
   dest.is_terminus = src.is_terminus
   dest.city = src.city
   dest.save()
   for rl in src.routelinks.all():
      rl.stage = dest
      rl.save()

   for sr in src.start_for_routes.all():
      sr.start = dest
      sr.save()

   for er in src.end_for_routes.all():
      er.end = dest
      er.save()

from stages.models import Stage
if len(sys.argv) != 3:
   print "Usage: python %s <stageid1> <stageid2>" % sys.argv[0]

st1 = Stage.objects.get(id=int(sys.argv[1]))
st2 = Stage.objects.get(id=int(sys.argv[2]))

temp = Stage()
temp.display_name = 'Delete me'
temp.city = 'wonderland'
temp.save()

copy_stage(temp, st1)
copy_stage(st1, st2)
copy_stage(st2, temp)
temp.delete()
