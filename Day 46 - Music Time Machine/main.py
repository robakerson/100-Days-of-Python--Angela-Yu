from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
CLIENT_ID = os.getenv("spotify_client_ID")
CLIENT_SECRET = os.getenv("spotify_client_secret")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        show_dialog=True,
        cache_path='token.txt'
    )
)

user_id = spotify.current_user()['id']

res = requests.get(url=URL)
movies_site = res.text

soup = BeautifulSoup(movies_site, 'html.parser')
songs = soup.find_all("span", class_="chart-element__information__song")

song_names = [song.getText() for song in songs]

print(song_names)
