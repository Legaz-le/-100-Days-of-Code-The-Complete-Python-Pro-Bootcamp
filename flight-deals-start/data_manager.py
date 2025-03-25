

import requests
import os
from requests.auth import HTTPBasicAuth
endpoint = "https://api.sheety.co/d5c2f3c1f3792d9fdb9cbdac2946fb1f/копияFlightDeals/prices/"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]

                }
            }
        response = requests.put(url=f"{endpoint}/{city['id']}",json=new_data)
        print(response.text)

