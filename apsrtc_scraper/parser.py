from BeautifulSoup import BeautifulSoup, NavigableString
import urllib2
import simplejson as json
import sys
def strip_tags(html, invalid_tags):
  soup = BeautifulSoup(html)
  for tag in soup.findAll(True):
    if tag.name in invalid_tags:
      s = ""
      for c in tag.contents:
        if not isinstance(c, NavigableString):
          c = strip_tags(unicode(c), invalid_tags)
        s += unicode(c)
        tag.replaceWith(s)
  return soup

def getHtml(url):
    user_agent = 'Mozilla/5 (Ubuntu 10.04) Gecko'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def parseHtml(html):
    soup = strip_tags(html, ['span'])
    trs = soup.findAll('tr')[5:-1]
    routes = []
    for tr in trs:
        tds = [x.contents[0] for x in tr.findAll('td')[:12]]
        route = {
            "from_stage" : tds[3].strip(),
            "to_stage" : tds[4].strip(),
            "via" : [x.strip() for x in tds[5].split(',')],
            "frequency_peak" : tds[10],
            "frequency_slack" : tds[11]
        }
        if type(tds[1]).__name__ == 'Tag':
            part1 = tds[1].contents[0].strip()
        else:
            part1 = tds[1].strip()
        if type(tds[2]).__name__ == 'Tag':
            part2 = tds[2].contents[0].strip()
        else:
            part2 = tds[2].strip()
        route["route_id"] = part1 + part2
        routes.append(route)
    return routes

if __name__ == "__main__":
    #url = 'http://apsrtc.gov.in/About%20Us/Route-Network/TIME%20TABLE-HCZ.htm'
    #html = getHtml(url)
    html = open('TIME TABLE-HCZ_debugged.htm','r').read()
    routes = parseHtml(html)
    json.dump(routes, sys.stdout, indent=2)

