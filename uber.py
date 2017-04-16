import urllib2
import json
from uber_rides.session import Session


def Uber(start_latitude, start_longitude, end_latitude, end_longitude):
	request_headers = {
		"Authorization": "Token VG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS" 
	}

	session = Session(server_token = "sVG0_JuX6mRTU1FUTvL8wT1M8-2V51wrLv4sKzxaS")

	request = urllib2.Request("https://api.uber.com/v1.2/estimates/price?start_latitude=" + str(start_latitude) + "&start_longitude=" + str(start_longitude) + "&end_latitude=" +  str(end_latitude) + "&end_longitude=" + str(end_longitude), headers = request_headers)
	content = urllib2.urlopen(request).read()	
	jsoncontent = json.loads(content)
	print(jsoncontent)

	prices = jsoncontent['prices']
	if prices is None:
		return {}

	estimate = prices[2]['estimate']
	if estimate is None:
		return {}

	print("Estimate", estimate)
	return estimate
