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

PROMISED_DOWN = 50
PROMISED_UP = 4

load_dotenv("C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/.env.txt")
# TWITTER_LOGIN = os.getenv('twitter_login')
# TWITTER_PASS = os.getenv('twitter_pw')

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, options=chrome_options)
        self.driver.maximize_window()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        try:
            close_ad = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
            close_ad.click()
        except:
            pass
        down_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

        self.down = down_speed.text
        self.up = up_speed.text

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')

        # Sign in with google
        sign_in_with_google = self.driver.get(By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[1]')
        sign_in_with_google.click()
        base_window = self.driver.window_handles[0]
        google_login = self.driver.window_handles[1]
        self.driver.switch_to(google_login)

        email = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        email.send_keys(GMAIL_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_button.click()


        text_box = self.driver.get(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        text_box.send_keys(f'This is a test message. My upload speed is: {self.up}MBps, My download speed is: {self.down}MBps. This is an automatically generated message.')
        tweet_button = self.driver.get(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div')
        tweet_button.click()


twit_bot = InternetSpeedTwitterBot()
# twit_bot.get_internet_speed()
twit_bot.tweet_at_provider()



