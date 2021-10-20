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

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
FB_LOGIN = os.getenv('facebook_login')
FB_PASS = os.getenv('facebook_pw')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

driver.get("https://tinder.com/")

login = driver.find_element(By.XPATH, "//*[@id='c-364499427']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")

try:
    accept_privacy = driver.find_element(By.XPATH, '//*[@id="c-364499427"]/div/div[2]/div/div/div[1]/button')
    accept_privacy.click()
except NoS:
    pass

login.click()


time.sleep(1)
login_FB = driver.find_element(By.XPATH, '//*[@id="c-143158991"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_FB.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)