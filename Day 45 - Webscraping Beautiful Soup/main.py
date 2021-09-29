from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

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

all_headings = soup.select(selector=".heading")  # select all elements with class of heading
print(all_headings)

