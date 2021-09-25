from env_import import *
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        res = requests.get(url=sheety_endpoint)
        data = res.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            res = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            # print(res.text)