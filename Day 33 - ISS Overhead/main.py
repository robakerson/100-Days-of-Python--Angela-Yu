import requests
from datetime import datetime

MY_LAT = 42.036098
MY_LONG = -91.587219
LOCAL_UTC_OFFSET = -6

def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour

#
#
# res = requests.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()
#
# data = res.json()
#
# longitude = data["iss_position"]['longitude']
# latitude = data["iss_position"]['latitude']
# iss_position = (logitude, latitude)
# print(longitude, latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()

data = res.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
local_sunrise = utc_to_local(sunrise)
local_sunset = utc_to_local(sunset)

time_now = datetime.now()

print(local_sunrise)
print(local_sunset)
print(time_now.hour)