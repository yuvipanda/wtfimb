import MySQLdb
import pdb
import os
import sys

def setup_environment():
    pathname = os.path.dirname(sys.argv[0])
    sys.path.append(os.path.abspath(pathname))
    sys.path.append(os.path.normpath(os.path.join(os.path.abspath(pathname), '../')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

setup_environment()

from basic.models import *

old = MySQLdb.connect(
		host = "localhost",
		user = "root",
		passwd = "plasmafury",
		db = "busroutesin"
		)


#Migrate the Stages First
oldCur = old.cursor()

def NewStageForOldID(id):
	oldCur.execute("SELECT mtc_name FROM stages WHERE id = %s" % id)
	r = oldCur.fetchone()
	return Stage.objects.get(mtc_name=r[0])

def NewStagesForOldRoute(id):
	oldCur.execute("SELECT stage_id FROM routes_stages WHERE route_id = %s" % id)
	rows = oldCur.fetchall()	
	return [NewStageForOldID(r[0]) for r in rows]


#pdb.set_trace()
oldCur.execute ("SELECT name, lattitude, longitude, mtc_name FROM stages")
rows = oldCur.fetchall()
for r in rows:
	s = Stage(
			display_name = r[0],
			lattitude = r[1],
			longitude = r[2],
			mtc_name = r[3]
			)
	s.save()

oldCur.execute ("SELECT display_name, mtc_name, type, time, fare, start_stage, end_stage, id from routes")
rows = oldCur.fetchall()
for r in rows:
	route = Route(
			display_name = r[0],
			mtc_name = r[1],
			types = r[2],
			time = r[3],
			fare = r[4])
	route.start = NewStageForOldID(r[5])
	route.end = NewStageForOldID(r[6])
	route.save()
	route.stages = NewStagesForOldRoute(r[7]) 
	route.save()

	
