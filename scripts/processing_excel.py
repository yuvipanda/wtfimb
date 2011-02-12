from __init__ import *

if __name__ == "__main__":
   import marshal
   from stages.models import Stage
   cg = marshal.load(open('../citygraph','r'))
   nj = set([stage_id for stage_id in cg.keys() if len(cg[stage_id]) <= 2]) # Non-junction stops
   j = set([stage_id for stage_id in cg.keys() if len(cg[stage_id]) > 2]) # Junction stops
   t = set([stage.id for stage in Stage.objects.filter(city='chennai') if stage.start_for_routes.count() + stage.end_for_routes.count() > 0]) # Terminal stops
   nt = set([stage.id for stage in Stage.objects.filter(city='chennai') if stage.start_for_routes.count() + stage.end_for_routes.count() == 0]) # Non-terminal stops
   shortlist = j | (nj & t) # stops that will make it to the worksheet
   hitlist = nj & nt # stops that will be hunted down
   # Remove all the non-terminal non-junction stops and re-wire citygraph
   # Assuming cg has consistent data for both directions of travel
   for prey in hitlist:
      if len(cg[prey]) == 1:
         del cg[cg[prey].keys()[0]][prey]
      else: # if len(cg[prey]) == 2:
         left = cg[prey].keys()[0]
         if left not in cg:
            raise Exception("left %d not in cg" % left)
         right = cg[prey].keys()[1]
         if right not in cg:
            raise Exception("right %d not in cg" % right)
         if left not in cg[right]:
            cg[left][right] = cg[right][left] = [cg[left][prey][0],# cg[left][prey]==cg[prey][right]
                              cg[left][prey][1] + cg[prey][right][1]] # Adding the distance
         else:
            cg[left][right][0] += cg[left][prey][0]
            cg[right][left][0] = cg[left][right][0]
      del cg[prey]
   shortlisted_stages = Stage.objects.filter(id__in=shortlist)

   print 'j =', len(j)
   print 't =', len(t)
   print 'nt =', len(nt)
   print 'nj =', len(nj)
   print 'jt =', len(j & t)
   print 'jnt =', len(j & nt)
   print 'njt =', len(nj & t)
   print 'njnt =', len(nj & nt)

   from xlwt import *
   from django.db.models import Count
   wb = Workbook()
   heading_style = easyxf("font: bold on; align: wrap on, vert center, horiz center")

   # STAGES WORKSHEET
   ws_stages = wb.add_sheet("stages")
   ws_stages.write(0, 0, "ID", heading_style)
   ws_stages.write(0, 1, "STAGE", heading_style)
   ws_stages.write(0, 2, "LAT", heading_style)
   ws_stages.write(0, 3, "LON", heading_style)
   ws_stages.write(0, 4, "TERMINAL_SERVICES", heading_style)
   ws_stages.write(0, 5, "TOTAL_SERVICES", heading_style)
   i = 0
   for stage in shortlisted_stages.annotate(total_services=Count('routelinks')).order_by('-total_services'):
      i += 1
      ws_stages.write(i, 0, stage.id)
      ws_stages.write(i, 1, stage.display_name)
      if stage.location:
         ws_stages.write(i, 2, stage.location.y)
         ws_stages.write(i, 3, stage.location.x)
      else:
         ws_stages.write(i, 2, 0)
         ws_stages.write(i, 3, 0)
      ws_stages.write(i, 4, stage.start_for_routes.count() + stage.end_for_routes.count())
      ws_stages.write(i, 5, stage.total_services)

   # ROUTES WORKSHEET
   from routes.models import Route
   qs_routes = Route.objects.filter(city='chennai')
   ws_routes = wb.add_sheet("routes")
   ws_routes.write(0, 0, "ID", heading_style)
   ws_routes.write(0, 1, "ROUTE", heading_style)
   ws_routes.write(0, 2, "TYPE", heading_style)
   ws_routes.write(0, 3, "STAGES ARRAY", heading_style)
   i = 0
   for route in qs_routes.order_by('id'):
      for service_type in route.types.split(','):
         i += 1
         ws_routes.write(i, 0, route.id) # FIXME: Ids are not unique because of service types
         ws_routes.write(i, 1, route.display_name)
         ws_routes.write(i, 2, service_type)
         j = 2
         for routestage in route.routestage_set.order_by('sequence'):
            if routestage.stage_id not in shortlist:
               continue
            j += 1
            ws_routes.write(i, j, routestage.stage_id)

   # SEGMENTS WORKSHEET
   ws_segments = wb.add_sheet("segments")
   ws_segments.write(0, 0, "ID", heading_style)
   ws_segments.write(0, 1, "SEGMENT", heading_style)
   ws_segments.write(0, 2, "STAGE_A", heading_style)
   ws_segments.write(0, 3, "STAGE_B", heading_style)
   ws_segments.write(0, 4, "STAGE_A_TERMINAL_ROUTES", heading_style)
   ws_segments.write(0, 5, "STAGE_B_TERMINAL_ROUTES", heading_style)
   ws_segments.write(0, 6, "ROUTES ARRAY")
   i = 0
   for src in cg.keys():
      src_stage = Stage.objects.get(id=src)
      for dest in cg[src].keys():
         if src > dest: continue # Guess writing only one direction of the segment is enough
         dest_stage = Stage.objects.get(id=dest)
         i += 1
         ws_segments.write(i, 0, i)
         ws_segments.write(i, 1, "%s - %s" % (src_stage.display_name, dest_stage.display_name))
         ws_segments.write(i, 2, src)
         ws_segments.write(i, 3, dest)
         ws_segments.write(i, 4, src_stage.start_for_routes.count() + src_stage.end_for_routes.count())
         ws_segments.write(i, 5, dest_stage.start_for_routes.count() + dest_stage.end_for_routes.count())
         j = 5
         for route in Route.objects.filter(stages=src).filter(stages=dest).order_by('id'):
            j += 1
            ws_segments.write(i, j, route.id)
   wb.save('processing_input.xls')
