import os
from dotenv import load_dotenv
from pprint import pprint
import requests
from flight_search import FlightSearch

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
SHEETY_USERNAME = os.getenv("sheety_username")
SHEETY_AUTH = os.getenv('sheety_auth')

sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices"
sheety_header = {
    'Authorization': SHEETY_AUTH
}

fsearch = FlightSearch()

# res = requests.get(url=sheety_endpoint, headers=sheety_header)
# res.raise_for_status()
#
# result = res.json()


result = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
sheet_data = result['prices']

for place in sheet_data:
    if not place['iataCode']:
        place['iataCode'] = fsearch.search_city(place['city'])


print(result)
print(sheet_data)