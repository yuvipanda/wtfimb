import marshal
import os
import sys
from datetime import datetime
from django.conf import settings
from math import *

def setup_environment():
   PARENT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
   ROOT_DIR = os.path.normpath(os.path.join(PARENT_DIR,'../'))
   PARENT_ROOT_DIR = os.path.normpath(os.path.join(ROOT_DIR,'../'))
   sys.path.append(PARENT_DIR)
   sys.path.append(ROOT_DIR)
   sys.path.append(PARENT_ROOT_DIR)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_environment()
from stages.models import Stage

H = marshal.load(open(os.path.join(settings.ROOT_DIR, 'distancegraph'),'rb'))
G = marshal.load(open(os.path.join(settings.ROOT_DIR, 'adjacencygraph'),'rb'))

came_from = {}                    # A linked list structure that remembers the path built
# DM = Multiplier of Distance when computing heuristic
# 'change overs is minimized' < DM < 'distance is minimized'
DM = 1
# IM = Multiplier of Importance when computing heuristic
# 'Changeover can be any stage' < IM < 'Important stages are preferred for changeovers'
IM = 0.0005
# RM = Multiplier of Route_Count when computing heuristic
# 'Naive routing' < RM < 'Stages that are strongly connected are preferred'
RM = 0.0005
  
def get_heuristic(start_stage, end_stage):
   if not H[start_stage].has_key(end_stage):
      return 100000 # Some large value, ideally Infinity
   elif not G[start_stage].has_key(end_stage):
      route_count = 0
   else:
      route_count = G[start_stage][end_stage]
   dist = H[start_stage][end_stage]
   heuristic = DM*dist - IM*(Stage.objects.get(pk=start_stage).importance) - RM*route_count
   return heuristic   

def get_distance(stage1,stage2):
   if not H[stage1].has_key(stage2):
      return 100000 # Some large value, ideally Infinity
   return H[stage1][stage2]

def A_star(start, goal):
   closedset = []                 # The set of nodes already evaluated.     
   openset = [start]              # The set of tentative nodes to be evaluated.
   g_score = {}                   # Distance from start along optimal path.
   h_score = {}                   # Heuristic distance to goal.
   f_score = {}                   # Estimated total distance from start to goal through y.
   g_score[start] = 0 
   h_score[start] = get_heuristic(start,goal)     
   f_score[start] = h_score[start]
   while openset:
      #Finding the node in openset having the lowest f_score[] value
      x = openset[0]
      for stage_id in openset:
         if f_score[x] > f_score[stage_id]:
            x = stage_id            
      if x == goal:
         path = []
         current_node = goal
         while current_node != start:
            path.append(current_node)
            current_node = came_from[current_node]
         for s in path:
            H[s]
         path.append(start)
         path.reverse()   
         return path
         
      openset.remove(x)
      closedset.append(x)
         
      for y in G[x]:
         if y in closedset:
            continue
         tentative_g_score = g_score[x] + get_distance(x,y) 

         if y not in openset:
            openset.append(y)
            tentative_is_better = True
         elif tentative_g_score < g_score[y]:
            tentative_is_better = True
         else:
            tentative_is_better = False

         if tentative_is_better == True:
            came_from[y] = x
            g_score[y] = tentative_g_score
            h_score[y] = get_heuristic(y, goal)
            f_score[y] = g_score[y] + h_score[y] 
   return None

if __name__ == "__main__":
   setup_environment()
   from stages.models import Stage
   G = marshal.load(open(os.path.join(settings.ROOT_DIR,'adjacencygraph'),'rb'))
   H = marshal.load(open(os.path.join(settings.ROOT_DIR,'distancegraph'),'rb'))
   path = A_star(int(sys.argv[1]),int(sys.argv[2]))
   print [Stage.objects.get(pk=sid) for sid in path]
