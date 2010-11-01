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
for route in routes_index:
   
   # Post the 'BUSNO' to the server and get HTML output
   url = "http://delhigovt.nic.in/dtcbusroute/dtc/find_route/busnodetails.asp"
   data = { 'BUSNO': route }
   data_encoded = urllib.urlencode(data)
   request = urllib2.urlopen( url, data_encoded )
   html = request.read()
 
   # Clean the bad HTML code
   table_start_pos = html.rfind('<table')
   table_end_pos = html.rfind('</table>')
   html = "<html>\n\t<body>\n\t\t" + html[table_start_pos:table_end_pos + 8] + "\n\t</body>\n</html>"

   # Parse the HTML   
   soup = BeautifulSoup(html)
   tds = soup.table.findAll('td')
   
   # Clean the td
   tds = tds[:-1] # remove last blank td element
   tds = [str(td.contents[0]).strip() for td in tds] # Strip leading white space

   # Store in the dictionary
   routes_detail[route] = tds
   
# Output the Dictionary to json file
f = open('routes_detail.json','w')
f.write(json.dumps(routes_detail, indent=4))
f.close()

# Output the Dictionary to stdout as json
json.dumps(routes_detail, indent=4)
