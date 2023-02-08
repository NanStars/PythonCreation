import requests
from lxml import etree


def getHTMLText(url):
    cookie = "_sy_iu_0201=atmti7e7qmo57gfvaivrymf2ncdkgxg23eymofyajjznj5kufgzevxe627vpheyxqcjueqsdxdpfqhaviiiq3uvqlmnpseqlmrnw4lub2llgusalpzikfjeftriuiy2yzeorkiy2427vsuiemxupjcexji"
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
        film_name = e_html.xpath('/html/body/div[2]/div[2]/table/tbody/tr[2]/td[2]/a/text()')
        a = "".join(film_name)
        print(film_name)

        # print(a)

        return a
    except:
        return 'xx'


if __name__ == '__main__':
    url = input('url')
    getHTMLText(url)
