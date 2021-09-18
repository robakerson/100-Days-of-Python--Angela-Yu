import requests

API_KEY = ""
CITY = "Cedar Rapids,US"
LAT = 42.0083
LONG = -91.6441
# API_CALL = f"http://api.openweathermap.org/data/2.5/weather"
# CALL_PARAMS = {
#     "q": CITY,
#     "appid": API_KEY,
# }
API_ONECALL = f"https://api.openweathermap.org/data/2.5/onecall"
ONECALL_PARAMS = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
}


res = requests.get(url=API_ONECALL, params=ONECALL_PARAMS)
res.raise_for_status()
data = res.json()

print(res)
print(data)