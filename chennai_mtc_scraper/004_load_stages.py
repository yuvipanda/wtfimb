import simplejson as json
import os
import sys

CITY = 'chennai' # For different city, change here

def setup_env():
   pathname = os.path.dirname(sys.argv[0])
   sys.path.append(os.path.abspath(pathname))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../../')))
   os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_env()

def main():
   sjs = json.load(open('stages.json', 'r'))
   from stages.models import Stage
   
   for s in Stage.objects.filter(city=CITY):
      s.city = CITY + '_old'
      s.save()

   # For every stage name in the list
   for sj in sjs:
      try:
         s = Stage.objects.get(city__contains=CITY, mtc_name = sj)
         s_old = Stage()
         s_old.display_name = s.display_name
         s_old.city = s.city
         s_old.mtc_name = s.mtc_name
         s_old.save()
      except Stage.DoesNotExist:
         s = Stage()
      s.display_name = sj.title()
      s.city = CITY
      s.mtc_name = sj
      # Save the stage
      s.save()

if __name__ == "__main__":
   setup_env()
   main()
