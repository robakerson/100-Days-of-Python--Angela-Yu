import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
APP_ID = os.getenv("nutrition_app_id")
API_KEY = os.getenv("nutrition_api_key")
SHEETY_USERNAME = os.getenv("sheety_username")
SHEETY_AUTH = os.getenv('sheety_auth')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise_request_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What exercise did you complete today?:")

exercise_request_params = {
    'gender': 'male',
    'age': '35',
    'query': query
}

res = requests.post(url=exercise_request_endpoint, json=exercise_request_params, headers=headers)
res.raise_for_status()

result = res.json()

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/workoutTracking/workouts"
sheety_header = {
    'Authorization': SHEETY_AUTH
}

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    res = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_header)
    res.raise_for_status()

    print(res)
    print(res.text)