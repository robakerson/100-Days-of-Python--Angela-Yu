from pprint import pprint
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from env_import import *

fsearch = FlightSearch()
dmanager = DataManager()


sheet_data = dmanager.get_destination_data()

for city in sheet_data:
    if not city['iataCode']:
        city['iataCode'] = fsearch.get_destination_code(city['city'])

dmanager.destination_data = sheet_data
dmanager.update_destination_codes()



