import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
TOKEN = os.getenv("pixl_token")
USERNAME = os.getenv("pixl_username")

headers = {
    "X-USER-TOKEN": TOKEN
}
pixela_endpoint = 'https://pixe.la/v1/users'

# ------- Create profile ---------#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# create profile
# res = requests.post(url=pixela_endpoint, json=user_params)
# print(res.text)


# ------- Create a graph ---------#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Learning to Code",
#     "unit": "hours",
#     "type": "int",
#     "color": "ajisai"
# }

# res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res.text)


# ------- Post a pixel ---------#
cur_graph = 'graph1'
cur_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{cur_graph}"

# sort today's date in the proper format
now = datetime.datetime.now()
year = now.year
month = now.month
if month < 10:
    month = f"0{month}"
day = now.day
if day < 10:
    day = f"0{day}"

today = f"{year}{month}{day}"

pixel_params = {
    "date": today,
    "quantity": '1',
}

# post a pixel!
res = requests.post(url=cur_graph_endpoint, json=pixel_params, headers=headers)
print(res.text)