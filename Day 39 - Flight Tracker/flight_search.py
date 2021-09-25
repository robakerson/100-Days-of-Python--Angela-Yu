from env_import import *
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        cur_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        cur_params = {
            'term': city_name,
            'location_types': 'city',
        }
        header = {
            'apikey': TEQUILA_API_KEY
        }
        res = requests.get(url=cur_endpoint, params=cur_params, headers=header)
        code = res.json()['locations'][0]['code']
        return code

