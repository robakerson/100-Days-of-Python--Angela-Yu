from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
res = requests.get(url=URL)
movies_site = res.text

# print(movies_site)
soup = BeautifulSoup(movies_site, 'html.parser')
# articles = soup.find_all(name='div', class_='jsx-4245974604')
articles = soup.find_all(name='h3')

# att_two = soup.select(selector=".jsx-4245974604")

print(articles)