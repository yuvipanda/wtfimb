from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import simplejson as json

user_agent = 'Mozilla/5 (Ubuntu 10.04) Gecko'
headers = { 'User-Agent' : user_agent }

# Load routes_index from file
routes_index = json.load(open('routes_index.json','r'))

# Scrape the stage information for every route in routes_index
routes_detail = {}
pf = open("partial_file", "w")
pf.write("{\n")
for route in routes_index:
   
   # GET the routedetails from the server
   params = urllib.urlencode({'cboRouteCode': route, 'submit':'Search'})
   url = "http://www.mtcbus.org/Routes.asp?%s" % params
   request = urllib2.Request( url, None, headers)
   response = urllib2.urlopen(request)
   html = response.read()
   
   # Cleanup bad HTML
   html = html.replace("'top'BGColor=''", "'top' BGColor=''")
   html = html.replace("JPG'Align", "JPG' Align")
   html = html.replace("OnClick=window.open(", "OnClick=\"window.open(")
   html = html.replace("')>View Route Map", "')\">View Route Map")

   '''
   # Save the page
   filename = 'temp.html'
   f = open(filename, "w")
   f.write(html)
   f.close()
   
   # Load the page
   filename = 'temp.html'
   f = open(filename, "r")
   html = f.read()
   f.close()
   '''
   
   # Parse the HTML   
   soup = BeautifulSoup(html)
   tds = soup.find('table', {'border':"1"}).findAll('td', {'align':'left'})[1:]
   text = []
   for td in tds:
      if len(td.contents) == 0:
         text.append(None)
      else:
         text.append(td.contents[0])
   # Store in the dictionary
   route_detail = {
        'service_type' : text[1], 
        'source' : text[2],
        'destination' : text[3],
        'stages' : text[4:]
   }
   routes_detail[route] = route_detail
   pf.write("\"%s\" :\n" % route)
   pf.write(json.dumps(route_detail, indent=4))
   pf.write(",\n") #FIXME: Don't include this for last element
   pf.flush()
pf.write("}")
pf.close()
# Output the Dictionary to json file
f = open('routes_detail.json','w')
f.write(json.dumps(routes_detail, indent=4, sort_keys=True))
f.close()

'''
# Output the Dictionary to stdout as json
print json.dumps(routes_detail, indent=4, sort_keys=True)
'''
