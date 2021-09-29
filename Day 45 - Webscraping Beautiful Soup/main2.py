from bs4 import BeautifulSoup
import requests

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"
res = requests.get(url=URL)
movies_site = res.text

soup = BeautifulSoup(movies_site, 'html.parser')
articles = soup.find_all(name='h2')

articles_text = []
for _ in range(len(articles)):
    if _ % 2 == 0:
        articles_text.append(f"{articles[_].text} {articles[_+1].text}")
    # print(articles[_].text)
    # print(_ % 2)

with open("movies.txt", "w") as file:
    for _ in range(100):
        file.write(articles_text[_])
        file.write("\n")
