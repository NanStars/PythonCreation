import requests
from lxml import etree
from lxml import html

url = 'https://mitao1.tv:16888/vod/type/id/14/page/7.html'
ele = etree.HTML(requests.get(url).text)

tree3 = html.tostring(ele, encoding='utf-8').decode('utf-8')
print(tree3)
