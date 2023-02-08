# Import all-important Libraries
from bs4 import BeautifulSoup
import html5lib
import requests
from lxml import etree
import requests, csv, re
from lxml import etree

soup = BeautifulSoup(open('F:\python\selenium\供应商管理系统\detailHouseallocationGoods.htm', encoding='utf-8'),
                     features='html.parser')  # features值可为lxml
soup.encoding = 'utf-8'
html = soup.text
print(html)
e_html = etree.HTML(html)
Listing_No = e_html.xpath('')
print(Listing_No)
