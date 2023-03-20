import requests
from lxml import etree
import requests, csv, re
from lxml import etree

def getHTMLText(url):
    cookie = "*********"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Cookie': cookie
    }
    try:
        r = requests.get(url, headers=headers, timeout=30)
        # r = requests.get(url, headers=headers,timeout=30,proxies=get_random_ip(ip_list))
        r.raise_for_status()
        r.encoding = 'utf-8'
        html = r.text
        print(html)
        e_html = etree.HTML(html)
        #Listing_No = e_html.xpath('/html/body/div[1]/div/table/tbody/tr[1]/td[1]/h5/text()')


        #a = "".join(Listing_No)
        #print(Listing_No)

        # print(a)

        return a
    except:
        return 'xx'


if __name__ == '__main__':
    url = '********'
    getHTMLText(url)
