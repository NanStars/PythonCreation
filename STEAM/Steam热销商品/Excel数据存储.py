import requests
from scrapy import Selector
import pandas as pd

#没有代理ip
class getSteamInfo():
    headers = {
        "Host": "store.steampowered.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    }

    url = []
    name = []
    sales_date = []
    discount = []
    price = []

    # api获取ip
    def getApiIp(self):
        # 获取且仅获取一个ip
        api_url = 'api地址'
        res = requests.get(api_url, timeout=5)
        try:
            if res.status_code == 200:
                api_data = res.json()['data'][0]
                proxies = {
                    'http': 'http://{}:{}'.format(api_data['ip'], api_data['port']),
                    'https': 'http://{}:{}'.format(api_data['ip'], api_data['port']),
                }
                print(proxies)
                return proxies
            else:
                print('获取失败')
        except:
            print('获取失败')

    def getInfo(self):
        url = 'https://store.steampowered.com/search/results/?query&start=0&count=50&sort_by=_ASC&os=win&snr=1_7_7_globaltopsellers_7&filter=globaltopsellers&infinite=1'
        res = self.getRes(url, self.headers, '', '', 'GET')  # 自己封装的请求方法
        res = res.json()['results_html']
        sel = Selector(text=res)
        nodes = sel.css('.search_result_row')
        for node in nodes:
            url = node.css('a::attr(href)').extract_first()
            if url not in self.url:
                self.url.append(url)
                name = node.css('a .search_name .title::text').extract_first()
                sales_date = node.css('a .search_released::text').extract_first()
                discount = node.css('.search_discount span::text').extract_first()
                discount = discount if discount else 'no discount'
                price = node.css('a .search_price::text').extract_first().strip()
                discountPrice = node.css('.discounted::text').extract()
                discountPrice = discountPrice[-1] if discountPrice else ''
                price = discountPrice if discountPrice else price
                self.name.append(name)
                self.sales_date.append(sales_date)
                self.discount.append(discount)
                self.price.append(price)
            else:
                print('已存在')
        # self.insert_info()

    def insert_info(self):
        data = {
            'URL': self.url, '游戏名': self.name, '发售日': self.sales_date, '是否打折': self.discount, '价格': self.price
        }
        frame = pd.DataFrame(data)
        xlsxFrame = pd.read_excel('./steam.xlsx')
        print(xlsxFrame)
        if xlsxFrame is not None:
            print('追加')
            frame = frame.append(xlsxFrame)
            frame.to_excel('./steam.xlsx', index=False)
        else:
            frame.to_excel('./steam.xlsx', index=False)

    # 专门发送请求的方法,代理请求三次，三次失败返回错误
    def getRes(self, url, headers, proxies, post_data, method):
        if proxies:
            for i in range(3):
                try:
                    # 传代理的post请求
                    if method == 'POST':
                        res = requests.post(url, headers=headers, data=post_data, proxies=proxies)
                    # 传代理的get请求
                    else:
                        res = requests.get(url, headers=headers, proxies=proxies)
                    if res:
                        return res
                except:
                    print(f'第{i + 1}次请求出错')
                else:
                    return None
        else:
            for i in range(3):
                proxies = self.getApiIp()
                try:
                    # 请求代理的post请求
                    if method == 'POST':
                        res = requests.post(url, headers=headers, data=post_data, proxies=proxies)
                    # 请求代理的get请求
                    else:
                        res = requests.get(url, headers=headers, proxies=proxies)
                    if res:
                        return res
                except:
                    print(f"第{i + 1}次请求出错")
                else:
                    return None


if __name__ == '__main__':
    getSteamInfo().getInfo()