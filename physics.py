import requests
from bs4 import BeautifulSoup

url = 'https://arxiv.org/list/physics/new'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

articles = soup.find_all('div', class_='list-title mathjax')
links = soup.find_all('span', class_='list-identifier')
count = 1
for article, link in zip(articles, links):
    print(str(count) + '.')
    print('\t' + article.text[8:].strip('\n'))
    print('\t' + 'https://arxiv.org' + link.contents[2]['href'])
    count += 1
