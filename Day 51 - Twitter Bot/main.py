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

PROMISED_DOWN = 150
PROMISED_UP = 10


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()


load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
# TWITTER_LOGIN = os.getenv('facebook_login')
# TWITTER_PASS = os.getenv('facebook_pw')

driver.get("https://twitter.com/")