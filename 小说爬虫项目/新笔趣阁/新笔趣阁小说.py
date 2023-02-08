import requests
from lxml import etree
from tqdm import tqdm

url = "https://www.xbiquge.la/xiaoshuodaquan/"
response = requests.get(url)
response.encoding = "utf-8"
html = response.text
# ele
ele = etree.HTML(html)
book_names = ele.xpath("//div[@id='main']/div[@class='novellist']/ul/li/a/text()")
book_urls = ele.xpath("//div[@id='main']/div[@class='novellist']/ul/li/a/@href")
s = ''
for book_name in range(len(book_names)):
    s += book_names[book_name] + '\n' + book_urls[book_name] + '\n'
with open('title.txt', 'w', encoding='utf-8') as file:
    file.writelines(s)
print("输入完成")

with open("title.txt", 'r', encoding='utf-8') as file:
    s = file.read()
    # print(s)
s = s.split("\n")

title = s[0]
url = s[1]
# print(title)
# print(url)
response = requests.get(url)
response.encoding = "utf-8"
html = response.text
# print(html)
ele = etree.HTML(html)
book_chapters = ele.xpath("//div[@class='box_con']/div[@id='list']/dl/dd/a/text()")
# book_author = ele.xpath("")
book_c_urls = ele.xpath("//div[@class='box_con']/div[@id='list']/dl/dd/a/@href")

s = ""
for book_chapter in range(len(book_chapters)):
    s += book_chapters[book_chapter] + "\n" + book_c_urls[book_chapter] + "\n"
with open("chapter.txt", "w", encoding='utf-8') as f:
    f.write(s)
print("输入完成！")
with open("chapter.txt", 'r', encoding='utf-8') as file:
    s = file.read()
    # print(s)
s = s.split("\n")

chapter_titles = s[::2]
chapter_urls = s[1::2]


def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())


o_url = "https://www.xbiquge.la"
# new_url =  o_url +  chapter_urls[0]
pbar = tqdm(range(len(chapter_urls)))
for i in pbar:
    new_url = o_url + chapter_urls[i]

    # print(new_url)
    response = requests.get(new_url)
    response.encoding = "utf-8"
    html = response.text
    # print(html)
    ele = etree.HTML(html)
    book_bodys = ele.xpath("//div[@id='content']/text()")
    # print(book_bodys[0])
    s = "\n" + chapter_titles[i] + "\n"

    for book_body in book_bodys:
        c = "".join(book_body.split())
        c = remove_upprintable_chars(c)
        s += c
    with open("牧神记.txt", "a") as f:
        f.write(s)

print("文章《牧神记》 下载完毕！")
