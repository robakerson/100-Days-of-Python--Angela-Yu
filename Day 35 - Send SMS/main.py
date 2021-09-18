import requests
from twilio.rest import Client

# -------------- don't upload ---------------- #


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