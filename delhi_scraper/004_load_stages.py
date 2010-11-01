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
      # if the stage is present already, do nothing
      if Stage.objects.filter(city='delhi').filter(mtc_name=sj):
         continue
      new_stage = Stage()
      new_stage.display_name = sj
      new_stage.city = 'delhi'
      new_stage.mtc_name = sj
      
      # Save the stage
      new_stage.save()
   
if __name__ == "__main__":
   setup_env()
   main()
