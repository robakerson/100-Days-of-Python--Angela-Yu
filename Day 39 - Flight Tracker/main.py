from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta

fsearch = FlightSearch()
dmanager = DataManager()
ORIGIN_CITY_IATA = "LON"

sheet_data = dmanager.get_destination_data()

for city in sheet_data:
    if not city['iataCode']:
        city['iataCode'] = fsearch.get_destination_code(city['city'])

dmanager.destination_data = sheet_data
dmanager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = fsearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

