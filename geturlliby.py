import urllib2
result = urllib2.urlopen('http://www.google.com');
print result.read()