import requests
from datetime import datetime
import smtplib

MY_LAT = 42.036098
MY_LONG = -91.587219
LOCAL_UTC_OFFSET = -6
MY_EMAIL = "TEST@EMAIL.COM"
MY_PASSWORD = "PASSWORD"

def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour

# -------------------------- ISS position API CALL --------------------------#

def is_iss_close():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data = res.json()

    iss_longitude = float(data["iss_position"]['longitude'])
    iss_latitude = float(data["iss_position"]['latitude'])
    if MY_LONG + 5 > iss_longitude > MY_LONG - 5 and MY_LAT + 5 > iss_latitude > MY_LAT - 5:
        return True
    else:
        return False

# -------------------------- Sunrise/Sunset API CALL --------------------------#

def is_nighttime():
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
    time_now = datetime.now().hour

    if time_now <= local_sunrise or time_now >= local_sunset:
        return True
    else:
        return False


if is_nighttime() and is_iss_close():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: LOOK UP\n\n The ISS is above you in the sky"
    )


print(is_nighttime())
print(is_iss_close())