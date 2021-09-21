import os
import requests
from dotenv import load_dotenv

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
TOKEN = os.getenv("pixl_token")
USERNAME = os.getenv("pixl_username")

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create profile
# res = requests.post(url=pixela_endpoint, json=user_params)
# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Learning to Code",
    "unit": "hours",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create graph
# res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res.text)