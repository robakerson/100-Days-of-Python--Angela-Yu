import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# -------------- don't upload ---------------- #
load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
API_KEY = os.getenv("OWM_API_KEY")
ACCT_SID = os.getenv("ACCT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_PH = os.getenv("TWILIO_PH")
PERSONAL_PH = os.getenv("PERSONAL_PH")

LAT = 42.0083
LONG = -91.6441

API_ONECALL = f"https://api.openweathermap.org/data/2.5/onecall"
ONECALL_PARAMS = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

res = requests.get(url=API_ONECALL, params=ONECALL_PARAMS)
res.raise_for_status()
data = res.json()

check_qty_hours = 12
hourly_data = data['hourly']

it_will_rain = False
for _ in range(check_qty_hours):
    current_weather = hourly_data[_]['weather']  # will hold list of dictionaries
    for num in range(len(current_weather)):
        if current_weather[num]["id"] < 700:
            it_will_rain = True

if it_will_rain:
    client = Client(ACCT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an ☔. It's going to rain",
        from_=TWILIO_PH,
        to=PERSONAL_PH,
    )
    print(message.status)
else:
    print("HEY")