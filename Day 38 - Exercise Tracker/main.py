import os
import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
APP_ID = os.getenv("nutrition_app_id")
API_KEY = os.getenv("nutrition_api_key")


headers={
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

print(res)
print(res.text)