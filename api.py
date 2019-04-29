version = "0.0.1"
import json
from bottle import run, get, post, request
import urllib
import urllib2

@post('/dcordproxy')
def listing_handler():
	
	url = request.get_header('path')
	
	payload = request.body.read()
	
	req = urllib2.Request(url, headers={'user-agent':'Proxy Service for Detected.Solutions'})
	req.add_header('Content-Type', 'application/json')
	val = urllib2.urlopen(req, payload)
	
	return val.read()

	pass


run(host = 'IP', port='PORT')


print("LOADED." + version)