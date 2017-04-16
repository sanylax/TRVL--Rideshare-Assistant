import urllib2
import json
from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session
from lyft_rides.client import LyftRidesClient
from lyft_rides.auth import AuthorizationCodeGrant
  
def Lyft(start_latitude, start_longitude, end_latitude, end_longitude):
	auth_flow = ClientCredentialGrant(client_id="BaRMBhEu0hPh", client_secret="YGqQrluq5clWEVkyPvDWQIJ7XXjOCDKk", scopes="public")
	session = auth_flow.get_session()

	client = LyftRidesClient(session)
	response = client.get_cost_estimates(start_latitude, start_longitude, end_latitude, end_longitude)

	print(response.json)
	estimated_cost = response.json['cost_estimates'][2]['estimated_cost_cents_max'] / 100

	print(estimated_cost)
	return estimated_cost
