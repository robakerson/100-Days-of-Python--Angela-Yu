from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
# driver.get("https://orteil.dashnet.org/cookieclicker/") # modern version
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "bigCookie")

# BUILDING_PRICES = ["productPrice3","productPrice2","productPrice1","productPrice0"]
BUILDINGS = ["product3","product2","product1","product0"]

def click_for_five():
    start = time.time()
    while time.time() < (start + 5):
        cookie.click()


def get_cur_cookies():
    return driver.find_element(By.ID, "cookies").text.split()[0]


def get_cookies_per_second():
    return driver.find_element(By.ID, "cookies").text.split()[-1]

# # modern version
# def get_cur_price(product_id):
#     return driver.find_element(By.CSS_SELECTOR, f"#{product_id} .price").text.split()[0]

def get_cur_price(product_id):
    return driver.find_element(By.CSS_SELECTOR, f"#{product_id} .price").text.split()[0]


def buy_most_expensive():
    temp_cookies = get_cur_cookies()
    cur_cookies = int("".join(temp_cookies.split(',')))
    for building in BUILDINGS:
        price = get_cur_price(building)
        real_price = int("".join(price.split(',')))
        if cur_cookies > real_price:
            driver.find_element(By.ID, building).click()
            # buy_most_expensive()


game_start = time.time()

while time.time() < game_start + 300:
    click_for_five()
    buy_most_expensive()

print("Cookies/second: " + get_cookies_per_second())

