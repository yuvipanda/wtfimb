import simplejson as json
import os
import sys
from django.template.defaultfilters import slugify
def setup_env():
   pathname = os.path.dirname(sys.argv[0])
   sys.path.append(os.path.abspath(pathname))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../../')))
   os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_env()

def main():
   rjs = json.load(open('routes_detail.json', 'r'))
   from routes.models import Route, RouteStage
   from stages.models import Stage
   
   # For every route number in the dictionary
   for rj in rjs:
      
      # if the route is present already, edit it
      if not Route.objects.filter(city='delhi').filter(mtc_name=rj):
         new_route = Route()
      else:
         new_route = Route.objects.filter(city='delhi').get(mtc_name=rj)
         
      # Add/Reset details of the route
      new_route.display_name = rj
      new_route.city = 'delhi'
      new_route.mtc_name = rj
      new_route.types = "O" #FIXME: Classify routes under appropriate types
      new_route.fare = -1 #TODO: Scrape fare data
      new_route.time = -1 #TODO: Scrape time data
      new_route.slug = slugify(rj)

      # Add new/existing stage object as route's start stage
      try:
         sstage = rjs[rj][0]
         ssobj = Stage.objects.filter(city='delhi').get(mtc_name=sstage)
      except Stage.DoesNotExist:
         ssobj = Stage()
         ssobj.mtc_name = sstage
         ssobj.display_name = sstage
         ssobj.city = 'delhi'
         ssobj.save()
      new_route.start = ssobj
      
      # Add new/existing stage object as route's end stage
      try:
         estage = rjs[rj][-1]
         esobj = Stage.objects.filter(city='delhi').get(mtc_name=estage)
      except Stage.DoesNotExist:
         esobj = Stage()
         esobj.mtc_name = estage
         esobj.display_name = estage
         esobj.city = 'delhi'
         esobj.save()
      new_route.end = esobj

      # Save the route
      new_route.save()
      
      # Add RouteStage object for every stage in route
      sequence = 100
      for stage in rjs[rj]:
         
         # Get or create stage object
         try:
            sobj = Stage.objects.filter(city='delhi').get(mtc_name=stage)
         except Stage.DoesNotExist:
            sobj = Stage()
            sobj.mtc_name = stage
            sobj.display_name = stage
            sobj.city = 'delhi'
            sobj.save()
         
         # Get or create RouteStage object
         try:
            rs = RouteStage.objects.filter(route=new_route).get(stage__display_name=stage)
         except RouteStage.DoesNotExist:
            rs = RouteStage()
         rs = RouteStage()
         rs.route = new_route
         rs.stage = sobj
         rs.sequence = sequence
         rs.save()
         
         # Increment sequence of stage
         sequence += 100

if __name__ == "__main__":
   setup_env()
   main()
