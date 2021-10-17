from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # articlecount = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # print(articlecount.text)
# #
# #
# # all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up = driver.find_element(By.CSS_SELECTOR, "button")

fname.send_keys("Bob")
lname.send_keys("A")
email.send_keys("johnny@five.com")
sign_up.click()