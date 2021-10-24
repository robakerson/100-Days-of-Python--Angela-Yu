import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

# hackertime; fake a real browser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

zillow_search = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

res = requests.get(headers=headers, url=zillow_search)
soup = BeautifulSoup(res.content, 'html.parser')

print(soup.prettify())

prices = soup.find_all(class_='list-card-price')
addr = soup.find_all(class_='list-card-addr')
link = soup.find_all(class_='list-card-link')

print(prices)
print(addr)
print(link)

print(len(prices))
print(len(link))

# print(soup.text)
# print(soup)

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s, options=chrome_options)
# driver.maximize_window()
#
# driver.get('https://www.google.com')

# (address of the form) https://docs.google.com/forms/d/e/1FAIpQLSchd0igQnIZvLGD35U0LZKm0R_G8QGu46b6ujoEPxkJvnCZQw/viewform?usp=sf_link