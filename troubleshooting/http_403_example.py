# a

import urllib

url = 'http//:****'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)  # 这里要注意，必须使用url=url，headers=headers的格式，否则回报错，无法连接字符

response = urllib.request.urlopen(req)  # 注意，这里要用req，不然就被添加useragent

# b
# 那我们换一个支持 HTTP/2.0 的库呢？比如 httpx，安装方法如下：
'''
pip3 install 'httpx[http2]'
'''
