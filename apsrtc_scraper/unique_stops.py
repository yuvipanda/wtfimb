import simplejson as json
import csv
import sys

parsed_routes = json.load(open('parsed_routes.json', 'r'))

def add_stop(unprocessed_stop):
    stop = unprocessed_stop.replace("\n","")
    stop = stop.replace("\r","")
    stop = stop.replace("&nbsp","")
    stop = stop.replace("  ", " ")
    unique_stops.add((unprocessed_stop, stop))

unique_stops = set()
for route in parsed_routes:
    add_stop(route["from_stage"])
    add_stop(route["to_stage"])
    [add_stop(x) for x in route["via"]]

stops = list(unique_stops)
stops.sort(key=lambda x: x[0].lower())

writer = csv.writer(sys.stdout)
writer.writerows(stops)
