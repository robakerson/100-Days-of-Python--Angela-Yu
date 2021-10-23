import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

driver.get('https://www.google.com')

# (address of the form) https://docs.google.com/forms/d/e/1FAIpQLSchd0igQnIZvLGD35U0LZKm0R_G8QGu46b6ujoEPxkJvnCZQw/viewform?usp=sf_link