from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

zillow_search = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
webform = 'https://docs.google.com/forms/d/e/1FAIpQLSchd0igQnIZvLGD35U0LZKm0R_G8QGu46b6ujoEPxkJvnCZQw/viewform?usp=sf_link'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

driver.get(zillow_search)
time.sleep(4)

for _ in range(22):
    webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
for _ in range(120):
    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

html_data = driver.page_source
soup = BeautifulSoup(html_data, "html.parser")
property_list = soup.select("ul li article")

property_dic={}
for n in range(len(property_list)):
    address = property_list[n].select_one(".list-card-addr").getText()
    price = property_list[n].select_one(".list-card-price").getText().split("/")[0].split("+")[0]
    link = property_list[n].select_one(".list-card-link").get("href")
    # get absolute path
    link = urljoin(zillow_search, link)
    property_dic.update({n: {"address": f"{address}", "price": f"{price}", "link": f"{link}"}})

print(property_dic)

# property_dic = {0: {'adress': '2136 Alemany Blvd, San Francisco, CA 94112', 'price': '$3,000', 'link': 'https://www.zillow.com/homedetails/2136-Alemany-Blvd-San-Francisco-CA-94112/15188677_zpid/'}, 1: {'adress': '1537 Dolores St #2, San Francisco, CA 94110', 'price': '$2,500', 'link': 'https://www.zillow.com/homedetails/1537-Dolores-St-2-San-Francisco-CA-94110/2069138014_zpid/'}, 2: {'adress': '1377 9th Ave, San Francisco, CA 94122', 'price': '$2,600', 'link': 'https://www.zillow.com/homedetails/1377-9th-Ave-San-Francisco-CA-94122/2072143149_zpid/'}, 3: {'adress': '2211 Stockton St #1492387, San Francisco, CA 94133', 'price': '$2,810', 'link': 'https://www.zillow.com/homedetails/2211-Stockton-St-1492387-San-Francisco-CA-94133/2104934304_zpid/'}, 4: {'adress': '480 Potrero Ave | 480 Potrero Ave, San Francisco, CA', 'price': '$2,630', 'link': 'https://www.zillow.com/b/480-potrero-ave-san-francisco-ca-5mY4JQ/'}, 5: {'adress': '1177 Market at Trinity Place | 1177 Market St, San Francisco, CA', 'price': '$2,399', 'link': 'https://www.zillow.com/b/1177-market-at-trinity-place-san-francisco-ca-BNjvdD/'}, 6: {'adress': '168 Bluxome St, San Francisco, CA 94107', 'price': '$3,000', 'link': 'https://www.zillow.com/homedetails/168-Bluxome-St-San-Francisco-CA-94107/332860327_zpid/'}, 7: {'adress': '1285 Sutter St UNIT 307, San Francisco, CA 94109', 'price': '$2,958', 'link': 'https://www.zillow.com/homedetails/1285-Sutter-St-UNIT-307-San-Francisco-CA-94109/2110477891_zpid/'}, 8: {'adress': '545 Ofarrell St #202, San Francisco, CA 94102', 'price': '$1,995', 'link': 'https://www.zillow.com/homedetails/545-Ofarrell-St-202-San-Francisco-CA-94102/2072486434_zpid/'}, 9: {'adress': '801 E Jones St #308, San Francisco, CA 94109', 'price': '$2,450', 'link': 'https://www.zillow.com/homedetails/801-E-Jones-St-308-San-Francisco-CA-94109/2067846518_zpid/'}, 10: {'adress': 'The Landing | 1395 22nd St, San Francisco, CA', 'price': '$2,869', 'link': 'https://www.zillow.com/b/the-landing-san-francisco-ca-9NK3gC/'}, 11: {'adress': '840 Van Ness | 840 Van Ness Ave, San Francisco, CA', 'price': '$2,295', 'link': 'https://www.zillow.com/b/840-van-ness-san-francisco-ca-5YCwMj/'}, 12: {'adress': '825 Post St #201, San Francisco, CA 94109', 'price': '$2,395', 'link': 'https://www.zillow.com/homedetails/825-Post-St-201-San-Francisco-CA-94109/2067916051_zpid/'}, 13: {'adress': "750 O'Farrell St | 750 Ofarrell St, San Francisco, CA", 'price': '$1,850', 'link': 'https://www.zillow.com/b/750-o%27farrell-st-san-francisco-ca-5YXpvZ/'}, 14: {'adress': '950 Franklin | 950 Franklin St, San Francisco, CA', 'price': '$2,395', 'link': 'https://www.zillow.com/b/950-franklin-san-francisco-ca-5Xj398/'}, 15: {'adress': '1190 Mission St #1421, San Francisco, CA 94103', 'price': '$2,399', 'link': 'https://www.zillow.com/homedetails/1190-Mission-St-1421-San-Francisco-CA-94103/2080162369_zpid/'}, 16: {'adress': '405 6th Ave | 405 6th Ave, San Francisco, CA', 'price': '$2,195', 'link': 'https://www.zillow.com/b/405-6th-ave-san-francisco-ca-5Z59JL/'}, 17: {'adress': '400 Duboce Ave APT 413, San Francisco, CA 94117', 'price': '$2,995', 'link': 'https://www.zillow.com/homedetails/400-Duboce-Ave-APT-413-San-Francisco-CA-94117/2123966229_zpid/'}, 18: {'adress': '600 DIVISADERO/1290 HAYES | 600 Divisadero Hayes, San Francisco, CA', 'price': '$2,695', 'link': 'https://www.zillow.com/b/600-divisadero-1290-hayes-san-francisco-ca-C4Vnqh/'}, 19: {'adress': '1815 40th Ave FLOOR 1, San Francisco, CA 94122', 'price': '$2,800', 'link': 'https://www.zillow.com/homedetails/1815-40th-Ave-FLOOR-1-San-Francisco-CA-94122/2080438789_zpid/'}, 20: {'adress': '750 Fell St #1, San Francisco, CA 94117', 'price': '$2,600', 'link': 'https://www.zillow.com/homedetails/750-Fell-St-1-San-Francisco-CA-94117/2067795430_zpid/'}, 21: {'adress': 'Avalon Ocean Avenue | 1200 Ocean Ave, San Francisco, CA', 'price': '$2,632', 'link': 'https://www.zillow.com/b/avalon-ocean-avenue-san-francisco-ca-5XjSMb/'}, 22: {'adress': '1801 Wedemeyer St #119, San Francisco, CA 94129', 'price': '$2,775', 'link': 'https://www.zillow.com/homedetails/1801-Wedemeyer-St-119-San-Francisco-CA-94129/2078051040_zpid/'}, 23: {'adress': '95 Fairlawn Ave, Daly City, CA 94015', 'price': '$2,590', 'link': 'https://www.zillow.com/homedetails/95-Fairlawn-Ave-Daly-City-CA-94015/15458135_zpid/'}, 24: {'adress': 'Mosser Towers Apartments | 455 Eddy St, San Francisco, CA', 'price': '$2,050', 'link': 'https://www.zillow.com/b/mosser-towers-apartments-san-francisco-ca-9NJr4f/'}, 25: {'adress': '1060 Bush St #315, San Francisco, CA 94109', 'price': '$2,395', 'link': 'https://www.zillow.com/homedetails/1060-Bush-St-315-San-Francisco-CA-94109/2069134392_zpid/'}, 26: {'adress': '277 Golden Gate Ave #10389208, San Francisco, CA 94102', 'price': '$2,700', 'link': 'https://www.zillow.com/homedetails/277-Golden-Gate-Ave-10389208-San-Francisco-CA-94102/2068710654_zpid/'}, 27: {'adress': '240 Dolores St APT 126, San Francisco, CA 94103', 'price': '$2,899', 'link': 'https://www.zillow.com/homedetails/240-Dolores-St-APT-126-San-Francisco-CA-94103/2090430430_zpid/'}, 28: {'adress': '747 Eddy St #8, San Francisco, CA 94109', 'price': '$1,800', 'link': 'https://www.zillow.com/homedetails/747-Eddy-St-8-San-Francisco-CA-94109/2080400685_zpid/'}, 29: {'adress': '1363 7th Ave APT 2, San Francisco, CA 94122', 'price': '$2,795', 'link': 'https://www.zillow.com/homedetails/1363-7th-Ave-APT-2-San-Francisco-CA-94122/2096144724_zpid/'}, 30: {'adress': '1701 Turk St, San Francisco, CA 94115', 'price': '$2,495', 'link': 'https://www.zillow.com/homedetails/1701-Turk-St-San-Francisco-CA-94115/2067797127_zpid/'}, 31: {'adress': '401 Steiner St #5, San Francisco, CA 94117', 'price': '$2,650', 'link': 'https://www.zillow.com/homedetails/401-Steiner-St-5-San-Francisco-CA-94117/2067797146_zpid/'}, 32: {'adress': '199 New Montgomery St, San Francisco, CA 94105', 'price': '$3,000', 'link': 'https://www.zillow.com/homedetails/199-New-Montgomery-St-San-Francisco-CA-94105/2111358188_zpid/'}, 33: {'adress': '94 Robinson Dr, San Francisco, CA 94112', 'price': '$2,850', 'link': 'https://www.zillow.com/homedetails/94-Robinson-Dr-San-Francisco-CA-94112/15177827_zpid/'}, 34: {'adress': '1200 Gough St, San Francisco, CA', 'price': '$2,900 1 bd', 'link': 'https://www.zillow.com/b/1200-gough-st-san-francisco-ca-5YStz6/'}, 35: {'adress': 'Fox Plaza | 1390 Market St, San Francisco, CA', 'price': '$2,809', 'link': 'https://www.zillow.com/b/fox-plaza-san-francisco-ca-5Xj2b8/'}, 36: {'adress': '2440 Van Ness Ave #F08Z3F5EN, San Francisco, CA 94109', 'price': '$2,600', 'link': 'https://www.zillow.com/homedetails/2440-Van-Ness-Ave-F08Z3F5EN-San-Francisco-CA-94109/2071535114_zpid/'}, 37: {'adress': 'L Seven | 1222 Harrison St, San Francisco, CA', 'price': '$2,820', 'link': 'https://www.zillow.com/b/l-seven-san-francisco-ca-9NJtD7/'}, 38: {'adress': 'AVA 55 Ninth | 55 9th St, San Francisco, CA', 'price': '$2,580', 'link': 'https://www.zillow.com/b/ava-55-ninth-san-francisco-ca-5XkH8X/'}, 39: {'adress': '2834 Folsom St #D, San Francisco, CA 94110', 'price': '$2,150', 'link': 'https://www.zillow.com/homedetails/2834-Folsom-St-D-San-Francisco-CA-94110/2067800110_zpid/'}}

print(len(property_dic))

driver.get(webform)

for property in property_dic:
    price = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.click()
    price.send_keys(property_dic[property]['price'])
    link = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.click()
    link.send_keys(property_dic[property]['link'])
    address = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.click()
    address.send_keys(property_dic[property]['address'])
    submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(0.5)
    submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
    time.sleep(0.5)