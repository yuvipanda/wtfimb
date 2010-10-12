from BeautifulSoup import BeautifulSoup
import urllib2
import simplejson as json

user_agent = 'Mozilla/5 (Ubuntu 10.04) Gecko'
headers = { 'User-Agent' : user_agent }

# Get the Page from the server ( contains one select box with route numbers )
mtc_routes_url = 'http://www.mtcbus.org/Routes.asp'
request = urllib2.Request(mtc_routes_url, None, headers)
response = urllib2.urlopen(request)
the_page = response.read()

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
options = soup.select.findAll('option')

# Output the Routes index list to json file
filename = 'routes_index.json'
f = open(filename, "w")
f.write(json.dumps([ option.contents[0] for option in options ], indent=4))
f.close()

# Output the Routes index list to stdout as json
print json.dumps([ option.contents[0] for option in options ], indent=4)
