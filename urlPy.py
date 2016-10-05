import urllib2
import pprint
result = urllib2.urlopen("http://www.freegeoip.net/json/117.21.191.2")
pprint.pprint(result.read());