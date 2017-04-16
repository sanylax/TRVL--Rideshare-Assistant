import googlemaps

def GoogleMaps(starting_location, ending_location):
	maps = googlemaps.Client(key='AIzaSyCOlweck6eXODDMta-HgidoYqhM3GQ9XOE')
	
	geocode_starting_location = maps.geocode(starting_location)[0]['geometry']['location']
	geocode_ending_location = maps.geocode(ending_location)[0]['geometry']['location']
	print("Start: ", geocode_starting_location)
	print("End: ", geocode_ending_location)
	
	return [geocode_starting_location['lat'], geocode_starting_location['lng'], geocode_ending_location['lat'], geocode_ending_location['lng']]
