
**urllib queries

from urllib.request import urlretrieve
from urllib.parse import urlencode
mydict = {'q': 'whee! Stanford!!!', 'something': 'else'}
qstr = urlencode(mydict)
# str resolves to: 'q=whee%21+Stanford%21%21%21&something=else'
thing 


** Getting a URL text using the dict/parse/query stuff

import requests
url_endpoint = 'https://www.duckduckgo.com'
mydict = {'q': 'whee! Stanford!!!', 'something': 'else'}
resp = requests.get(url_endpoint, params=mydict)

**to open web browsers from code
import webbrowser
url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400"
webbrowser.open(url)

**Wrinting Google Maps API with parameters
from urllib.parse import urlencode
import webbrowser
GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
mydict = {'size': '600x400'} #only size paramater needs to be specified
url = GMAPS_URL + urlencode(mydict) # https://maps.googleapis.com/maps/api/staticmap?size=600x400
mydict = {'size': '600x400', 'zoom': 4} #adding zoom parameter
url = GMAPS_URL + urlencode(mydict) # https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=4
mydict = {'size': '600x400', 'zoom': 14, 
          'markers': 'CoHo Café at Stanford'}
url = GMAPS_URL + urlencode(mydict) #marker at coho
pac12 = ['University of Arizona, AZ',
            'Arizona State University, AZ',
            'University of California, Berkeley, CA',
            'University of California, Los Angeles, CA',
            'University of Colorado Boulder, CO',
            'University of Oregon, OR',
            'Oregon State University, OR',
            'University of Southern California, CA',
            'Stanford University, CA',
            'University of Utah, UT',
            'University of Washington, WA',
            'Washington State University, WA']

mydict = {
  'size': '600x400','markers': pac12 
} #markers at all the pac 12 schools

url = GMAPS_URL + urlencode(mydict, doseq=True)

***To avoid creating lists by hand and read in 
import csv
import requests
from urllib.parse import urlencode
import webbrowser

USGS_URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv'
resp = requests.get(USGS_URL) #gets info from the url, which is just plain csv white text
lines = resp.text.splitlines() #splits lines of text from USGS url
earthquakes = csv.DictReader(lines) #reads a dictionary ?
coordinate_pairs = [] #list you will populate
for quake in earthquakes: #goes through lines. is quake a key?
    coordinate_pairs.append(quake['latitude'] + ',' + quake['longitude'])    
# create a URL based on Google Static Maps API specs
GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap'
query_string = urlencode(
                {'size': '800x500', 'markers': coordinate_pairs}, 
                doseq=True)
url = GMAPS_URL + '?' + query_string
webbrowser.open(url)


CLEANER VERSION OF ABOVE
# slightly more Pythonic, cleaner version
from csv import DictReader
import requests
import webbrowser
USGS_URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv'
GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap'
# get the USGS data, create a list of lines
lines = requests.get(USGS_URL).text.splitlines()

# get the latitude/longitude pairs
coordinate_pairs = ["%s,%s" % (q['latitude'], q['longitude']) for q in DictReader(lines)]

# this is another way of serializing the URL
preq = requests.PreparedRequest()
preq.prepare_url(GMAPS_URL, {'size':'800x500', 'markers': coordinate_pairs})
webbrowser.open(preq.url)

**Function that takes location, map width and map height and makes a google map url)
def foogoo_url(locations, width = 600, height = 400):
    from urllib.parse import urlencode
    gmap_url = 'https://maps.googleapis.com/maps/api/staticmap'
    size_str = str(width) + 'x' + str(height)
    query_str = urlencode({'size': size_str, 'markers': locations}, doseq=True)
    return gmap_url + '?' + query_str

>>> foogoo_url('New York, NY', height='200')
'https://maps.googleapis.com/maps/api/staticmap?markers=New+York%2C+NY&size=600x200'
>>> foogoo_url(['Wyoming', 'Alaska'])
'https://maps.googleapis.com/maps/api/staticmap?markers=Wyoming&markers=Alaska&size=600x400'

    