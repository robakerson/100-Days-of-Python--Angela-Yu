from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
CLIENT_ID = os.getenv("spotify_client_ID")
CLIENT_SECRET = os.getenv("spotify_client_secret")

res = requests.get(url=URL)
movies_site = res.text

soup = BeautifulSoup(movies_site, 'html.parser')
songs = soup.find_all("span", class_="chart-element__information__song")

song_names = [song.getText() for song in songs]

print(song_names)
