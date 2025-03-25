import requests
import os
from data_manager import DataManager
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self):
        self.Api_key = os.getenv("API_KEY")
        self.Api_secret = os.getenv("API_SECRET")
        self.Token = self.get_new_token()

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.Api_key,
            'client_secret': self.Api_secret,
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self,city_name):

        headers = {
            "Authorization": f"Bearer {self.Token}"
        }
        query = {
            "keyword":city_name,
            "max": "2",
            "include": "AIRPORTS",

        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)



        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: no Airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No Airport code found for {city_name}")
            return "Not Found"
        return  code
    def check_flights(self,original_city_code,destination_city_code,from_time,to_time):
        headers = {"Authorization": f"Bearer {self.Token}"}
        query = {
            "originLocationCode":original_city_code,
            "destinationLocationCode":destination_city_code,
            "departureDate": from_time.strftime("%Y-%m=%d"),
            "returnDate":to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "noneStop": "true",
            "currencyCode": "USD",
            "max": "10",

        }
        response = requests.get(url=FLIGHT_ENDPOINT,headers=headers,params=query)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print(f"There was a problem with the flight search.\n"
                  "for details on status codes, check the API documenation")

            return None
        return response.json()




