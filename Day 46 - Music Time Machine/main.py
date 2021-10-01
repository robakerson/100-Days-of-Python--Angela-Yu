from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

res = requests.get(url=URL)
movies_site = res.text

soup = BeautifulSoup(movies_site, 'html.parser')
songs = soup.find_all("span", class_="chart-element__information__song")

song_names = [song.getText() for song in songs]

print(song_names)