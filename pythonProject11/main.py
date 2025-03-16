import requests
from datetime import datetime
import os
Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id":os.environ["APPI_ID"],
    "x-app-key":os.environ["API_KEY"],
}
parameters = {
    "query":input("what did you do? "),
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 180,
    "age": 25,
}

response = requests.post(url=Endpoint,json=parameters,headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%x")

second_endpoint = "https://api.sheety.co/d5c2f3c1f3792d9fdb9cbdac2946fb1f/копияMyWorkouts/workouts"
headers_Second = {

}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date":today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

second_response = requests.post(url=second_endpoint,json=sheet_inputs,)

print(second_response)