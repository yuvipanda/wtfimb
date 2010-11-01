from BeautifulSoup import BeautifulSoup
import urllib2
import simplejson as json

user_agent = 'Mozilla/5 (Ubuntu 10.04) Gecko'
headers = { 'User-Agent' : user_agent }

# Get the Page from the server ( contains one select box with route numbers )
dtc_viewmap_url = 'http://delhigovt.nic.in/dtcbusroute/dtc/Find_Route/viewmap.asp'
request = urllib2.Request(dtc_viewmap_url, None, headers)
response = urllib2.urlopen(request)
the_page = response.read()

# Clean the bad HTML code
form_start_pos = the_page.rfind('<form')
form_end_pos = the_page.rfind('</form>')
the_page = "<html>\n\t<body>\n\t\t" + the_page[form_start_pos:form_end_pos + 7] + "\n\t</body>\n</html>"

# Save the page
filename = 'routes_index.html'
f = open(filename, "w")
f.write(the_page)
f.close()

# Load the page
filename = 'routes_index.html'
f = open(filename, "r")
the_page = f.read()
f.close()

# Parse the HTML
soup = BeautifulSoup(the_page)
options = soup.select.findAll('option')[1:]

# Output the Routes index list to json file
filename = 'routes_index.json'
f = open(filename, "w")
f.write(json.dumps([ option.contents[0] for option in options ], indent=4))
f.close()

# Output the Routes index list to stdout as json
print json.dumps([ option.contents[0] for option in options ], indent=4)
