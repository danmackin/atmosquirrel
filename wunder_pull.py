#!/usr/bin/python
# 
# 04/10/2017 - Dan Mackin
# Started customizing for site
#
import urllib2
import json

from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

#print config.get('main', 'wu_api')
#print config.get('main', 'wu_city')
#print config.get('main', 'wu_state')

# getfloat() raises an exception if the value is not a float
#a_float = config.getfloat('main', 'a_float')

# getint() and getboolean() also do this for their respective types
#an_int = config.getint('main', 'an_int')

wu_api = config.get('main', 'wu_api')
print "Weather Underground API Set to: %s" % wu_api

f = urllib2.urlopen('http://api.wunderground.com/api/%s/conditions/q/pws:KCOLAFAY65.json' % wu_api)
#f = urllib2.urlopen('http://api.wunderground.com/api/%s/geolookup/conditions/q/CO/Lafayette.json' % wu_api)
json_string = f.read()

# Uncomment to Print Data
#print json_string

# Parse Data
parsed_json = json.loads(json_string)

# Get Location & Temp
location = parsed_json['current_observation']['observation_location']['full']
temp_f = parsed_json['current_observation']['temp_f']

# Print in easy format
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
