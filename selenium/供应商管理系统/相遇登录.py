from selenium.webdriver.common.by import By
import requests
import time
import pytesseract
from PIL import Image
from selenium import webdriver
from time import sleep
from lxml import etree
import json
import csv

# 创建一个浏览器
browser = webdriver.Chrome()
TOKEN = 'free'  # token 获取：http://www.bhshare.cn/imgcode/gettoken
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址


def breakvcode():
    # 打网站
    browser.get("*******")
    sleep(2)  # 两秒以后
    email = browser.find_element(By.ID, "username")  # 获取账号input
    email.send_keys("*******")  # 填写账号
    time.sleep(2)
    pwd = browser.find_element(By.ID, "password")  # 获取密码input
    time.sleep(2)
    pwd.send_keys("*****")  # 填写密码
    time.sleep(2)
    browser.get_screenshot_as_file('img.png')
    vcode = browser.find_element(By.XPATH, "//img[@id='check_code']")
    print("vcode", vcode)  # 打印看一下是否获取成功标签
    print("vcode.location", vcode.location)  # 打印验证码图片坐标
    print("vcode.size", vcode.size)  # 打印验证码图片尺寸
    left = vcode.location['x']  # 左上角起点x轴坐标
    top = vcode.location['y']  # 左上角起点y轴坐标
    right = vcode.location['x'] + vcode.size['width']  # 右下角终点x轴坐标
    bottom = vcode.location['y'] + vcode.size['height']  # 右下角终点y轴坐标
    img = Image.open('img.png')  # 打开之前截图
    img = img.crop((left, top, right, bottom))  # 按照验证码的坐标重新截取
    img.save('Vcode.png')  # 保存成新的图片 此时为验证码
    image = Image.open("Vcode.png")  # 打开验证码图片
    image = image.convert('L')  # 把图片传入'L'，转化为灰度图像
    image.save('VLcode.png', 'jpeg')  # 最终的图片


def imgcode_local(imgpath):
    """
    本地图片识别
    :param imgpath: 本地图片路径
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'local'
    }

    # binary上传文件
    files = {'file': open(imgpath, 'rb')}

    response = requests.post(URL, files=files, data=data)
    # print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


def Verification_code_writing(text):
    code = browser.find_element(By.ID, "checkCode")  # 获取到验证码input
    code.send_keys(text)  # 输入验证码
    time.sleep(2)
    denglu = browser.find_element(By.CLASS_NAME, "login_btn")  # 获取登录按钮
    denglu.click()  # 点击登录
    sleep(2)


def Number_of_orders():
    html = browser.page_source  # 提取网页源码
    print(html)

    # In[66]:

    # 使用xpth解析网页
    e_html = etree.HTML(html)

    film_name = e_html.xpath('//*[@id="content"]/h1/span[1]/text()')  # 电影名称
    print(film_name)

    year = e_html.xpath('//*[@id="content"]/h1/span[2]/text()')  # 年份
    print(year)

    director = e_html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')  # 导演
    print(director)

    types = e_html.xpath('//*[@id="info"]/span[5]/text()')  # 类型
    print(types)

    score = e_html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')  # 
    print(score)


if __name__ == '__main__':
    try:
        breakvcode()
        time.sleep(2)
        Verification_code_writing(imgcode_local('VLcode.png'))
    except Exception as e:
        print("错误", e)
        breakvcode()
