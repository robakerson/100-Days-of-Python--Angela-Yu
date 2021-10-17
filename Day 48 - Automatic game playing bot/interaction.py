from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articlecount = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(articlecount.text)

driver.quit()