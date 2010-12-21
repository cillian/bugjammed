import simplejson as json
import urllib2

request = urllib2.urlopen('https://api.launchpad.net/1.0/launchpad-project?ws.op=searchTasks&tags=bugjam2010&status_list=&order_by=-date_last_updated').read()
bugs = json.loads(request)["entries"]

# tidy bug titles
for bug in bugs:
    colon_position = bug["title"].index(":") + 2
    bug["title"] = bug["title"][colon_position:]
        
print '<h1>Bugjammed</h1><h2>A list of the latest fixed bugs from BugJam 2010</h2><ul>'

for bug in bugs:
    if bug["status"] == "Fix Committed":
        print '<li>'
        print bug["title"]
        print '</li>'

print '</ul>'
