#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import time
from flight_data import find_cheapest_flight
from datetime import datetime,timedelta


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGINAL_CITY = "TYO"



for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

tomorrow = datetime.now()+ timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    print(f"Getting flight for {destination['city']}")
    flights = flight_search.check_flights(
        ORIGINAL_CITY,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: money {cheapest_flight.price}")
    time.sleep(2)





