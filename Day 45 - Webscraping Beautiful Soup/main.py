from bs4 import BeautifulSoup
import requests

res = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = res.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

articles = soup.find_all(name='a', class_='storylink')

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# print(article_texts)
# print(article_links)
# print(article_scores)

index_of_highest_score = article_scores.index(max(article_scores))  # find index of highest scoring article

print(article_texts[index_of_highest_score])  # print text from highest scoring article
print(article_links[index_of_highest_score])  # print link from highest scoring article


# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.meta)
# print(soup.title.text)

# all_anchor_tags = soup.find_all(name='a')  # find all tags with name 'a' ie anchor tags, as a list
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())  # print the title of each tag
#     # print(tag.get('href'))  # print the link from each tag
#     pass

# heading = soup.find(name='h1', id='name')  # find specific h1 tag
# print(heading)

# section_heading = soup.find(name='h3', class_="heading")  # if grabbing class, need to use class_ as "class" is reserved
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")  # "p a" is the CSS selector that finds the anchor tag that lies within a paragraph tag
# print(company_url)
#
# all_headings = soup.select(selector=".heading")  # select all elements with class of heading
# print(all_headings)
#
