import requests
from bs4 import BeautifulSoup

url = 'http://www.codewithtomu.ml/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class': 'post-title'})

for i in title.getText():
    print(i)