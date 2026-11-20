from lxml import etree
import requests
import time
import re


class Myspider(object):
    def __init__(self):
        self.headers = {

        }
        self.url = 'https://m.ybmhpp2.vip/home/book/capter/id/3044'

    def run(self):
        try:
            target_urls = self.get_target_urls()
            self.get_target_images(target_urls)
        except Exception as e:
            print('错误原因', e)

    def get_target_urls(self):
        response = requests.get(self.url, headers=self.headers)
        text = response.content
        html = etree.HTML(text)
        target_urls = html.xpath(
            "//*[@id='framework7-root']/div[4]/div/div/div[2]/div[1]/article/section/div[1]/img/@src")
        return target_urls

    def download(self, target_urls):
        response = requests.get()

        pass


if __name__ == '__main__':
    spider = Myspider
    spider.run()

from bs4 import BeautifulSoup

url = 'https://m.ybmhpp2.vip/home/book/capter/id/3044'
response = requests.get(url)
print(response.status_code)
response.encoding = 'utf-8'
text = response.content

html = response.text
ele = etree.HTML(html)
urls = ele.xpath("//*[@id='framework7-root']/div[4]/div/div/div[2]/div[1]/article/section/div[1]/img/@src")

# //*[@id="framework7-root"]/div[4]/div/div/div[2]/div[1]/article/section/div[1]/img
'''soup = BeautifulSoup(html,'html.parser')
for link in soup.find_all('div[class="reader-cartoon-image loaded"]'):
    print(link.get('src'))'''
