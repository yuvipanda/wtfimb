import marshal
import os
import sys
from datetime import datetime
from math import *



came_from = {}                    # A linked list structure that remembers the path built
# M <= Multiplier of g_score when computing f_score
# If M is large, change overs is minimized, otherwise, distance is minimized
M = 5

def setup_environment():
   pathname = os.path.dirname(sys.argv[0])
   sys.path.append(os.path.abspath(pathname))
   sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
   os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
   
def get_heuristic(start_stage, end_stage, H, G):
   if H[start_stage].has_key(end_stage):
      (dist, importance, route_count) = H[start_stage][end_stage]
      return dist - pow(importance, 0.5) 
   else:
      return 100000 # Some large value, ideally Infinity

def A_star(start, goal, H, G, alternatives=3):
   closedset = []                 # The set of nodes already evaluated.     
   openset = [start]              # The set of tentative nodes to be evaluated.
   g_score = {}                   # Distance from start along optimal path.
   h_score = {}                   # Heuristic distance to goal.
   f_score = {}                   # Estimated total distance from start to goal through y.
   paths = []
   cur_alt = 0
   g_score[start] = 0 
   h_score[start] = get_heuristic(start,goal, H, G)     
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
         paths.append(path)
         cur_alt = cur_alt + 1
         if cur_alt >= alternatives:
            return paths
         
      openset.remove(x)
      if x!= goal:
         closedset.append(x)
         
      for y in G[x]:
         if y in closedset:
            continue
         tentative_g_score = g_score[x] + 1 

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
            h_score[y] = get_heuristic(y, goal, H, G)
            f_score[y] = g_score[y]*M + h_score[y] 
   return None

if __name__ == "__main__":
   setup_environment()
   from stages.models import Stage
   G = marshal.load(open('/home/yuvipanda/code/wtfimb/adjacencygraph','rb'))
   H = marshal.load(open('/home/yuvipanda/code/wtfimb/distancegraph','rb'))
   paths = A_star(int(sys.argv[1]),int(sys.argv[2]), H, G, 6)
   for path in paths:
      print path
