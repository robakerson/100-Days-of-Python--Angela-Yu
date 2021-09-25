# ---- import environmental variables so I don't upload the wrong data to .git ----- #

import os
from dotenv import load_dotenv

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
SHEETY_USERNAME = os.getenv("sheety_username")
SHEETY_AUTH = os.getenv('sheety_auth')

sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/flightDeals/prices"

sheety_header = {
    'Authorization': SHEETY_AUTH
}