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

# all this just to make the window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

driver.get("https://tinder.com/")

login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')

try:
    accept_privacy = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/button')
    accept_privacy.click()
except:
    pass
login.click()

# click "login with facebook" button
time.sleep(1)
login_FB = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_FB.click()

# make facebook login active window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# login with Facebook
email = driver.find_element(By.ID, "email")
email.send_keys(FB_LOGIN)
password = driver.find_element(By.ID, "pass")
password.send_keys(FB_PASS)
login_button = driver.find_element(By.ID, "loginbutton")
login_button.click()

driver.switch_to.window(base_window)
looking_for_location_tracking_button = True
while  looking_for_location_tracking_button:
    try:
        time.sleep(3)
        location_accept = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        location_accept.click()
        looking_for_location_tracking_button = False
    except:
        pass

time.sleep(1)
no_notifications = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
no_notifications.click()

# find the initial like button with exception handling
not_loaded = True

while not_loaded:
    try:
        time.sleep(2)
        like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()
        # not_loaded = False
    except:
        try:
            like_button = driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            like_button.click()
            # not_loaded = False
        except:
            print("WTF")
            pass

# keep smashing that like button every 1.5 seconds!
no_popups = True

while no_popups:
    time.sleep(1.5)
    try:
        like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()
    except:
        try:
            like_button = driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            like_button.click()
        except:
            try:
                not_interested = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button')
                not_interested.click()
            except:
                try:
                    x_button = driver.find_element(By.XPATH, '//*[@id="c-143158991"]/div/div/div[3]/button/svg')
                    x_button.click()
                except:
                    try:
                        buy_window = driver.find_element(By.XPATH, '//*[@id="c-143158991"]/div/div/div[3]/button/span')
                        driver.close()
                        no_popups=False
                    except:
                        driver.close()
                        no_popups = False