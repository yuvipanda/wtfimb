import simplejson as json
import os
import sys

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
   
   # For every stage name in the list
   for sj in sjs:
      try:
         s = Stage.objects.get(city='chennai', mtc_name = sj)
      except Stage.DoesNotExist:
         s = Stage()
         s.display_name = sj.title()
         s.city = 'chennai'
         s.mtc_name = sj
         # Save the stage
         s.save()
      s.city = 'chennai_new'
      s.save()
   
   for s in Stage.objects.filter(city='chennai'):
      s.city = 'chennai_old'
      s.save()

   for s in Stage.objects.filter(city='chennai_new'):
      s.city = 'chennai'
      s.save()
   
if __name__ == "__main__":
   setup_env()
   main()
