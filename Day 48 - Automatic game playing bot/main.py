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

# open a webpage
driver.get("https://www.amazon.com/SAMSUNG-Adjustable-TUV-Certified-Intelligent-LS34A650UXNXGO/dp/B08V71HXY3/?_encoding=UTF8&pd_rd_w=SyuEX&pf_rd_p=8b894231-4b84-44da-9446-c27cf0e8abc2&pf_rd_r=G7MHA3TQANNE9BCZ7D07&pd_rd_r=20fb8069-6a4c-4704-ae9b-60378e4a183e&pd_rd_wg=7Ot9R&ref_=pd_gw_ci_mcx_mr_hp_d")
price = driver.find_element(By.ID, "priceblock_ourprice")
print(price.text)


# close the browser
# driver.close()
driver.quit()