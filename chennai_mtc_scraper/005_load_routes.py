import simplejson as json
import os
import sys
from django.template.defaultfilters import slugify
from mappings import *

CITY = 'chennai' # For different city, change here

MTC_TYPE_REVERSE_MAP = {
   'Ordinary': 'ORD',
   'Night Service': 'NGT',
   'LSS': 'LSS',
   'M-Route': 'MSVC',
   'Delux': 'DLX',
   'Air Condition': 'AC',
   'Express': 'EXP'
}

def setup_env():
   pathname = os.path.dirname(sys.argv[0])
   sys.path.append(os.path.abspath(pathname))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../../')))
   os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_env()

def resolve_route_name(name):
    display_name = name
    dlx_flag = False
    ac_flag = False
    for p in PREFIX_LIST:
        if display_name.startswith(p):
            if not p in PREFIX_KEEPERS:
               display_name = display_name.lstrip(p)
            if p == 'W':
               ac_flag = True
               display_name = display_name.rstrip('V')
            if p == 'S':
               dlx_flag = True
            break
    slug = slugify(display_name)
    for s in SUFFIX_LIST:
        if display_name.endswith(s):
            if not s in SUFFIX_KEEPERS: display_name = display_name.rstrip(s)
            slug = slugify(display_name)
            if s in EXT_ALIASES: display_name = display_name.replace(s," Ext")
            if s in CUT_ALIASES: display_name = display_name.replace(s," Cut")
            break
    if dlx_flag:
        display_name = display_name + " Dlx"
        slug = "s" + slug
    if ac_flag:
        display_name = display_name + " AC"
        slug = "w" + slug
    return (display_name, slug)

def main():
   rds = json.load(open('routes_detail.json', 'r'))
   from routes.models import Route, RouteStage, ROUTE_TYPE_MAPPING
   from stages.models import Stage
   
   # For every route number in the dictionary
   for mtc_name in rds:
      display_name, slug = resolve_route_name(mtc_name)
      rd = rds[mtc_name]
      if rd["source"] is None or rd["destination"] is None or len(rd["stages"]) == 0:
         continue # Skipping Incomplete routes
      service_type = rd["service_type"]
      s_type = MTC_TYPE_REVERSE_MAP[service_type]
      
      # if the route is present already, edit it
      if not Route.objects.filter(city=CITY).filter(slug=slug):
         r = Route()
      else:
         r = Route.objects.filter(city=CITY).get(slug=slug)
         
      # Add/Reset details of the route
      r.display_name = display_name
      r.city = CITY
      r.mtc_name = mtc_name
      if r.types is None or r.types == "":
         r.types = s_type
      elif s_type not in r.types.split(','):
         r.types = r.types + "," + s_type
      r.fare = -1 #TODO: Remove fare data
      r.time = -1 #TODO: Remove time data
      r.slug = slugify(slug)

      # Add new/existing stage object as route's start stage
      sstage = rd["source"]
      try:
         ssobj = Stage.objects.get(city=CITY, mtc_name = sstage)
      except Stage.DoesNotExist:
         ssobj = Stage()
         ssobj.display_name = sstage.title()
         ssobj.city = CITY
         ssobj.mtc_name = sstage
         ssobj.save()
      r.start = ssobj
      
      # Add new/existing stage object as route's end stage
      estage = rd["destination"]
      try:
         esobj = Stage.objects.get(city=CITY, mtc_name = estage)
      except Stage.DoesNotExist:
         esobj = Stage()
         esobj.display_name = estage.title()
         esobj.city = CITY
         esobj.mtc_name = estage
         esobj.save()
      r.end = esobj
      
      # Save the route
      r.save()
      
      # Add RouteStage object for every stage in route
      sequence = 100
      for stage in rd["stages"]:
         
         # Get or create stage object
         try:
            sobj = Stage.objects.get(city=CITY, mtc_name = stage)
         except Stage.DoesNotExist:
            sobj = Stage()
            sobj.display_name = stage.title()
            sobj.city = CITY
            sobj.mtc_name = stage
            sobj.save()
         
         # Get or create RouteStage object
         try:
            rs = RouteStage.objects.filter(route=r).get(stage=sobj)
         except RouteStage.DoesNotExist:
            rs = RouteStage()
         rs.route = r
         rs.stage = sobj
         rs.sequence = sequence
         rs.save()
         
         # Increment sequence of stage
         sequence += 100

if __name__ == "__main__":
   setup_env()
   main()
