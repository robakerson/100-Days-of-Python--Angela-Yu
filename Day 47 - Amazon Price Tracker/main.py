from bs4 import BeautifulSoup
import lxml
import requests


URL = "https://www.amazon.com/Ninja-DZ201-2-Basket-Technology-Stainless/dp/B089TQWJKK/ref=sr_1_4?dchild=1&keywords=air+fryer&qid=1633920818&sr=8-4"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Accept-Language': 'en-US',
}

res = requests.get(url=URL, headers=headers)
res.raise_for_status()
# cur_site = res.text

soup = BeautifulSoup(res.content, 'lxml')
# print(soup.prettify)

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)