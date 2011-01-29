from __init__ import *
import marshal
from stages.models import Stage
from routes.models import Route

def get_distance(sid1, sid2):
   s1 = Stage.objects.get(id=sid1)
   s2 = Stage.objects.get(id=sid2)
   if s1.location is None or s2.location is None:
      return None
   return round(s1.location.distance(s2.location) * 111.195101192, 2) # distance in degrees * (pi / 180) * Radius of earth(6371.01)

def update_city_graph():
   citygraph = {}
   for city in ['chennai']:
      for route in Route.objects.filter(city=city):
         prev_rs = None
         for rs in route.routestage_set.order_by('sequence'):
            if not rs.stage_id in citygraph:
               citygraph[rs.stage_id] = {}
            if prev_rs is None:
               prev_rs = rs
               continue
            if not prev_rs.stage_id in citygraph[rs.stage_id]:
               dist = get_distance(prev_rs.stage_id, rs.stage_id)
               citygraph[rs.stage_id][prev_rs.stage_id] = [1, dist]
               citygraph[prev_rs.stage_id][rs.stage_id] = [1, dist]
            else:
               citygraph[rs.stage_id][prev_rs.stage_id][0] += 1
               citygraph[prev_rs.stage_id][rs.stage_id][0] += 1
   marshal.dump(citygraph, open(os.path.join(ROOT_DIR,"citygraph"), "wb"))

if __name__ == "__main__":
    update_city_graph()
