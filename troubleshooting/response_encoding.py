
# 中文乱码
import requests
url ="https://www.iqiyi.com/"
header = \
    {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
html = requests.get(url, headers=header).text
print(html)
# 输出结果
'''
æ­²ï¼ææªæ»¿ç¶å°æ³å¾è¨
±å¯çæ³å®å¹´é½¡ï¼å»ºè­°æ¨
é¢éæ¬ç«ï¼
'''

# 解决方案
import requests

url = "https://www.iqiyi.com/"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
html = requests.get(url, headers=header)
html.encoding = "utf-8"
MyHtml = html.text
print(MyHtml)
