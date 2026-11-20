import requests
from lxml import etree


def getHTMLText(url):
    cookie = "******"
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
        e_html = etree.HTML(html)
        film_name = e_html.xpath('/html/body/div[1]/div[1]/div[2]/a/h2/text()')  # 电影名称
        film_name1 = e_html.xpath('/html/body/div[1]/div[2]/div[2]/a/h2/text()')
        a = "".join(film_name)
        b = "".join(film_name1)
        print("已退回：", b)

        # print(a)

        return a
    except:
        return 'xx'


if __name__ == '__main__':
    url = 'http://******'
    print('相遇单子数目'.center(35, '-'))
    b = str('0')
    asd = getHTMLText(url)
    if asd > b:
        print('待派工：', asd)
    else:
        print('没有单子')
