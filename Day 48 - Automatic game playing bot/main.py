from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# deprecated
# chrome_driver_path = "C:/Users/Bob/Desktop/WebDev/100 Days of Python -Angela Yu/chromedriver_win32/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.google.com')


# open a webpage
driver.get("https://www.amazon.com")


# close the browser
# driver.close()
driver.quit()