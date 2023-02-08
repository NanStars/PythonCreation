# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
with open('STEAM_DB.html', 'r', encoding='utf-8') as fp:
    r = fp.read()
bf = BeautifulSoup(r, "lxml")
for items in bf.find_all('div', class_='package'):
    item = items.find('a')
    url1 = item.get('href')
    with open('subid.txt', 'a', encoding='utf-8') as file:
        file.write(item.string + '\n')
